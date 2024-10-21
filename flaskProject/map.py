from datetime import datetime, timedelta
import sqlite3
import requests
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from models import db
from models import Airports
from sqlalchemy import or_, and_
import json

map = Blueprint('map', __name__)


@map.route('/map', methods=['GET', 'POST'])
@login_required
def map_function():


    airports = db.session.query(Airports).all()
    print(airports)



    return render_template("map2.html",
                           user=current_user,
                           airports=airports,
                           )
