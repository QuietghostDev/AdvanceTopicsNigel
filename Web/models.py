from sqlalchemy import Column, Interger, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Aircraft(Base):
    __tablename__ = "aircraft"

    icao = Column(String(4))
    iata = Column(String(20))
    reg = Column(String(7), unique=True)
    age = Column(Interger)
    airline = Column(String(30))

    def __init__(self, icao, iata, reg, age, airline):
        self.icao = icao
        self.iata = iata
        self.reg = reg
        self.age = age
        self.airline = airline

    def __repr__(self):
        return '<Aircraft %r>' % (self.reg)
