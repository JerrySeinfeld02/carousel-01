import sqlite3
connie =sqlite3.connect('robocupjr.db')
c = connie.cursor()

c.execute("""
INSERT INTO judges VALUES
('1', 'judyj', '44m'),
('2', 'busha', 'tkinter'),
('3', 'macleodC', 'immortal'),
('4', 'septimt', 'talos'),
('5', 'rcj', 'password')
""")

connie.commit()
connie.close()