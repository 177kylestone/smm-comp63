import click
from flask.cli import with_appcontext
from .extensions import db
from .models import Paddock, Sensor
from datetime import datetime

def register(app):
    @app.cli.command('seed')
    @with_appcontext
    def seed():
        """Seed DB with demo paddock and sensor"""
        if Paddock.query.count() == 0:
            p = Paddock(name='Demo Paddock')
            db.session.add(p)
            db.session.commit()
            s = Sensor(paddock_id=p.id, depth_cm=20, installed_at=datetime.utcnow())
            db.session.add(s)
            db.session.commit()
            click.echo(f'Seeded paddock {p.id}, sensor {s.id}')
        else:
            click.echo('DB already seeded')
