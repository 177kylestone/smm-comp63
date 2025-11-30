import requests
from flask import current_app

def fetch_eto_and_precip(lat, lon):
    base = current_app.config.get('OPEN_METEO_BASE')
    params = {'latitude': lat, 'longitude': lon, 'daily': 'precipitation_sum,et0_fao56', 'timezone': 'UTC'}
    r = requests.get(base, params=params, timeout=10)
    r.raise_for_status()
    js = r.json().get('daily', {})
    times = js.get('time', [])
    prec = js.get('precipitation_sum', [])
    eto = js.get('et0_fao56', [])
    out = []
    for i, d in enumerate(times):
        out.append({'date': d, 'precip_mm': prec[i] if i < len(prec) else None, 'eto_mm': eto[i] if i < len(eto) else None})
    return out
