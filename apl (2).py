from flask import Flask, render_template, url_for, request, redirect, make_response, session
from time import time
from datetime import datetime, date
import json
from flask_mysqldb import MySQL

STATIC_FOLDER='/'
app = Flask(__name__, static_folder=STATIC_FOLDER)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'floads'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('home.html')

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
            "INSERT INTO account(name, email, password) values (%s,%s,%s)", (name, email, password,)
        )
        mysql.connection.commit()
        session['name'] = name
        session['email'] = email
        return render_template('login(2).html')

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM account where email=%s", (email,)
        )
        account =cur.fetchone()
        cur.close()

        if len(account)>0:
            if password == account['password']:
                session['name'] = account['name']
                session['email'] = account ['email']
                return redirect(url_for('user'))
        else:
            return 'Error password or account does not match'
    else :
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return render_template('home.html')

@app.route ('/about')
def about():
    return render_template('about.html')

@app.route ('/about2')
def about2():
    return render_template('about2.html')

@app.route ('/user')
def user():
    return render_template('index.html')

@app.route ('/data')
def datapage():
    return render_template('data.html')

# --------------- DATABASE ---------------
@app.route('/database', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        # mengambil nilai yg dikirimkan
        berat = request.values.get('berat')
        tgl = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO tangkapan_tongkol(tglJam, berat) VALUES (%s,%s)",
            (tgl, berat))
        mysql.connection.commit()
        cur.close()
        return 'Data sudah masuk ke database'
    elif request.method == 'GET':
        return "NONE"

@app.route('/database1', methods=['GET', 'POST'])
def data1():
    if request.method == 'POST':
        # mengambil nilai yg dikirimkan
        weight = request.values.get('berat')
        tgl = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO tangkapan_cakalang(tglJam, berat) VALUES (%s,%s)",
            (tgl, weight))
        mysql.connection.commit()
        cur.close()
        return 'Data sudah masuk ke database'
    elif request.method == 'GET':
        return "NONE"

@app.route('/data2', methods=["GET", "POST"])
def data2():
    # Data Format
    cur = mysql.connection.cursor()
    resultValue = cur.execute(
        "SELECT * FROM tangkapan_tongkol order by no desc limit 1")
    if resultValue > 0:
        datasensor = cur.fetchall()
        berat = datasensor[0][2]
        data = [time() * 1000, berat]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
    else:
        berat = 0
        data = [time() * 1000, berat]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
    return response

@app.route('/data3', methods=["GET", "POST"])
def data3():
    # Data Format
    cur = mysql.connection.cursor()
    resultValue = cur.execute(
        "SELECT * FROM tangkapan_cakalang order by no desc limit 1")
    if resultValue > 0:
        datasensor = cur.fetchall()
        berat = datasensor[0][2]
        data = [time() * 1000, berat]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
    else:
        berat = 0
        data = [time() * 1000, berat]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
    return response

# --------------- DATABASE END ---------------


if __name__ == '__main__':
    app.secret_key = "diklatmitr11"
    app.run(debug="True")
