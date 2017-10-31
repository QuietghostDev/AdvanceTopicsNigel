from sqlalchemy import Column, Float, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Aircraft(Base):
    __tablename__ = "Aircraft"

    icao = Column(String(4))
    iata = Column(String(20))
    reg = Column(String(7), unique=True, primary_key=True)
    age = Column(Float)
    weight_class = Column(String(7))
    airline = Column(String(30))
    active = Column(Boolean)
    status = Column(String(10))

    def __init__(self, icao, iata, reg, age, weight_class, airline, active=True, status="Active"):
        self.icao = icao
        self.iata = iata
        self.reg = reg
        self.age = age
        self.weight_class = weight_class
        self.airline = airline
        self.active = active
        self.status = status

    def __repr__(self):
        return '<Aircraft %r>' % (self.reg)
