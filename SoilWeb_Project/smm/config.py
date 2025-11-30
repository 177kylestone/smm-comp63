import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///smm.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPEN_METEO_BASE = os.getenv('OPEN_METEO_BASE', 'https://api.open-meteo.com/v1/forecast')
