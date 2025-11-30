from smm import create_app
from smm.extensions import db

import tempfile
import os
import pytest

@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()
    os.close(db_fd)
    cfg = type('C', (), {})
    cfg.SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_path
    cfg.SECRET_KEY = 'test'
    app = create_app(config_class=cfg)
    with app.app_context():
        db.create_all()
    yield app
    os.unlink(db_path)

@pytest.fixture
def client(app):
    return app.test_client()

def test_advice_404(client):
    rv = client.get('/api/advice/1')
    assert rv.status_code == 404
