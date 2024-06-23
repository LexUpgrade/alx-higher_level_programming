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
    cur.execute("""SELECT c.name FROM states s
                JOIN cities c ON s.id LIKE c.state_id
                WHERE c.state_id LIKE
                (SELECT states.id FROM states WHERE name LIKE %s)
                ORDER BY c.id
                """, (av[4], ))
    cities = cur.fetchall()
    cur.close()
    db.close()

    for i, city in enumerate(cities):
        print(city[0], end="")
        if i != len(cities) - 1:
            print(", ", end="")
