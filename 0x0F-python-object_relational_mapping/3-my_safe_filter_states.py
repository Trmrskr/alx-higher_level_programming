#!/usr/bin/python3
"""
A modification of 2-my_filter_states.py,

This time the script is safe from
MySQL injections!
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Uses Python's MySQLdb to get the states
    from the database.
    """

    conn = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                           passwd=argv[2], db=argv[3])

    with conn.cursor() as cur:
        cur.execute("""
            SELECT
                *
            FROM
                states
            WHERE
                name LIKE BINARY %(name)s
            ORDER BY
                states.id ASC
        """, {
            'name': argv[4]
        })

        rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
