CREATE_DATABASE_SCRIPT = "CREATE DATABASE {}"

ID_GENERATOR_SCRIPT = "CREATE EXTENSION IF NOT EXISTS \"pgcrypto\""

CREATE_USERS_SCRIPT = "CREATE TABLE IF NOT EXISTS users(user_id uuid default \
gen_random_uuid() primary key unique not null, \
user_name varchar unique not null, \
user_email varchar, \
user_password varchar, \
user_created_at timestamp, \
user_modified_at timestamp)"

CREATE_POSTS_SCRIPT = "CREATE TABLE IF NOT EXISTS posts(posts_id uuid UNIQUE,\
creation_date timestamp,\
edit_date timestamp,\
author uuid not null,\
title varchar,\
post_content varchar,\
PRIMARY KEY(posts_id),\
FOREIGN KEY(author)\
    REFERENCES users(user_id) ON DELETE CASCADE);"

CREATE_ADMIN_SCRIPT = "INSERT INTO USERS \
(user_name, user_password) \
VALUES \
('admin', \
'8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918') \
on conflict do nothing"

TRANSFER_USERS_SCRIPT = "do $$ \
begin \
       if (select pg_typeof(author) from posts limit 1)::regtype = 'character varying'::regtype then \
           insert into users(user_name) select distinct author from posts on conflict do nothing; \
       end if;\
end $$"

UPDATE_POST_AUTHORS_COLUMN = "do $$ \
	begin \
		if (select pg_typeof(author) from posts limit 1)::regtype = 'character varying'::regtype then \
		update posts set author = users.user_id from users where users.user_name = posts.author; \
		end if; \
end $$"

UPDATE_POST_AUTHORS_DATATYPE = "alter table posts alter column \
author type uuid using author::uuid"

ALL_SCRIPTS = [
    ID_GENERATOR_SCRIPT,
    CREATE_POSTS_SCRIPT,
    CREATE_USERS_SCRIPT,
    CREATE_ADMIN_SCRIPT,
    TRANSFER_USERS_SCRIPT,
    UPDATE_POST_AUTHORS_COLUMN,
    UPDATE_POST_AUTHORS_DATATYPE]
