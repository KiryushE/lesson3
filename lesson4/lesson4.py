import sqlite3

sqlite_connection = sqlite3.connect("test_database.db")
cursor = sqlite_connection.cursor()
cursor.execute("""
""")
sqlite_connection.close()

with sqlite3.connect("test_database.db") as sqlite_connection:
    cursor = sqlite_connection.cursor()
    # cursor.execute("""CREATE TABLE School (
    # name TEXT,
    # surname TEXT,
    # class INTEGER,
    # city TEXT
    # )""")
    # cursor.execute("""INSERT INTO School VALUES('Artem', 'qwer', 10, 'Lviv')""")
    # cursor.execute("""UPDATE School SET class = 11 WHERE class = 10 """)
    # result = cursor.fetchall()
    # for i in result:
    #     print(i)