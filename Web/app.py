from flask import Flask
from models import Base, Aircraft
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


@app.before_first_request
def setup():
    Base.metadata.drop_all(bind=db.engine)
    Base.metadata.create_all(bind=db.engine)
    db.session.add(Aircraft('B738', '737-823(WL)', 'N990NN', 1.5, 'CLASS 3', 'Boeing', 'American Airlines'))
    db.session.add(Aircraft('A333', '330-323', 'N270AY', 17.5, 'CLASS 3', 'Airbus', 'American Airlines'))
    db.session.add(Aircraft('B738', '737-823(WL)', 'N917NN', 4.8, 'CLASS 3', 'Boeing', 'American Airlines'))
    db.session.add(Aircraft('B738', '737-890(WL)', 'N524AS', 8.6, 'CLASS 3', 'Boeing', 'Alaska Airlines'))
    db.session.add(Aircraft('B77W', '777-31H(ER)', 'A6-EGR', 5.5, 'CLASS 3', 'Boeing', 'Emirtates'))
    db.session.add(Aircraft('B752', '757-236(SF)', 'G-BIKV', 31.0, 'CLASS 3', 'Boeing', 'DHL Air', False, 'Scrapped'))
    db.session.add(Aircraft('B744', '747-422', 'N118UA', 18.8, 'CLASS 3', 'Boeing', 'United Airlines', False, 'Stored'))
    db.session.commit()

@app.route('/')
def root():
    Aircrafts = db.session.query(Aircraft).all()
    return u"<br>".join([u"{0}: {1} {2}, {3}".format(aircraft.reg, aircraft.manufacturer, aircraft.model, aircraft.icao) for aircraft in Aircrafts])

@app.route("/Boeing")
def boeing():
    Aircrafts = db.session.query(Aircraft).filter(Aircraft.manufacturer == 'Boeing')
    return u"<br>".join([u"{0}: {1} {2}, {3}".format(aircraft.reg, aircraft.manufacturer, aircraft.model, aircraft.icao) for aircraft in Aircrafts])

@app.route("/Airbus")
def airbus():
    Aircrafts = db.session.query(Aircraft).filter(Aircraft.manufacturer == 'Airbus')
    return u"<br>".join([u"{0}: {1} {2}, {3}".format(aircraft.reg, aircraft.manufacturer, aircraft.model, aircraft.icao) for aircraft in Aircrafts])

@app.route("/Active")
def active():
    Aircrafts = db.session.query(Aircraft).filter(Aircraft.active == True)
    return u"<br>".join([u"{0}: {1} {2}, {3}".format(aircraft.reg, aircraft.manufacturer, aircraft.model, aircraft.icao) for aircraft in Aircrafts])

@app.route("/Retired")
def inactive():
    Aircrafts = db.session.query(Aircraft).filter(Aircraft.active == False)
    return u"<br>".join([u"{0}: {1} {2}, {3}".format(aircraft.reg, aircraft.manufacturer, aircraft.model, aircraft.icao) for aircraft in Aircrafts])

if __name__ == '__main__':
    app.run('127.0.0.1', 5000)
