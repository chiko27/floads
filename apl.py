from flask import Flask, render_template, url_for, request, redirect, make_response
from time import time
from datetime import date, datetime
from random import random
import json
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'floads'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

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

@app.route('/summary', methods=["GET", "POST"])
def summary():
    if request.method == 'POST':
        amount = request.values.get('amount')
        species = request.values.get('species')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO jumlah (spesies, Total) VALUES (%s,%s)",
                    (species, amount))
        mysql.connection.commit()
        cur.close()
        return 'Data 2 sudah masuk ke database'
    elif request.method == 'GET':
        return "belom dibuat"

if __name__ == '__main__':
    app.run()
