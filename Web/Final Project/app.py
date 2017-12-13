from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Routes, Destinations

app = Flask(__name__)
engine = create_engine('sqlite:///routes.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/destinations/')
def showAllDestinations():
    destinations = session.query(Destinations).all()
    return render_template('molenaairlines.html', destinations=destinations)


@app.route('/destination/<int:origin_id>/', methods=['GET'])
def showFlights(origin_id):
    origin = session.query(Destinations).filter_by(id=origin_id).one()
    routes = session.query(Routes).filter_by(id=origin_id).all()
    return render_template('routes.html', city=origin, destinations=routes)


@app.route('/route/<int:id>/')
def showRoute(id):
    route = session.query(Routes).filter_by(id=id).one()
    return render_template('placeholder.html')


@app.route('/search/', methods=['GET', 'POST'])
def searchFlight():
    return render_template('flightSearch.html')


def redirectSearch():
    if request.form['origin'] and request.form['destination']:
        id = session.query(Routes).filter_by(origin=request.form['origin']).filter_by(
            destination=request.form['destination']).one()
        return redirect(url_for('showRoute', id=id))
    else: return redirect(url_for('searchFlight'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
