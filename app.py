import os
from flask import Flask, request, redirect, Response, json, render_template, url_for, make_response
from flask_mysqldb import MySQL
from datetime import date, datetime
from time import time
from random import random
import json

STATIC_FOLDER='/'
app = Flask(__name__, static_folder=STATIC_FOLDER)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='inkel2020'
mysql=MySQL(app)

@app.route("/")
def index():
    #untuk menampilkan template gunakan render_template
    return render_template("index.html")

@app.route("/data")
def data():
    #untuk menampilkan template gunakan render_template
    return render_template("data.html")

@app.route("/about")
def about():
    #untuk menampilkan template gunakan render_template
    return render_template("instrumen.html") 

@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('login.html')

@app.route('/sensor1', methods=['GET','POST'])
def sensor1():
    if request.method == 'POST':
        suhu=request.values.get('sensor1')
        salinitas=request.values.get('sensor2')
        tss=request.values.get('sensor3') 
        disox=request.values.get('sensor4') 
        tgl=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur=mysql.connection.cursor()
        cur.execute(
            "INSERT INTO sensor1(tgljam, suhu, salinitas, TSS, DO) VALUES(%s, %s, %s, %s, %s)", (tgl, suhu, salinitas, tss, disox)) 
        mysql.connection.commit()
        cur.close()
        return 'Data Masuk' 
    elif request.method == 'GET':
        return 'Ini akses GET'

@app.route('/datasens', methods=["GET", "POST"])
def data__():
    cur = mysql.connection.cursor()
    resultValue = cur.execute(
        "SELECT * FROM sensor1 order by Id desc limit 3")
    if resultValue > 0:
        datasensor = cur.fetchall()
        suhu = datasensor[0][2]
        salinitas = datasensor[0][3]
        tss = datasensor[0][4]
        do = datasensor[0][5]
        data = [time() * 1000, suhu, salinitas, tss, do]
        response = make_response(json.dumps(data))
        response.content_type = "application/json"
    else:
        suhu = 0
        salinitas = 0
        tss = 0
        do = 0
        data = [time() * 1000, suhu, salinitas, tss, do]
        response = make_response(json.dumps(data))
        response.content_type = "application/json"
    return response


@app.route('/datasens', methods=['GET', 'POST'])
def sensor1_():
    if request.method == 'POST':
        suhu = request.values.get('sensor1')
        salinitas = request.values.get('sensor2')
        tss = request.values.get('sensor3')
        do = request.values.get('sensor4')
        tgl = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO sensor1(tgljam, suhu, salinitas, TSS, DO) VALUES (%s,%s, %s, %s)", (tgl, suhu, salinitas, tss, do))
        mysql.connection.commit()
        cur.close()
        return redirect('/')
    elif request.method == 'GET':
        cur = mysql.connection.cursor()
        resultValue = cur.execute(
            "SELECT * FROM sensor1 order by Id desc limit 20")
        if resultValue > 0:
            datasensor = cur.fetchall()
        return render_template('index.html', data=datasensor)

if __name__ == "__main__":
    app.run()