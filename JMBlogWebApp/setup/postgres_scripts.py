LIST_DATABASES_SCRIPT = "SELECT datname FROM pg_database"

SEARCH_DATABASE_SCRIPT = "SELECT EXISTS(SELECT datname FROM pg_catalog.pg_database \
WHERE lower(datname) = lower('%s'))::bool;"

SEARCH_TABLE_SCRIPT = "SELECT EXISTS(SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME='%s')"

CREATE_DATABASE_SCRIPT = "CREATE DATABASE IF NOT EXISTS posts"

CREATE_USERS_SCRIPT = "CREATE TABLE IF NOT EXISTS users(user_id uuid UNIQUE,\
user_name varchar UNIQUE,\
user_email varchar,\
user_password varchar,\
user_created_at timestamp,\
user_modified_at timestamp);"

CREATE_POSTS_SCRIPT = "CREATE TABLE IF NOT EXISTS posts(posts_id uuid UNIQUE,\
creation_date timestamp,\
edit_date timestamp,\
author uuid UNIQUE,\
title varchar,\
post_content varchar,\
PRIMARY KEY(posts_id),\
FOREIGN KEY(author)\
    REFERENCES users(user_id) ON DELETE CASCADE);"

CREATE_ADMIN_SCRIPT = "INSERT INTO USERS(user_id, user_name, user_password)\
VALUES ('45137158-83d4-4871-9b50-2df81746cf29',\
'admin','8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918')"

CREATE_FULL_DATABASE = [CREATE_DATABASE_SCRIPT, CREATE_USERS_SCRIPT, CREATE_POSTS_SCRIPT, CREATE_ADMIN_SCRIPT]