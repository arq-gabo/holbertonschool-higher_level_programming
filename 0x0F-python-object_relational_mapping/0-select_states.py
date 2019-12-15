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

    myCursor.execute("SELECT * FROM hbtn_0e_0_usa.states ORDER BY id ASC")

    valuesDb = myCursor.fetchall()

    for val_db in valuesDb:
        print(val_db)

    myCursor.close()
    data_base.close()
