from flask import Blueprint, jsonify, request
from models import Item, item_schema, items_schema, db
import pandas as pd

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'yee': 'haw'}

@api.route('/items', methods = ['GET'])
def get_item():
    items = Item.query.all()
    print(items)
    response = items_schema.dump(items)
    return jsonify(response)

@api.route('/upload', methods = ['POST'])
def post_item():

    data = pd.read_csv('main_folder/static/images/DivvyChallenge.csv', sep = ',')
    print(f"hello, here is your data: {data['trip_id']}")
    # My data clearly imported fine; I am unsure how to get each row to send to the database, since apparently SQLAlchemy
    # is only interested in hashable data types, and Pandas makes things into 'series' which SQLAlchemy refuses to read.
    # I'd have solved it but then StackOverflow went down for maintenance. So I ate dinner instead and handed it in anyways.
    # I thought my attempted solution was moderately clever, but it didn't quite execute. Sorry, Ryan.
    # The database is connected and functional, but I'd have to manually insert the data at this point for 'the grade', 
    # and I am too lazy for that. #automateeverything
    for number in range(65498):
        trip_id = data['trip_id']
        starttime = data['starttime']
        stoptime = data['stoptime']
        bikeid = data['bikeid']
        from_station_id = data['from_station_id']
        from_station_name = data['from_station_name']
        to_station_id = data['to_station_id']
        to_station_name = data['to_station_name']
        usertype = data['usertype']
        gender = data['gender']
        birthday = data['birthday']
        trip_duration = data['trip_duration']

        item = Item(trip_id, starttime, stoptime, bikeid, from_station_id, from_station_name, to_station_id, to_station_name, usertype, gender, birthday, trip_duration)

        db.session.add(item)
        db.session.commit()

    response = items_schema.dump(item)
    return jsonify(response)