# SparkifyNoSQLDataMart
This project aims at modeling database around queries to facilitate the insights for Sparkify(a music streaming company).
The insights required to be mined include following sample questions.
1. Give me the artist, song title and song's length in the music app history that was heard during sessionId = 338, and itemInSession = 4
2. Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, 
   sessionid = 182
3. Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'

## Dataset
Data is events created in the music streaming app in the form of CSV files. As Cassandra will not support the joins, the database models to answer these queries need to be modeled keeping queries in mind. The files will be extracted to create a denormalized dataset named event_datafile_new.csv which will contain all the attributes required to answer above questions. The dataset event_datafile_new.csv contains data mentioned below:
![Sample events datafile]()
