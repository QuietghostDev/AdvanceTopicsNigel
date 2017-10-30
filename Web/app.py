from flask import Flask
from models import Base, User
from flask_sqlalchemy import SQLAlchemy

app =  Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.before_first_request
def setup():
    Base.metadata.drop_all(bind=db.engine)
    Base.metadata.create_all(bind=db.engine)
    db.session.add(Aircraft('B738', 'Boeing 737-800', 'N990NN', 'American Airlines'))
    db.session.commit()

@app.route('/')
def root():
    users = db.session.query(User).all()
    return u"<br>".join([u"{0}: {1}".format(user.name, user.email) for user in users])

if __name__ == '__main__':
    app.run('127.0.0.1', 5000)
