# Sparkify NoSQL DataMart
This project aims at modeling database around queries to facilitate the insights for Sparkify(a music streaming company).
The insights required to be mined include following sample questions.
1. Give me the artist, song title and song's length in the music app history that was heard during sessionId = 338, and itemInSession = 4
2. Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, 
   sessionid = 182
3. Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'

## Dataset
Data is events created in the music streaming app in the form of CSV files. As Cassandra will not support the joins, the database models to answer these queries need to be modeled keeping queries in mind. The files will be extracted to create a denormalized dataset named event_datafile_new.csv which will contain all the attributes required to answer above questions. The dataset event_datafile_new.csv contains data mentioned below:
![Sample events datafile](https://github.com/bhosalem/SparkifyNoSQLDataMart/blob/master/image_event_datafile_new.jpg)

## Primary key and clustering key criteria
### 1. To fetch the artist, song title and song's length in the music app history that was heard during sessionId = 338 and itemInSession         = 4
    As we need to analyse data for sessionId=338 and itemInSession =4, the good data distribution criteria can be achived by using
    partition key as sessionId and  data sorting within partition can be achived by itemInSession attribute. Together these columns
    also help identify rows uniquely
### 2. To fetch name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182
    As data needs to be filtered on userId and sessionId, we can start with userId as partition key as it gives good distribution of         data.But at the same time we need the data to be orted by itemInSession so clustering key will be used as a combination of               sessionId and itemInSession. Combination of userId,sessionId and iteminSession can identify rows uniquely.
### 3. To fetch every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'
    Though,song can be used a primary key as it can identify rows uniquely and partition the data on songs it will be wise to use userid as a clustering key as there could be multiple users listening to same song at any point in time.
 
 ## ETL process
 As a part of ETL, following tasks will be performed by sparkify_nosql_etl.py script
 1. Scan through the data directory and list all the files 
 2. Read each of the file identified in step 1 and extract required columns and create a denormalized dataset event_datafile_new.csv
 3. For each query, read dataset event_datafile_new.csv and insert rows into respective database tables.
 
# Run Instructions
Run the python scripts mentioned below in console
1. Run script sparkify_nosql_create_tables.py : Creates Apache Cassandra keyspace and tables required to model queries
2. Run script sparkify_nosql_etl.py : Extracts and loads data into tables
3. run script sparkify_nosql_select.py : Runs the required select statements and displays results in console

# Query output
Refer below the output of three queries in question for this project.
![select statement outputs](images/Select_queries_output.PNG)

        
