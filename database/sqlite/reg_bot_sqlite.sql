--
-- File generated with SQLiteStudio v3.4.3 on Sat May 27 16:44:14 2023
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: drop_accs
CREATE TABLE IF NOT EXISTS drop_accs (
    id_drop_accs  INTEGER PRIMARY KEY AUTOINCREMENT,
    tg_id         INTEGER UNIQUE
                          NOT NULL,
    tg_username   TEXT    NOT NULL,
    first_name    TEXT,
    middle_name   TEXT,
    surname       TEXT,
    country       TEXT,
    region        TEXT,
    city          TEXT,
    address       TEXT,
    postcode      TEXT,
    date_of_birth TEXT,
    document_id   TEXT,
    phone_number  TEXT,
    referral_id   INTEGER,
    language      TEXT    NOT NULL
                          DEFAULT ru,
    verified      INTEGER NOT NULL
                          DEFAULT (0),
    user_status   TEXT    NOT NULL
                          DEFAULT new,
    approve_date  TEXT,
    payment_date  TEXT
);


-- Table: drop_manager
CREATE TABLE IF NOT EXISTS drop_manager (
    drop_manager_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dm_tg_id        INTEGER NOT NULL
                            UNIQUE,
    dm_tg_username  TEXT    NOT NULL,
    invited_users   INTEGER DEFAULT (0) 
                            NOT NULL
);


-- Table: top_manager
CREATE TABLE IF NOT EXISTS top_manager (
    id_top_manager          INTEGER PRIMARY KEY,
    tg_id_top_manager       INTEGER UNIQUE
                                    NOT NULL,
    tg_username_top_manager TEXT    NOT NULL
);


-- Table: webpanel_accounts
CREATE TABLE IF NOT EXISTS webpanel_accounts (
    id_wp_accs       INTEGER PRIMARY KEY AUTOINCREMENT
                             NOT NULL,
    username_wp_accs TEXT    NOT NULL,
    password_wp_accs TEXT    NOT NULL
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
