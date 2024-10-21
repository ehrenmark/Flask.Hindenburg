
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

db = SQLAlchemy()
DB_NAME = "database.db"



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))


class Airports(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(150))
    IATA = db.Column(db.String(150))
    ICAO = db.Column(db.String(150))
    Country = db.Column(db.String(150))
    Continent = db.Column(db.String(150))
    Passengers = db.Column(db.Integer)
    Cargo = db.Column(db.Integer)
    altitude = db.Column(db.Integer)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

