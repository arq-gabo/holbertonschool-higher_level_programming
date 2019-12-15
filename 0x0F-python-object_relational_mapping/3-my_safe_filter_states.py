#!/usr/bin/python3

"""Module"""


import MySQLdb
import sys


if __name__ == "__main__":
    """connection with database"""
    data_base = MySQLdb.connect(user=sys.argv[1],
                                passwd=sys.argv[2],
                                db=sys.argv[3],
                                host='localhost',
                                port=3306)
    myCursor = data_base.cursor()

    myCursor.execute("SELECT * FROM states \
                      WHERE name LIKE BINARY %s\
                      ORDER BY id ASC;", (sys.argv[4]))

    values_db = myCursor.fetchall()

    for val_db in values_db:
        print('{}'.format(val_db))

    myCursor.close()
    data_base.close()
