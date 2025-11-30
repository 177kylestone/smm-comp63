from .extensions import db
from datetime import datetime

class Paddock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    geom_wkt = db.Column(db.Text)
    paw_mm = db.Column(db.Float, default=150.0)
    kc = db.Column(db.Float, default=1.0)
    mad_fraction = db.Column(db.Float, default=0.5)

class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    paddock_id = db.Column(db.Integer, db.ForeignKey('paddock.id'))
    depth_cm = db.Column(db.Integer)
    installed_at = db.Column(db.DateTime, default=datetime.utcnow)
    paddock = db.relationship('Paddock', backref='sensors')

class Reading(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'))
    ts = db.Column(db.DateTime)
    raw = db.Column(db.Float)
    vwc = db.Column(db.Float)
    temp_c = db.Column(db.Float)
    qc_flag = db.Column(db.String(32))
    sensor = db.relationship('Sensor', backref='readings')
