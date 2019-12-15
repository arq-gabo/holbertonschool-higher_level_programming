#!/usr/bin/python3

"""Module"""

import MySQLdb

data_base = MySQLdb.connect(host='localhost',
                            user='root',
                            passwd='1234',
                            db='hbtn_0e_0_usa')

myCursor = data_base.cursor()

myCursor.execute("SELECT * FROM hbtn_0e_0_usa.states ORDER BY id ASC")

valuesDb = myCursor.fetchall()

for val_db in valuesDb:
    print(val_db)

data_base.commit()

data_base.close()
