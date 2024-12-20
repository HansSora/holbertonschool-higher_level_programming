#!/usr/bin/python3
"""SQL learning"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    """SQL Learning"""

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    curr = db.cursor()

    s = """SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id"""

    curr.execute(s, (argv[4],))

    rows = curr.fetchall()

    for row in range(len(rows)):
        print(rows[row])

    curr.close()
    db.close()
