import mysql.connector

mydb = mysql.connector.connect(
    host="0.0.0.0", #name given in docker compose
    user="root",
    passwd="changeme"
)

cursor = mydb.cursor()
cursor.execute("CREATE DATABASE mspaintr_db")
cursor.execute("CREATE TABLE IF NOT EXISTS Users ("
               "username VARCHAR(20) NOT NULL, "
               "password VARCHAR(45), "
               "bio VARCHAR(255), "
               "followers INT")
cursor.execute("CREATE TABLE IF NOT EXISTS Posts ("
               "postid VARCHAR(255), "
               "image VARCHAR(255),"
               "upvotes INT, "
               "Users_username VARCHAR (20))")
cursor.execute("CREATE TABLE IF NOT EXISTS Comments("
               "commentid INT, "
               "comment VARCHAR(255), "
               "Posts_postid VARCHAR(255), "
               "Users_username VARCHAR(20))")
