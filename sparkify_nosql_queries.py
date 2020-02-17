#DROP TABLES
drop_music_hist_in_session="DROP TABLE IF EXISTS music_hist_in_session;"
drop_user_info_in_session="DROP TABLE IF EXISTS user_info_in_session;"
drop_users_listening_song="DROP TABLE IF EXISTS users_listening_song;"

#CREATE TABLES
create_music_hist_in_session = "CREATE TABLE IF NOT EXISTS music_hist_in_session(sessionId int,itemInSession int,artist text,song text,length double, PRIMARY KEY (sessionId,itemInSession));"

create_user_info_in_session = "CREATE TABLE IF NOT EXISTS user_info_in_session (userid int,sessionid int,itemInSession int,artist text,song text,first_name text,last_name text, PRIMARY KEY ((userid),sessionid,itemInSession));"

create_users_listening_song = "CREATE TABLE IF NOT EXISTS users_listening_song(song text,userid int,first_name text,last_name text, PRIMARY KEY (song,userid));"

#INSERT RECORDS
insert_music_hist_in_session = "insert into music_hist_in_session (sessionId,itemInSession,artist,song,length) VALUES (%s,%s,%s,%s,%s);"

insert_user_info_in_session = "insert into user_info_in_session (userid,sessionid,itemInSession,artist,song,first_name,last_name) VALUES (%s,%s,%s,%s,%s,%s,%s);"

insert_users_listening_song="insert into users_listening_song (song,userid,first_name,last_name) VALUES (%s,%s,%s,%s);"

#SELECT QUERIES
select_music_hist_in_session="select sessionId,itemInSession,artist,song,length from music_hist_in_session where sessionId=338 and iteminsession=4;"

select_user_info_in_session="select artist,song,first_name,last_name from user_info_in_session where userid=10 and sessionid=182;"

select_users_listening_song="select first_name,last_name from users_listening_song where song='All Hands Against His Own';"


drop_queries=[drop_music_hist_in_session,drop_user_info_in_session,drop_users_listening_song]
create_table_queries=[create_music_hist_in_session,create_user_info_in_session,create_users_listening_song]
insert_queries=[insert_music_hist_in_session,insert_user_info_in_session,insert_users_listening_song]
select_queries=[select_music_hist_in_session,select_user_info_in_session,select_users_listening_song]
