SHOW DATABASES LIKE mspaintrdb;
CREATE DATABASE IF NOT EXISTS mspaintrdb;
USE mspaintrdb;
CREATE TABLE IF NOT EXISTS Users(
    username VARCHAR(20) NOT NULL,
    password VARCHAR(45),
    bio VARCHAR(255),
    followers INT
    );
CREATE TABLE IF NOT EXISTS Posts (
    postid VARCHAR(255),
    image VARCHAR(255),
    upvotes INT,
    Users_username VARCHAR (20)
    );
CREATE TABLE IF NOT EXISTS Comments(
    commentid INT,
    comment VARCHAR(255),
    Posts_postid VARCHAR(255),
    Users_username VARCHAR(20)
    );

INSERT INTO Users (username, password, bio, followers)
VALUES ('defaultuser', 'defaultpass', 'This is the default bio!', 0);