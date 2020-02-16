""" This file run the select statements against each of the able and prints the results to the console
"""
import cassandra
from cassandra.cluster import Cluster
from sparkify_nosql_create_tables import create_keyspace
from sparkify_nosql_queries import select_queries,select_music_hist_in_session
#select_music_hist_in_session,select_user_info_in_session,select_users_listening_song


def run_query(session,query):
    print('========================================================================================================\n')
    print('Running query: '+query)
    try:
        rows=session.execute(query)
    except Exception as e:
        print(e)
    print('----Result----')
    for row in rows:
        print(list(row))
    
def main():
    cluster,session=create_keyspace()
    #run_query(session,select_music_hist_in_session)
    for query in select_queries:
        run_query(session,query)
    session.shutdown()
    cluster.shutdown()

if __name__ == "__main__":
    main()
