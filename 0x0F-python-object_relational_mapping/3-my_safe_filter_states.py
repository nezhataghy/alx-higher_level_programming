#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states table
 of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost",
                          port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3])

    cursor = con.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id;".format(argv[4]))
    records = cursor.fetchall()
    for row in records:
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    con.close()
