from .models import Paddock

def store_estimate(paddock: Paddock):
    return round(paddock.paw_mm * 0.6, 2)
