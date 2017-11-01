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
    db.session.add(Aircraft('B738', 'Boeing 737-823(WL)', 'N990NN', 1.5, 'CLASS 3', 'Boeing', 'American Airlines'))
    db.session.add(Aircraft('A333', 'A330-323', 'N270AY', 17.5, 'CLASS 3', 'Airbus', 'American Airlines'))
    db.session.add(Aircraft('B738', 'Boeing 737-890(WL)', 'N524AS', 8.6, 'CLASS 3', 'Boeing', 'Alaska Airlines'))
    db.session.add(Aircraft('B752', 'Boeing 757-236(SF)', 'G-BIKV', 31.0, 'CLASS 3', 'Boeing', 'DHL Air', False, 'Scrapped'))
    db.session.commit()


@app.route('/')
def root():
    Aircrafts = db.session.query(Aircraft).all()
    return u"<br>".join([u"{0}: {1}, {2}".format(aircraft.reg, aircraft.iata, aircraft.icao) for aircraft in Aircrafts])


if __name__ == '__main__':
    app.run('127.0.0.1', 5000)
