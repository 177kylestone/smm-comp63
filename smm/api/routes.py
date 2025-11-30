from flask import jsonify, abort
from . import bp
from ..models import Paddock

@bp.route('/advice/<int:paddock_id>')
def advice(paddock_id):
    p = Paddock.query.get(paddock_id)
    if not p:
        abort(404)
    return jsonify({
        'paddock_id': p.id,
        'paw_mm': p.paw_mm,
        'store_mm_estimate': round(p.paw_mm * 0.6, 2),
        'advice': 'No urgent irrigation need (MVP).'
    })
