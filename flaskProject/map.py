from datetime import datetime, timedelta

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from models import db
from sqlalchemy import or_, and_
import json

map = Blueprint('map', __name__)


@map.route('/map', methods=['GET', 'POST'])
@login_required
def map_function():


    return render_template("map2.html",
                           user=current_user,
                           )


