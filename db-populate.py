import sqlite3

connie = sqlite3.connect('robocupjr.db')
c = connie.cursor()

c.execute("""
INSERT INTO teams123(ID, name_first, name_last, team, category, year) VALUES
('1','Ferris','Bueller', 'Team Bueller', 'Dancing','2020'),
('2','Sloane','Petterson', 'Team Bueller', 'Dancing','2020'),
('3','Cameron ','Frye', 'Team Bueller', 'Dancing','2020'),
('4','Ed','Rooney', 'Glenbrook High', 'Dancing','2019'),
('5','Grace','Wheelburg', 'Glenbrook High', 'Dancing','2019'),
('6','Jeanie','Bueller', 'Glenbrook High', 'Dancing','2019'),

('7','Freddie','Mercury', 'The Kings', 'Dancing','2018'),
('8','Brian',' May', 'The Kings', 'Dancing','2018'),
('9','John','Deacon', 'The Kings', 'Dancing','2018'),
('10','Roger','Taylor', 'The Kings', 'Dancing','2018'),

('11','John','Lennon', 'The Eatles', 'Dancing' ,'2017'),
('12','Paul','McCartney', 'The Eatles', 'Dancing','2017'),
('13','Ringo','Starr', 'The Eatles', 'Dancing','2017'),
('14','George','Harrison', 'The Eatles', 'Dancing','2017'),

('15','Kurt','Cobain', 'Virnana', 'Dancing','2016'),
('16','Dave','Grohl', 'Virnana', 'Dancing','2016'),
('17','Krist','Novoselic', 'Virnana', 'Dancing','2016'),

('18','Bernard','Fanning', 'RockThumb', 'Dancing','2015'),
('19','Ian','Faung', 'RockThumb', 'Dancing','2015'),
('20','Jon','Coghill', 'RockThumb', 'Dancing','2015'),
('21','Darren','Middleton', 'RockThumb', 'Dancing','2015')
""")


connie.commit()
connie.close()
