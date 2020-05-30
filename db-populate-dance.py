import sqlite3

connie = sqlite3.connect('robocupjr.db')
c = connie.cursor()

c.execute("""
INSERT INTO dancingscores VALUES
('1', 'Team Bueller', '0'),
 ('2', 'The Kings', '0'),
 ('3', 'The Eatles', '0'),
 ('4', 'Virnana', '0'),
 ('5', 'RockThumb', '0'),
 ('6', 'test1', '0'),
 ('7', 'test2', '0'),
 ('8', 'test3', '0')
""")

connie.commit()
connie.close()
