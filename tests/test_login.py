from flask import url_for


def test_login_get(client, login_query_string):

    res = client.get(url_for('get_login'), query_string=login_query_string)

    assert res.status_code == 200
    assert res.json.get('code')


def test_login_post_correct_data(client, phone, login_query_string):
    code = client.get(url_for('get_login'), query_string=login_query_string).json.get('code')
    data = {'phone': phone, 'code': code}

    res = client.post(url_for('post_login'), json=data)

    assert res.status_code == 200
    assert res.json.get('status') == 'OK'


def test_login_post_incorrect_data(client, phone, login_query_string):
    code = client.get(url_for('get_login'), query_string=login_query_string).json.get('code')
    code += 'INCORRECT'
    data = {'phone': phone, 'code': code}

    res = client.post(url_for('post_login'), json=data)

    assert res.status_code == 200
    assert res.json.get('status') == 'Fail'
