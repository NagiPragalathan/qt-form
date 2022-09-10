import sqlite3

conn = sqlite3.connect('test.sqlite')


def create_table():
    print("Opened database successfully")

    conn.execute('''CREATE TABLE COMPANY
             (ID integer auto_increment primary key unique,
             NAME           TEXT    NOT NULL,
             EMAIL           TEXT  UNIQUE  NOT NULL,
             PASS           TEXT    NOT NULL,
             ORG            TEXT     NOT NULL);''')
    print("Table created successfully")

create_table()