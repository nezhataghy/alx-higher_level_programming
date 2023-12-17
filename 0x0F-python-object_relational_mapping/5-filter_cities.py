#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all cities
 of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost",
                          port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3])

    cursor = con.cursor()
    cursor.execute(
        """SELECT cities.name FROM cities JOIN states ON state_id=states.id
                    WHERE states.name = %s ORDER BY cities.id;""", (argv[4],))
    records = cursor.fetchall()
    print(", ".join(row[0] for row in records))
    cursor.close()
    con.close()
