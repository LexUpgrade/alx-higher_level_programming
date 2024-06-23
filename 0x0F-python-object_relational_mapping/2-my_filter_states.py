#!/usr/bin/python3
"""
    Takes in an argument and displays all values in the 'states' table of
    'hbtn_0e_0_usa' where 'name' matches the argument.
"""
from sys import argv as av
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=av[1], passwd=av[2], db=av[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY ('{}')"
                   .format(av[4]))
    states = cursor.fetchall()
    cursor.close()
    db.close()

    for state in states:
        print(state)
