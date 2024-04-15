#!/usr/bin/python3
""" this lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

def select_states(username, password, db_name):
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cursor = db.cursor()
    sql = "SELECT * FROM states ORDER BY states.id"

    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()

if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    select_states(username, password, db_name)
