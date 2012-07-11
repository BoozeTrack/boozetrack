from flask.ext.sqlalchemy import SQLAlchemy

from booze import app
db = SQLAlchemy(app)

class User(db.Model):

    __tablename__ = 'users'
    __table_args__ = {'mysql_engine':'InnoDB'}

    user_id   = db.Column(CHAR(22), primary_key=True)
    username  = db.Column(db.String(80), unique=True)
    email     = db.Column(db.String(120), unique=True)
    fb_id     = db.Column(db.BigInteger)
    state     = db.Column(db.CHAR(2))

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
