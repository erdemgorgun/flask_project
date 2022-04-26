import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('customer 1', 'Port: 23   Vlan Id: 56   IPv6 Address/Prefix Length: fe80::224:97ff:fe69:69af/64')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('customer 1', 'Port: 23   Vlan Id: 56   IPv6 Address/Prefix Length: 2001:9:10:56::60/64')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('another customer', 'Port:42 Vlan Id: N/A IPv6 Address/Prefix Length: fe80::224:97ff:fe69:69a1/64')
            )

connection.commit()
connection.close()
