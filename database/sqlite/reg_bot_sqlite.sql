--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: drop_accs
CREATE TABLE IF NOT EXISTS drop_accs (
    id_drop_accs  INTEGER PRIMARY KEY AUTOINCREMENT,
    tg_id         INTEGER UNIQUE
                          NOT NULL,
    tg_username   TEXT    NOT NULL,
    full_name     TEXT,
    country       TEXT,
    region        TEXT,
    city          TEXT,
    address       TEXT,
    date_of_birth TEXT,
    document_id   TEXT,
    phone_number  TEXT,
    referral_id   INTEGER,
    language      TEXT    NOT NULL
                          DEFAULT en,
    verified      INTEGER NOT NULL
                          DEFAULT (0),
    user_status   TEXT    NOT NULL
                          DEFAULT new
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


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
