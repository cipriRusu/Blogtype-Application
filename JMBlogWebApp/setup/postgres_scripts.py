CREATE_DATABASE_SCRIPT = "CREATE DATABASE %s;"

LIST_DATABASES_SCRIPT = "SELECT datname from pg_database"

SEARCH_TABLE_SCRIPT = "SELECT EXISTS(SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME=%s)"

CREATE_TABLE_SCRIPT = "CREATE TABLE POSTS(posts_id uuid,\
creation_date timestamp,\
edit_date timestamp,\
author uuid,\
title varchar,\
post_content varchar,\
PRIMARY KEY(posts_id),\
FOREIGN KEY(author)\
    REFERENCES users(user_id));"

CREATE_USERS_SCRIPT = "CREATE TABLE USERS(user_id uuid,\
user_name varchar UNIQUE,\
user_email varchar,\
user_password varchar,\
user_created_at timestamp,\
user_modified_at timestamp);"