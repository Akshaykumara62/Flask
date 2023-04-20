from flask import Flask, render_template
from model import app

@app.route("/")
def welcome():
    return "Welcome"

@app.route("/name")
def profile():
    return "Hello"

@app.route('/info/<my_name>')
def userinfo(my_name):
    return "Hello Welcome to the Site Mr."+my_name
@app.route('/all/<my_name>')
def all_name(my_name):
    return render_template('main.html',name=my_name)


app.route("/image")
def image1():
    return render_template('image.html')

if __name__=="__main__":
    app.run()