import sqlite3

def indiv_details():
    #name_first, name_last, team, category, year = details()
    details_record = details()
        #'rankings.html', name_first=name_first, name_last=name_last, team=team, category=category, year=year)

def details():
    connie =sqlite3.connect('rcj.db')
    c = connie.cursor()
    c.execute("SELECT name_first, name_last, team, category, year FROM users123 WHERE ID = '1'")
    return( c.fetchall())
def select_all():
    connie = sqlite3.connect('robocupjr.db')
    c = connie.cursor()
    c.execute("SELECT * FROM judges")
    return (c.fetchall())
output = select_all()

for item in output:
    print(item)