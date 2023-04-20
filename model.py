from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy import Column
from sqlalchemy import Integer
from datetime import datetime           

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Akshay@123@127.0.0.1/Akshay'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)
class blog_detail13(db.Model):
    blogid = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100),nullable=False)
    Organisation = db.Column(db.String(500),nullable=False)
    DOJ = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    DOE = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    def __init__(self, Name, Organisation,DOJ,DOE):
        self.name = Name
        self.organisation = Organisation
        self.doj = DOJ
        self.doe = DOE
    def __repr__(self):
        return f"{self.name}, {self.organisation}, {self.doj}, {self.doe}"
if __name__=="__main__":
    db.create_all()
