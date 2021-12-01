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
            "INSERT INTO account(name, email, password) values (%s,%s,%s)", (name, email, password,)
        )
        mysql.connection.commit()
        session['name'] = name
        session['email'] = email
<<<<<<< HEAD
        return redirect(url_for('login'))
=======
        return render_template('login(2).html')
>>>>>>> 54858b40fa9ab81e21cccddb199b3c1c56568f58

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
                return redirect(url_for('index'))
        else:
            return 'Error password or account does not match'
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
        berat = request.values.get('berat')
        spesies = request.values.get('spesies')
        lokasi = request.values.get('lokasi')
        id_nelayan = request.values.get('id_nelayan')
        id_kapal = request.values.get('id_kapal')
        tgl = date.today()
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO hasil_tangkapan (tglJam, id_kapal, id_nelayan, lokasi, spesies, berat) VALUES (%s,%s,%s,%s,%s,%s)",
            (tgl, id_kapal, id_nelayan, lokasi, spesies, berat))
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
        "SELECT * FROM hasil_tangkapan order by no desc limit 1")
    if resultValue > 0:
        datasensor = cur.fetchall()
        id_kapal = datasensor[0][2]
        id_nelayan = datasensor[0][3]
        lokasi = datasensor[0][4]
        spesies = datasensor[0][5]
        berat = datasensor[0][6]
        data = [time() * 1000, id_kapal, id_nelayan, lokasi, spesies, berat]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
    else:
        id_kapal = 0
        id_nelayan = 0
        lokasi = 0
        spesies = 0
        berat = 0
        data = [time() * 1000, id_kapal, id_nelayan, lokasi, spesies, berat]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
    return response

# --------------- DATABASE END ---------------


if __name__ == '__main__':
    app.secret_key = "diklatmitr11"
    app.run(debug="True")
