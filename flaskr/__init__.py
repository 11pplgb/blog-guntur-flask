
import os

from cs50 import SQL
from flask import import Flask,flask,jsonify,redirect,render_template,request,session

#import apk flask untuk di pakai di web kita
from flask import Flask
#mangatur nama apk
app = Flask(__name__)

#mengatur URIdan apa yang ditampilkan di URI tersebut di akses
@app.route('/')#ketika URI dipangil maka akan menjalankan fungsi hello
def hello():#function
    return 'Hello,Wold!'

@app.route('/login')
def login():
    return 'halaman login'