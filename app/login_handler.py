from flask import request, jsonify
from . import app
from .utils import validate_phone_number, generate_code

CHECK_USER_DATA = {}


@app.get('/login')
def get_login():
    phone = request.args.get('phone')
    if phone:
        validated_phone_number = validate_phone_number(phone)
        code = generate_code()
        CHECK_USER_DATA.update({validated_phone_number: code})
        return jsonify({'code': code})
    return jsonify({'error': 'phone number is required'})


@app.post('/login')
def post_login():
    phone = code = ''
    try:
        phone = request.json['phone']
    except AttributeError:
        jsonify({'error': 'phone number is required'})

    try:
        code = request.json['code']
    except AttributeError:
        jsonify({'error': 'code is required'})

    validated_phone_number = validate_phone_number(phone)
    if CHECK_USER_DATA.get(validated_phone_number) == code:
        return jsonify({'status': 'OK'})
    return jsonify({'status': 'Fail'})
