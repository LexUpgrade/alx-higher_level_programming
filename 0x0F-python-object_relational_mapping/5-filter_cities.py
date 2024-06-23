#!/usr/bin/python3
"""
    Takes in the name of a state as an argument and lists all 'cities' of the
    state, under the database: 'hbtn_0e_4_usa'.
"""
from sys import argv as av
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=av[1], passwd=av[2], db=av[3])
    cur = db.cursor()
    cur.execute("""SELECT c.name FROM cities c
                INNER JOIN states s ON s.id=c.state_id
                WHERE s.name=%s
                """, (av[4], ))
    cities = cur.fetchall()
    cur.close()
    db.close()

    cities_ = [c[0] for c in cities]
    print(", ".join(cities_))
