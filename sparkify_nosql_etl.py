# Import Python packages 
import pandas as pd
import cassandra
import re
import os
import glob
import numpy as np
import json
import csv
from decimal import Decimal
from sparkify_nosql_create_tables import create_keyspace
from sparkify_nosql_queries import insert_queries,insert_music_hist_in_session,insert_user_info_in_session,insert_users_listening_song

file = 'event_datafile_new.csv'

def read_files(filepath):
    """This function parses the filepath creates list of all the files present in the directory.
    Then reads all the files in the list and creates an intermediate denormalized dataset which will
    be used to insert into the database tables
    
    input parameter : filepath where data csv files are stored
    
    returns : none
    """
    file_count=1
    # Create a for loop to create a list of files and collect each filepath
    for root, dirs, files in os.walk(filepath):
        # join the file path and roots with the subdirectories using glob
        file_path_list = glob.glob(os.path.join(root,'*'))
        
    # get total number of files found
    num_files = len(file_path_list)
    print('{} files found in {}'.format(len(file_path_list), filepath))
    # initiating an empty list of rows that will be generated from each file
    full_data_rows_list = [] 
    # for every filepath in the file path list 
    for f in file_path_list:
        print('{}/{} files processed.'.format(file_count, num_files))
        # reading csv file 
        with open(f, 'r', encoding = 'utf8', newline='') as csvfile: 
            # creating a csv reader object 
            csvreader = csv.reader(csvfile) 
            next(csvreader)
            # extracting each data row one by one and append it        
            for line in csvreader:
                full_data_rows_list.append(line)
        file_count+=1
    # creating a smaller event data csv file called event_datafile_full csv that will be used to insert data into the \
    # Apache Cassandra tables
    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    with open(file, 'w', encoding = 'utf8', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(['artist','firstName','gender','itemInSession','lastName','length',\
                    'level','location','sessionId','song','userId'])
        for row in full_data_rows_list:
            if (row[0] == ''):
                continue
            writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))

def insert_records(session):
    """This function reads the file created in earlier step and loads into the database tables.
    
    input : session object to connect to cassandra db.
    returns : none"""
    print('Now inserting records into analytics tables.')
    with open(file, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader) # skip header
        for line in csvreader:
                    try:
                        session.execute(insert_music_hist_in_session,(int(line[8]),int(line[3]),line[0],line[9],Decimal(line[5])))                
                    except Exception as e:
                        print('Table insert for music history in a sesion failed\n')
                        print(e)
                        
                    try:
                        session.execute(insert_user_info_in_session,(int(line[10]),int(line[8]),int(line[3]),line[0],line[9],line[1],line[4]))
                    except Exception as e:
                        print('Table insert for user information in a sesion failed\n')
                        print(e)
                        
                    try:
                        session.execute(insert_users_listening_song,(line[9],int(line[10]),line[1],line[4]))
                    except Exception as e:
                        print('Table insert for users listening to a song failed\n')
                        print(e)
    print('Data inserted successfully in analytics tables.')

def main():
    filepath = os.getcwd() + '/event_data'
    cluster,session=create_keyspace()
    read_files(filepath)
    insert_records(session)
    session.shutdown()
    cluster.shutdown()

if __name__ == "__main__":
    main()