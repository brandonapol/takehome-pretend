# imports 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow 
import uuid 
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()


class Item(db.Model):
    trip_id = db.Column(db.String, primary_key = True)
    starttime = db.Column(db.String(150))
    stoptime = db.Column(db.String(150))
    bikeid = db.Column(db.String(150))
    from_station_id = db.Column(db.String(150))
    from_station_name = db.Column(db.String(150))
    to_station_id = db.Column(db.String(150))
    to_station_name = db.Column(db.String(150))
    usertype = db.Column(db.String(150))
    gender = db.Column(db.String(150))
    birthday = db.Column(db.String(150))
    trip_duration = db.Column(db.String(150))

    def __init__(self, trip_id, starttime, stoptime, bikeid, from_station_id, from_station_name, to_station_id, to_station_name, usertype, gender, birthday, trip_duration):
        self.trip_id = trip_id
        self.starttime = starttime
        self.stoptime = stoptime
        self.bikeid = bikeid
        self.from_station_id = from_station_id
        self.from_station_name = from_station_name
        self.to_station_id = to_station_id
        self.to_station_name = to_station_name
        self.usertype = usertype
        self.gender = gender
        self.birthday = birthday
        self.trip_duration = trip_duration


    def __repr__(self):
        return f'The following vehicle has been added to the collection: {self.name}'


class ItemSchema(ma.Schema):
    class Meta:
        fields = ['id', 'name','description']

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)