import os
import json
import webbrowser

from tracemalloc import stop
from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_mysqldb import MySQL
#from tqdm import tqdm
#from time import sleep

# Probando Varaibles de Entorno
from dotenv import load_dotenv
load_dotenv()
title = os.getenv('TITLE')
print('Titulo = '+ title)

# Get data for connection DB
with open('config/db.json') as file:
    data = json.load(file)

# initializations
webbrowser.open("http://127.0.0.1:3000", autoraise=True)
app = Flask(__name__)

# Mysql Connection

# # Name Host
# app.config['MYSQL_HOST'] = data['host']
# #Name User_Mysql
# app.config['MYSQL_USER'] = data['user']
# # Name Password_Mysql
# app.config['MYSQL_PASSWORD'] = data['password']
# # Name DB
# app.config['MYSQL_DB'] = data['dbase']

# # Initial Mysql
# mysql = MySQL(app)

# settings
app.secret_key = "mysecretkey"

# routes
@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/cerrar')
def cerrar():
    #ver como detener el server 
    return render_template('index.html')

@app.route('/convertir', methods=['POST'])
def convertir():
    op1 = 'off'
    op2 = 'off'
    if request.method == 'POST':
        link = request.form['link']

        if request.form.get('mp4'):
            op1 = request.form['mp4']
        if request.form.get('mp3'):
            op2 = request.form['mp3']

        if op1 == 'on':
            proceso = "youtube-dl --format mp4 "+ link
        else:
            if op2 == 'on':
                proceso = "youtube-dl -x --audio-format mp3 "+ link

        os.system(proceso)
        
        flash('Proceso Completado ....')
        return redirect(url_for('Index'))

# starting the app
def init():
    if __name__ == "__main__":    
        app.run(port=3000, debug=True)
        
init()
