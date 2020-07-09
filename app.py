from flask import Flask, render_template, request, url_for, redirect
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)

