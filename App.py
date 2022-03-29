import os
import webbrowser


from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from tqdm import tqdm
from time import sleep

# initializations
app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flaskcrud'
mysql = MySQL(app)

# settings
app.secret_key = "mysecretkey"

# routes
@app.route('/')
def Index():
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
if __name__ == "__main__":
    webbrowser.open("localhost:3000", new=2, autoraise=True)
    app.run(port=3000, debug=True)

