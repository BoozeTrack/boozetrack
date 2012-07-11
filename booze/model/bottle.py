from flask.ext.sqlalchemy import SQLAlchemy

from booze import app
db = SQLAlchemy(app)

class Bottle(db.Model):

    __tablename__ = 'bottles'
    __table_args__ = {'mysql_engine':'InnoDB'}

    bottle_id = db.Column(CHAR(22), primary_key=True)
    name      = db.Column(db.String(255))
    upc       = db.Column(db.BigInteger)   # 6, 12, or 13 digit number:  http://en.wikipedia.org/wiki/Universal_Product_Code
    abv       = db.Column(db.SmallInteger) # divide by 10, 0-100% with one decimal place (for beer like 5.4%)

    maker_id  = db.Column(db.CHAR(22), db.ForeignKey('makers.maker_id'))
    type_id   = db.Column(db.CHAR(22), db.ForeignKey('types.type_id'))
    size_id   = db.Column(db.CHAR(22), db.ForeignKey('sizes.size_id'))
