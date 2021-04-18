from flask import render_template, request
from app import app

@app.route('/')
def index():
    render_template('index.html', title='Home')

