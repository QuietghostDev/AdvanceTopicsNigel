from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.py import Base, Routes, Destinations

app = Flask(__name__)
engine = create_engine
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/destinations/')
def showAllDestinations():
    destinations = session.query(Destinations).all()
    return render_template(routes)

@app.route('/destination/<id:origin_id>/')
def showFlights(origin_id):
    origin = session.query(Destinations).filter_by(id=origin_id).one()
    routes = session.query(Routes).filter_by(id=origin_id).all()
    return render_template(city=origin, destinations=routes)
