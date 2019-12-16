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

    myCursor.execute("SELECT cities.name\
                      FROM cities WHERE cities.state_id = ANY\
                      (SELECT id FROM states\
                      WHERE name = '{}')".format(sys.argv[4]))

    values_db = myCursor.fetchall()

    for i in range(len(values_db)):
        if i == len(values_db) - 1:
            print(values_db[i][0])
        else:
            print('{}, '.format(values_db[i][0]), end='')

    myCursor.close()
    data_base.close()