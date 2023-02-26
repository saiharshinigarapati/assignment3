import redis
import hashlib
import pickle
import time
from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)
@app.route('/')
def index():
   return render_template('index.html')
@app.route('/random')
def rando():
    return render_template('random.html')
@app.route('/specified')
def soe():
    return render_template('specified.html')
@app.route('/task')
def tak():
    return render_template('task.html')
@app.route('/all', methods=['POST','GET'])
def fulllist():
    conn = sqlite3.connect('all_month.db')
    cur = conn.cursor()
    querry="Select * from all_month "
    cur.execute(querry)
    rows = cur.fetchall()
    conn.close()
    return render_template("list.html",rows = rows)
@app.route('/random',methods=['POST','GET'])
def  random():
    conn=sqlite3.connect('all_month.db')
    cur=conn.cursor()
    querry="select * FROM all_month ORDER BY RANDOM() LIMIT 1000 "
    cur.execute(querry)
    rows=cur.fetchall()
    conn.close()
    return render_template("list.html",rows=rows)
@app.route('/res',methods=['POST','GET'])
def res():
    conn=sqlite3.connect('all_month.db')
    cur=conn.cursor()
    N=str(request.form['N'])
    querry="select time,latitude,longitude,mag from all_month  order by RANDOM() LIMIT '"+N+"' "
    cur.execute(querry) 
    rows=cur.fetchall()
    conn.close()
    return render_template("specified.html",rows=rows)
    
if __name__ == '__main__':
    app.debug=True
    app.run()
