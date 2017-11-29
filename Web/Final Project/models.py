import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, create_engine
from sqlalchemy.exe.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Destinations(Base):
    __tablename__ = 'destinations'

    id = Column(Integer, primary_key=True)
    airportName = Column(String(255))

    @property
    def serialize(self):
        return {'airportName':self.airportName, 'id':self.id}

class Routes(Base):
    __tablename__ = 'routes'

    id = Column(Integer, primary_key=True)
    destination = Column(String(255))
    time = Column(Integer)
    price = Column(Float)
    origin_id = Column(Integer, ForeignKey('destinations.id'))
    origin = relationship(Destinations)
