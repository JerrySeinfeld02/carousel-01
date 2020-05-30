import sqlite3
connie =sqlite3.connect('robocupjr.db')
c = connie.cursor()

c.execute("""
CREATE TABLE dancingscores(
id  INTEGER VARCHAR(3) PRIMARY KEY,
team TEXT,
score INTEGER
)
""")

connie.commit()
connie.close()