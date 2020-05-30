import sqlite3
connie =sqlite3.connect('robocupjr.db')
c = connie.cursor()

c.execute("""
CREATE TABLE judges(
id VARCHAR(3) PRIMARY KEY,
username TEXT,
password TEXT
)
""")

connie.commit()
connie.close()
