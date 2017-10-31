from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Aircraft(Base):
    __tablename__ = "Aircraft"

    icao = Column(String(4))
    iata = Column(String(20))
    reg = Column(String(7), unique=True, primary_key=True)
    age = Column(Integer)
    airline = Column(String(30))
    status = Column(Boolean)

    def __init__(self, icao, iata, reg, age, airline, status):
        self.icao = icao
        self.iata = iata
        self.reg = reg
        self.age = age
        self.airline = airline
        self.status = status

    def __repr__(self):
        return '<Aircraft %r>' % (self.reg)
