#!flask/bin/python3
from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	items = db.relationship('Item', backref='owner', lazy='dynamic')

	def __repr__(self):
		return '<User %r>' % (self.nickname)

class Item(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(140))
	description = db.Column(db.String(140))
	location_name = db.Column(db.String(64))
	location_address = db.Column(db.String(64))
	message = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Item %r>' % (self.body)