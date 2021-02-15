# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json, sqlite3


app = Flask(__name__)


conn = sqlite3.connect("mapsbd.db", check_same_thread=False)
cursor = conn.cursor()
data = ''

category_data = {}
alldata = {}

# === Код в котором заполняются словари ===

cursor.execute("SELECT * FROM good_requests")
allFiles = cursor.fetchall()
category_data = {}
alldata = {}
data = []

for i in range(len(allFiles)):   
    category_data[allFiles[i][1]] = allFiles[i][2]

    if allFiles[i][1] in alldata:
        data.append(alldata[allFiles[i][1]])
        data[0].append([allFiles[i][3], allFiles[i][4]])
        alldata[allFiles[i][1]] = data[0]
        data = []
    else:
        alldata[allFiles[i][1]] = [[allFiles[i][3], allFiles[i][4]]]
        
# === конец ===

@app.route('/')
@app.route('/home')
def home():

            
    return render_template('home.html', category=json.dumps(category_data), alldata = json.dumps(alldata))

@app.route('/about-us')
def about_us():
    return render_template('about_us.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/<ctg>')
def category(ctg):
    one_category = {}
    if(ctg == 'coronavirus'):
        one_category = 'coronavirus'
    else:
        for key in category_data:
            ctgdata = category_data[key].replace(' ', '-').lower()
            if(ctgdata == ctg):
                 key_copy = key
        one_category[key_copy] = category_data[key_copy]
            
    return render_template('home.html', category=json.dumps(one_category), alldata = json.dumps(alldata))

@app.route('/home/category/<ctg>/<indicator>')
def category_and_indicator(ctg, indicator):
    n = 0
    for key in category_data:
        ctgdata = category_data[key].replace(' ', '-').lower()
        if(ctg == ctgdata or ctg == 'covid-19'):
             n += 1
    if(n>0):
        ctg_and_indicator = [ctg, indicator]
                
    
            
    return render_template('home.html', category=json.dumps(category_data), alldata = json.dumps(alldata), ctg_and_indicator=ctg_and_indicator)





