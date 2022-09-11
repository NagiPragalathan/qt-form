import sqlite3

conn = sqlite3.connect('test.sqlite')


def create_table():
    print("Opened database successfully")

    conn.execute('''CREATE TABLE COMPANY
             (ID integer auto_increment primary key unique,
             NAME           TEXT    NOT NULL,
             EMAIL           TEXT  UNIQUE  NOT NULL,
             PASS           TEXT    NOT NULL,
             ORG            TEXT     ,
             ACTIVE BOOL DEFAULT FALSE,
             TYPE INT NOT NULL DEFAULT 1,
             CREATED_DATE DATETIME DEFAULT CURRENT_TIMESTAMP );''')
    conn.execute('''CREATE TABLE USER_LOG
             (ID integer auto_increment primary key unique,
             USR_NAME    TEXT    NOT NULL,
             LAST_LOGIN DATETIME DEFAULT CURRENT_TIMESTAMP );''')
    
    
    print("Table created successfully")

create_table()