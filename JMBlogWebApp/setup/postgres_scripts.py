ID_GENERATOR_SCRIPT = "CREATE EXTENSION IF NOT EXISTS \"pgcrypto\""

CREATE_DATABASE_SCRIPT = "CREATE DATABASE {}"

CREATE_USERS_SCRIPT = "CREATE TABLE IF NOT EXISTS users(user_id uuid UNIQUE,\
user_name varchar UNIQUE,\
user_email varchar,\
user_password varchar,\
user_created_at timestamp,\
user_modified_at timestamp);"

TRANSFER_USERS_SCRIPT = "insert into users(user_id, user_name) \
select distinct gen_random_uuid(), author from posts"

UPDATE_POST_AUTHORS_COLUMN = "update posts set \
author = users.user_id from users where users.user_name = posts.author"

UPDATE_POST_AUTHORS_DATATYPE = "alter table posts \
alter column author type uuid using author::uuid"

CREATE_POSTS_SCRIPT = "CREATE TABLE IF NOT EXISTS posts(posts_id uuid UNIQUE,\
creation_date timestamp,\
edit_date timestamp,\
author uuid not null,\
title varchar,\
post_content varchar,\
PRIMARY KEY(posts_id),\
FOREIGN KEY(author)\
    REFERENCES users(user_id) ON DELETE CASCADE);"

CREATE_ADMIN_SCRIPT = "INSERT INTO USERS(user_id, user_name, user_password)\
VALUES ('45137158-83d4-4871-9b50-2df81746cf29',\
'admin','8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918') ON CONFLICT DO NOTHING"

CREATE_ALL_DB_RELATIONS = [CREATE_USERS_SCRIPT,
                           CREATE_POSTS_SCRIPT,
                           CREATE_ADMIN_SCRIPT]

UPDATE_EXISTING_DB = [ID_GENERATOR_SCRIPT,
                      CREATE_USERS_SCRIPT,
                      CREATE_ADMIN_SCRIPT,
                      TRANSFER_USERS_SCRIPT,
                      UPDATE_POST_AUTHORS_COLUMN,
                      UPDATE_POST_AUTHORS_DATATYPE]
