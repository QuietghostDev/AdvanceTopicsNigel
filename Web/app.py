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
    db.session.add(Aircraft('B738', 'Boeing 737-823(WL)', 'N990NN', 1.5, 'American Airlines', True))
    db.session.commit()


@app.route('/')
def root():
    Aircrafts = db.session.query(Aircraft).all()
    return u"<br>".join([u"{0}: {1}, {2}".format(aircraft.reg, aircraft.iata, aircraft.icao) for aircraft in Aircrafts])


if __name__ == '__main__':
    app.run('127.0.0.1', 5000)
