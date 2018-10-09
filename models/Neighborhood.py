# coding=utf-8
import time
import json

from database import db

class Neighborhood(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'), nullable=False)
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'), nullable=False)
    name = db.Column(db.String(255))
    price = db.Column(db.Integer)
    position_info = db.Column(db.String(255))
    house_info = db.Column(db.String(255))
    vendor_given_id = db.Column(db.String(255))
    area = db.Column(db.String(255))
    year = db.Column(db.String(255))
    update_time = db.Column(db.Integer, nullable=False, default=time.time, onupdate=time.time)

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return '<Neighborhood %r>' % self.name
