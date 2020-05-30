from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
import sqlite3

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

# ---------------------------------LOGIN SETUP------------------------------------------

db = SQLAlchemy(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# set the type and location of the DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///robocupjr.db'
# make sure this key stays secret
app.config['SECRET_KEY'] = 'key'


# class name has to match the table name
# class variables must match the column names of the table
# one column must be called 'id'
class judges(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)


# should be set to refer to the class name as above
@login_manager.user_loader
def load_user(id):
    return judges.query.get(id)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/criteria')
def criteria_page():
    return render_template('criteria.html')


@app.route('/dancing')
def dancing_page():
    dance_results = dancing_table()
    print(dance_results)
    return render_template('dancing.html', product=dance_results)


def dancing_table():
    connie = sqlite3.connect('robocupjr.db')
    c = connie.cursor()
    c.execute("SELECT * FROM dancingscores")
    return (c.fetchall())


# --------TESTING INDIV DETAILS--------------------------------------------
@app.route('/search/<id>/')
def search_id(id):
    name_first, name_last, team, category, year = details(id)
    return render_template('search.html', name_first=name_first, name_last=name_last,
                           team=team, category=category, year=year)


# ------ Placehodler for future searching function
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        id = request.form['ID']
        return redirect(url_for('search_id', id=id))
    else:
        return render_template('id_search.html')


def details(id):
    connie = sqlite3.connect('robocupjr.db')
    c = connie.cursor()
    c.execute("SELECT name_first, name_last, team, category, year  FROM teams123 WHERE ID = ?", (id,))
    name_first, name_last, team, category, year = c.fetchone()
    return (name_first, name_last, team, category, year)


# --------------- End Ranking Page---------------
@app.route('/teams')
def teams_page():
    teams_results = teams_page_table()
    print(teams_results)
    return render_template('teams.html', output=teams_results)



def teams_page_table():
    connie = sqlite3.connect('robocupjr.db')
    c = connie.cursor()
    c.execute("SELECT * FROM teams123")
    return (c.fetchall())


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'GET':
        return render_template('Login.html')
    else:
        try:
            my_judge = judges.query.filter_by(username=request.form['username']).first()
        except:
            return redirect(url_for('login_page'))

    if my_judge is not None:
        if my_judge.password == request.form['password']:
            login_user(my_judge)
            return render_template('admin.html')
        else:
            flash('An error occured. Please check Username and Password ')
            return redirect(url_for('login_page'))
    else:
        flash('An error occured. Please check Username and Password ')
        return redirect(url_for('login_page'))


@app.route('/logout')
@login_required
def log_me_out():
    logout_user()
    return render_template('logout.html')



@app.route('/register')
def register_page():
    return render_template('register.html')


@app.route('/admin')
def admin_page():
    if current_user.is_authenticated:
        return render_template('admin.html')
    else:
        return render_template('login.html')

#
# @app.route('/admin/scoring/<scrid>')
# def scoring_page(scrid):
#     scr_list = scr_lister()
#     return render_template('score.html')
@app.route('/admin/delete_success', methods = ['GET', 'POST'])
def character_delete_success():
    if request.method == 'POST':
        id = request.form['id']
        team_delete(id)
        return render_template('character_delete_success.html')
    else:
        return render_template ('admin.html')

@app.route('/admin/delete')
def admin_delete():
    id, team, score = query_profile_full(6)
    return render_template('character_delete.html',
                           id=id,
                           team=team,
                           score=score
                           )


def query_profile_full(id):
    connie = sqlite3.connect('robocupjr.db')
    c = connie.cursor()
    c.execute("SELECT id, team, score FROM dancingscores WHERE ID = ?", (id,))
    id, team, score = c.fetchone()
    return (id, team, score)

def team_delete(id):
    connie = sqlite3.connect('robocupjr.db')
    c = connie.cursor()
    c.execute("DELETE FROM dancingscores WHERE id =?",(id,))





@app.route('/register/team_add', methods=['GET', 'POST'])
def team_add():
    if request.method == 'POST':
        first_name = request.form['first_name']
        surname = request.form['surname']
        team_name = request.form['team_name']
        category = request.form['category']
        new_team_details = (first_name, surname, team_name, category)
        update_team_add(new_team_details)
        return redirect(url_for('register_page'))
    else:
        return render_template('register.html')


def update_team_add(new_team_details):
    sql_add_chr = """INSERT INTO teams123 (name_first, name_last, team, category) 
    VALUES (?,?,?,?)"""
    connie = sqlite3.connect('robocupjr.db')
    c = connie.cursor()
    c.execute(sql_add_chr, new_team_details)
    connie.commit()


# ---------------Ranking Page---------------
@app.route('/rankings')
def rankings_page():
    rankings_results = rankings_table()
    return render_template('rankings.html', rank=rankings_results)


def rankings_table():
    connie = sqlite3.connect('robocupjr.db')
    c = connie.cursor()
    c.execute("SELECT * FROM teams123")
    return (c.fetchall())


# -----------------------
# -------2020 Ranking----------------------------
@app.route('/rankings/2020')
def rankings2020():
    rankings_results = rankings_2020()
    return render_template('rankings.html', rank=rankings_results)


def rankings_2020():
    connie = sqlite3.connect('robocupjr.db')
    c = connie.cursor()
    c.execute("SELECT * FROM teams123 WHERE year = 2020")
    twenty_data = c.fetchall()
    return (twenty_data)


# -----------------------------------------------
# -------2019 Ranking----------------------------
@app.route('/rankings/2019')
def rankings2019():
    rankings_results = rankings_2019()
    return render_template('rankings.html', rank=rankings_results)


def rankings_2019():
    connie = sqlite3.connect('robocupjr.db')
    c = connie.cursor()
    c.execute("SELECT * FROM teams123 WHERE year = 2019")
    nineteen_data = c.fetchall()
    return (nineteen_data)


# -----------------------------------------------
@app.route('/rankings/2018')
def rankings2018():
    rankings_results = rankings_2018()
    return render_template('rankings.html', rank=rankings_results)


def rankings_2018():
    connie = sqlite3.connect('robocupjr.db')
    c = connie.cursor()
    c.execute("SELECT * FROM teams123 WHERE year = 2018")
    eighteen_data = c.fetchall()
    return (eighteen_data)


# -----------------------------------------------
# -------2017 Ranking----------------------------
@app.route('/rankings/2017')
def rankings2017():
    rankings_results = rankings_2017()
    return render_template('rankings.html', rank=rankings_results)


def rankings_2017():
    connie = sqlite3.connect('robocupjr.db')
    c = connie.cursor()
    c.execute("SELECT * FROM teams123 WHERE year = 2017")
    seventeen_data = c.fetchall()
    return (seventeen_data)


# -----------------------------------------------
# -------2016 Ranking----------------------------
@app.route('/rankings/2016')
def rankings2016():
    rankings_results = rankings_2016()
    return render_template('rankings.html', rank=rankings_results)


def rankings_2016():
    connie = sqlite3.connect('robocupjr.db')
    c = connie.cursor()
    c.execute("SELECT * FROM teams123 WHERE year = 2016")
    sixteen_data = c.fetchall()
    return (sixteen_data)


# -----------------------------------------------
# -------2015 Ranking----------------------------
@app.route('/rankings/2015')
def rankings2015():
    rankings_results = rankings_2015()
    return render_template('rankings.html', rank=rankings_results)


def rankings_2015():
    connie = sqlite3.connect('robocupjr.db')
    c = connie.cursor()
    c.execute("SELECT * FROM teams123 WHERE year = 2015")
    fifteen_data = c.fetchall()
    return (fifteen_data)


if __name__ == '__main__':
    app.run()
