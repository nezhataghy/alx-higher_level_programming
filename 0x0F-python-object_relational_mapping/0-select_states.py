#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost",
                        port=3306, user=argv[1],
                        passwd=argv[2], db=argv[3])
    
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id;")
    records = cursor.fetchall()
    for row in records:
        print(row)
    cursor.close()
    con.close()
