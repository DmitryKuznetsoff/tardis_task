from flask import request, jsonify
from . import app, init_redis
from .utils import validate_phone_number, generate_code

redis = init_redis()


@app.get('/login')
def get_login():
    phone = request.args.get('phone')
    if phone:
        validated_phone_number = validate_phone_number(phone)
        code = generate_code()
        redis.set(validated_phone_number, code)
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
    if redis.get(validated_phone_number).decode() == code:
        return jsonify({'status': 'OK'})
    return jsonify({'status': 'Fail'})
