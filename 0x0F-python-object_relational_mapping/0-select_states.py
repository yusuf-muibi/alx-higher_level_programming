#!/usr/bin/python3
""" This lists all states from the database hbtn_0e_0_usa """
import sys
import MySQLdb

def select_states(username, password, db_name):
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cursor = db.cursor()
    sql = "SELECT * FROM states ORDER BY id ASC"
    
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except MySQLdb.Error as e:
        print("Error: unable to fetch data")
        print(e)
    finally:
        cursor.close()
        db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
        
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    select_states(username, password, db_name)
