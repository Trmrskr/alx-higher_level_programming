#!/usr/bin/python3
"""
This script takes in four arguments, user, password, database and a searchtext
It uses python MySQLdb connector to query all values in states which name
matches the searchtext from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    The namespace of the script.
    connect to database using MySQLdb connector.
    use cursor to create a working environment to interface with database
    fetchall rows and print using for loop.
    """

    conn = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                           passwd=argv[2], db=argv[3])

    cur = conn.cursor()
    cur.execute("SELECT * FROM states \
                WHERE name = '{}' \
                ORDER BY states.id ASC".format(argv[4]))
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
