import os
import sqlite3
import logging

#Configuration of the logger
logging.basicConfig(level=logging.ERROR, format="%(name)s %(asctime)s - [%(levelname)s] - %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")


# Set SQLite db files location
FILENAME = os.path.abspath(__file__)
DBDIR = FILENAME.rstrip('code\\filename.py')
DBPATH = os.path.join(DBDIR, "database", "database.db")
logging.info(f"Path to the db : {DBPATH}")

# Connect to DB
def create_connection(db_path = DBPATH):
    con = None
    try:
        con = sqlite3.connect(db_path)
    except Exception as e:
        logging.exception("An exception occured.")
        raise    
    cur = con.cursor()
    return cur

# Create the record table
def create_table(cur):
    try: 
        cur.execute("CREATE TABLE IF NOT EXISTS recorder(id INTEGER PRIMARY KEY AUTOINCREMENT, pointing_date DATETIME NOT NULL, value TEXT CHECK(value IN ('IN','OUT')) NOT NULL)")
        logging.info('recorder has been created.')
    except Exception as e:
        logging.exception("An exception occured.")
        raise
    
# Insert into the table a record
def insert_record(cur, record_value):
    try: 
        cur.execute(f"INSERT INTO recorder (id, pointing_date, value) VALUES (NULL, DATETIME(), '{record_value}')")
        logging.info('A record has been successfully added.')
    except Exception as e:
        logging.exception("An exception occured.")
        raise
    
def daily_countdown():
    pass

if __name__ == "__main__":
    
    cur = create_connection()
    insert_record(cur, "IN")
    create_table(cur)