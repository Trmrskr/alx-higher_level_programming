#!/usr/bin/python3
"""
This script uses the python MySQLdb connector to connect to MySQL,
Executes a command that lists all the states from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    The namespace of this script, creates the connection,
    use cursor to create a distinct working environment for connection
    executes an SQL query and print each each row from the SQL queries.
    """
    conn = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                           passwd=argv[2], db=argv[3])

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
