#!/usr/bin/python3
"""
This is a python script using MySQLdb connector to
lists all states with a `name` starting with the letter `N`
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    The name space of this script connects to the database,
    Create a working environment to interface with the database
    """
    conn = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                           passwd=argv[2], db=argv[3])

    cur = conn.cursor()
    cur.execute("SELECT * FROM states \
                 WHERE states.name LIKE /^N\w*$/ \
                 ORDER BY states.id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
