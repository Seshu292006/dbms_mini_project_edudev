import flask
from flask import Flask, request, render_template, redirect, url_for
from flask_pymongo import PyMongo


app=flask.Flask(__name__)

mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/flaskmongo")
db = mongodb_client.db


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # process form, save user, etc.
        return redirect(url_for('login'))  # 'login' is the endpoint for your login route
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    n = e = p = ''
    if request.method == 'POST':
        n = request.form.get('username', '')
        e = request.form.get('email', '')
        p = request.form.get('password', '')
        db.user_info.insert_many([
    {'username': n, 'email': e, 'password': p}
])
        return redirect(url_for('home'))  # Redirect to a home page or dashboard after login
    return render_template('login.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/about', methods=['GET', 'POST'])
def about():   
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():   
    return render_template('contact.html')


@app.route('/courses', methods=['GET', 'POST'])
def courses():   
    return render_template('courses.html')

if __name__ == "__main__":
    app.run(debug=True)

    
