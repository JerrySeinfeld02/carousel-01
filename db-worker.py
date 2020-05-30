import sqlite3

connie = sqlite3.connect('robocupjr.db')
c = connie.cursor()
c.execute("DELETE FROM dancingscores WHERE id = 6")

connie.commit()
connie.close()



