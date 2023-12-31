#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost",
                          port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3])

    cursor = con.cursor()
    cursor.execute(
        """SELECT cities.id, cities.name, states.name FROM cities
                    JOIN states ON state_id=states.id ORDER BY cities.id;""")
    records = cursor.fetchall()
    for row in records:
        print(row)
    cursor.close()
    con.close()
