# coding=utf-8
import time
import json

from database import db

class District(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    url = db.Column(db.String(255))
    update_time = db.Column(db.Integer, nullable=False, default=time.time, onupdate=time.time)

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return '<District %r>' % self.name
