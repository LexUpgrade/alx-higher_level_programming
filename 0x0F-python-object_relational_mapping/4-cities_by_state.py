#!/usr/bin/python3
"""Lists all 'cities' from the database 'hbtn_0e_4_usa'."""
from sys import argv as av
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=av[1], passwd=av[2], db=av[3])
    cur = db.cursor()
    cur.execute("""SELECT c.id, c.name, s.name
                FROM states s
                JOIN cities c ON s.id LIKE c.state_id
                ORDER BY c.id
                """)
    cities_by_states = cur.fetchall()
    cur.close()
    db.close()

    for c_s in cities_by_states:
        print(c_s)
