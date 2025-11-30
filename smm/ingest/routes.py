from flask import request, jsonify
from .service import parse_and_store_csv
from . import bp

@bp.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('file')
    if not f:
        return jsonify({'error': 'no file'}), 400
    res = parse_and_store_csv(f)
    return jsonify(res)
