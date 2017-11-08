from sqlalchemy import Column, Float, String, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Aircraft(Base):
    __tablename__ = "Aircraft"

    id = Column(Integer, primary_key=True)
    icao = Column(String(4))
    model = Column(String(20))
    reg = Column(String(7), unique=True)
    age = Column(Float)
    weight_class = Column(String(7))
    manufacturer = Column(String(30))
    airline = Column(String(30))
    active = Column(Boolean)
    status = Column(String(10))

    def __init__(self, icao, model, reg, age, weight_class, manufacturer, airline, active=True, status="Active"):
        self.icao = icao
        self.model = model
        self.reg = reg
        self.age = age
        self.weight_class = weight_class
        self.manufacturer = manufacturer
        self.airline = airline
        self.active = active
        self.status = status

    def __repr__(self):
        return '<Aircraft %r>' % (self.reg)
