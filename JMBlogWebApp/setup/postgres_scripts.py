CREATE_DATABASE_SCRIPT = "CREATE DATABASE %s;"

LIST_DATABASES_SCRIPT = "SELECT datname from pg_database"

SEARCH_TABLE_SCRIPT = "SELECT EXISTS(SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME=%s)"

CREATE_TABLE_SCRIPT = "CREATE TABLE POSTS(posts_id uuid,\
creation_date timestamp,\
edit_date timestamp,\
author varchar,\
title varchar,\
post_content varchar);"
