from flask import Flask, render_template, url_for, request, redirect, make_response, session
from time import time
from datetime import date, datetime
from random import random
import json
from flask_mysqldb import MySQL

STATIC_FOLDER='/'
app = Flask(__name__, static_folder=STATIC_FOLDER)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'floads'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('login.html')

@app.route('/register', methods=["GET", "POST"])
def regis():
    if request.method =='GET':
        return render_template('regis.html')
    else :
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO user(name, email, password) values (%s,%s,%s)", (name, email, password,)
        )
        mysql.connection.commit()
        session['name'] = name
        session['email'] = email
        return redirect(url_for('main'))

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM user where email=%s", (email,)
        )
        user =cur.fetchone()
        cur.close()

        if len(user)>0:
            if password == user['password']:
                session['name'] = user['name']
                session['email'] = user ['email']
                return redirect(url_for('home'))
        else:
            return 'Error password or user does not match'
    else :
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return render_template('login.html')

@app.route ('/about')
def about():
    return render_template('about.html')

@app.route ('/data')
def datapage():
    return render_template('data.html')
# --------------- DATABASE ---------------
@app.route('/database', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        # mengambil nilai yg dikirimkan
        weight = request.values.get('weight')
        species = request.values.get('species')
        tgl = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO spesies_ikan (tglJam, berat, spesies) VALUES (%s,%s,%s)",
            (tgl, weight, species))
        mysql.connection.commit()
        cur.close()
        return 'Data sudah masuk ke database'
    elif request.method == 'GET':
        return "belom dibuat"

# --------------- DATABASE END ---------------


if __name__ == '__main__':
    app.run(debug="True")
