import sqlite3

connie = sqlite3.connect('robocupjr.db')
c = connie.cursor()

c.execute("""
CREATE TABLE scores123(
ID INTEGER PRIMARY KEY AUTOINCREMENT ,
team text,
score text
)
""")
connie.commit()
connie.close()
