CREATE TABLE
    IS601_Users(
        id int auto_increment PRIMARY KEY,
        username VARCHAR(60) not null unique default (substring_index(email, '@', 1)) COMMENT 'Username field that defaults to the name of the email',
        email VARCHAR(60) unique,
        password VARCHAR(60) not null,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )