#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.

This time the script is safe from
MySQL injections!
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """

    conn = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    cur = conn.cursor()

    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY states.id ASC""", {'name': argv[4]})
    query_rows = cur.fetchall()

    for rows in query_rows:
        print(row);

    cur.close()
    conn.close()
