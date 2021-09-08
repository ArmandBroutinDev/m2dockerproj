from flask import Flask
from flask import escape
from flask import render_template
import requests


app = Flask(__name__)

@app.route("/")
def welcome():
    phrase = requests.get('http://127.0.0.1:3305/')
    return render_template('welcome.html',phrase=phrase)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')  

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=3306)