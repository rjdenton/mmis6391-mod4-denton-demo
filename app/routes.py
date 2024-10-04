from flask import render_template, request
from . import app

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/runners', methods=['GET', 'POST'])
def runner():
    return render_template('runners.html')

