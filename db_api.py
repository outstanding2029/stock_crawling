import datetime
import sqlite3 as sql

DB_NAME = 'history.db'

today = 'table_' + datetime.datetime.now().strftime('%Y%m%d')

def initialize():
    try:
        conn = sql.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS %s (code text PRIMARY KEY, message text)" % today)
        conn.commit()
        return conn;
    except Exception as e:
        print('Exception from db_api - initialize : ' + e)
    return None;

def finailize():
    db.close();

def insert(code, message):
    try:
        cursor = db.cursor()
        cursor.execute("INSERT INTO %s (code, message) VALUES (?, ?)" % today, (code, message))
        db.commit()
    except Exception as e:
        print('Exception from db_api - insert : ' + e)
        if db:
            db.rollback()

def is_exist(code):
    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM %s WHERE code=:code" % today, {"code":code})
        row = cursor.fetchone()
        if row != None:
            return 'true'
        else:
            return None
    except Exception as e:
        print ('Exception from db_api - is_exist : ' + e)
    return None;

db = initialize()
