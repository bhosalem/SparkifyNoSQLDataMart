from cassandra.cluster import Cluster
from sparkify_nosql_queries import drop_queries,create_table_queries

def create_keyspace():
    # This should make a connection to a Cassandra instance your local machine 
    # (127.0.0.1)
    try:
        cluster = Cluster(['127.0.0.1'])
        # To establish connection and begin executing queries, need a session
        session = cluster.connect()
    except Exception as e:
        print(e)
        
    #Create a Keyspace 
    try:
        session.execute("""CREATE KEYSPACE IF NOT EXISTS udacity 
        WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };""")
    except Exception as e:
        print(e)
    
    #Set KEYSPACE to the keyspace specified above
    try:
        session.set_keyspace('udacity')
    except Exception as e:
        print(e)
    return cluster,session

def drop_tables(session):
    for query in drop_queries:
        try:
            session.execute(query)
        except Exception as e:
            print(e)
            
def create_tables(session):
    for query in create_table_queries:
        try:
            session.execute(query)
        except Exception as e:
            print(e)
            
def main():
    cluster,session = create_keyspace()
    drop_tables(session)
    create_tables(session)
    session.shutdown()
    cluster.shutdown()

if __name__ == "__main__":
    main()
