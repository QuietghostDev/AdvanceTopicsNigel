from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Destinations, Base, Routes

engine = create_engine('sqlite:///routes.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

Philadelphia = Destinations(airportName="Philadelphia", id=1)
session.add(Philadelphia)
ito2 = Routes(name="Philadelphia to New York", destination="New York", time=.75, price=5, origin_id=1)
session.add(ito2)
ito6 = Routes(name="Philadelphia to Chicago", destination="Chicago", time=1.5, price=5, origin_id=1)
session.add(ito6)

NewYork = Destinations(airportName="New York", id=2)
session.add(NewYork)
bto1 = Routes(name="New York to Philadelphia", destination="Philadelphia", time=.75, price=5, origin_id=2)
session.add(bto1)
bto6 = Routes(name="New York to Chicago", destination="New York", time=1.5, price=5, origin_id=2)
session.add(bto6)
bto2 = Routes(name="New York to New York", destination="New York", time=0, price=100000000, origin_id=2)
session.add(bto2)
bto3 = Routes(name="New York to Los Angeles", destination="Los Angeles", time=5.5, price=5, origin_id=2)
session.add(bto3)
bto4 = Routes(name="New York to San Fransisco", destination="San Fransisco", time=5.5, price=5, origin_id=2)
session.add(bto4)
bto5 = Routes(name="New York to Boston", destination="Boston", time=.9, price=5, origin_id=2)
session.add(bto5)
bto7 = Routes(name="New York to Dallas", destination="Dallas", time=2, price=5, origin_id=2)
session.add(bto7)

LosAngeles = Destinations(airportName="Los Angeles", id=3)
session.add(LosAngeles)
cto2 = Routes(name="Los Angeles to New York", destination="New York", time=5.5, price=5, origin_id=3)
session.add(cto2)
cto6 = Routes(name="Los Angeles to Chicago", destination="Chicago", time=4, price=5, origin_id=3)
session.add(cto6)
cto4 = Routes(name="Los Angeles to San Fransisco", destination="San Fransisco", time=.85, price=5, origin_id=3)
session.add(cto4)

SanFrancisco = Destinations(airportName="San Francisco", id=4)
session.add(SanFrancisco)
dto2 = Routes(name="San Fransisco to New York", destination="New York",  time=5.5, price=5, origin_id=4)
session.add(dto2)
dto6 = Routes(name="San Fransisco to Chicago", destination="Chicago", time=4, price=5, origin_id=4)
session.add(dto6)
dto6 = Routes(name="San Fransisco to Los Angeles", destination="Los Angeles", time=.85, price=5, origin_id=4)
session.add(dto6)
dto7 = Routes(name="San Fransisco to Dallas", destination="New York", time=1.5, price=5, origin_id=4)
session.add(dto7)

Boston = Destinations(airportName="Boston", id=5)
session.add(Boston)
eto2 = Routes(name="Boston to New York", destination="New York", time=.9, price=5, origin_id=5)
session.add(eto2)
eto6 = Routes(name="Boston to Chicago", destination="Chicago", time=2.6, price=5, origin_id=5)
session.add(eto6)

Chicago = Destinations(airportName="Chicago", id=6)
session.add(Chicago)
fto2 = Routes(name="Chicago to New York", destination="New York", time=1.5, price=5, origin_id=6)
session.add(fto2)
fto1 = Routes(name="Chicago to Philadelphia", destination="Philadelphia", time=1.5, price=5, origin_id=6)
session.add(fto1)
fto3 = Routes(name="Chicago to Los Angeles", destination="Los Angeles", time=4, price=5, origin_id=6)
session.add(fto3)
fto4 = Routes(name="Chicago to San Fransisco", destination="San Fransisco", time=4, price=5, origin_id=6)
session.add(fto4)
fto5 = Routes(name="Chicago to Boston", destination="Boston", time=2.6, price=5, origin_id=6)
session.add(fto5)
fto7 = Routes(name="Chicago to Dallas", destination="Dallas", time=2, price=5, origin_id=6)
session.add(fto7)

Dallas = Destinations(airportName="Dallas", id=7)
session.add(Dallas)
gto2 = Routes(name="Dallas to New York", destination="New York", time=5, price=5, origin_id=7)
session.add(gto2)
gto6 = Routes(name="Dallas to Chicago", destination="Chicago", time=2, price=5, origin_id=7)
session.add(gto6)
gto4 = Routes(name="Dallas to San Fransisco", destination="San Fransisco", time=3.5, price=5, origin_id=7)
session.add(gto4)

session.commit()
