import csv, io
from datetime import datetime
from ..models import Reading
from ..extensions import db
from ..calibrate import raw_to_vwc

def parse_and_store_csv(file_storage):
    content = file_storage.read()
    if isinstance(content, bytes):
        txt = content.decode('utf-8')
    else:
        txt = str(content)
    reader = csv.DictReader(io.StringIO(txt))
    inserted = 0
    errors = []
    for i, row in enumerate(reader, start=1):
        try:
            sid = int(row['sensor_id'])
            ts = datetime.fromisoformat(row['ts'])
            raw = float(row['raw'])
            temp = float(row['temp_c']) if row.get('temp_c') not in (None, '') else None
            vwc = raw_to_vwc(raw)
            r = Reading(sensor_id=sid, ts=ts, raw=raw, vwc=vwc, temp_c=temp, qc_flag='OK')
            db.session.add(r)
            inserted += 1
        except Exception as e:
            errors.append(f'row {i}: {str(e)}')
    db.session.commit()
    return {'inserted': inserted, 'errors': errors}
