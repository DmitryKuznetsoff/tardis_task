import random

from flask import url_for


def test_structure_get_default_link(client):
    res = client.get(url_for('get_structure'))

    assert res.status_code == 200

    structure = res.json
    assert 'html' in structure


def test_structure_get_certain_link(client, structure_query_string):
    res = client.get(url_for('get_structure'), query_string=structure_query_string)

    assert res.status_code == 200

    structure = res.json
    assert 'html' in structure


def test_structure_get_certain_link_with_tags(client, structure_query_string, tags):
    structure_query_string.update({'tags': tags})
    res = client.get(url_for('get_structure'), query_string=structure_query_string)

    assert res.status_code == 200

    structure = res.json
    assert set(structure.keys()).issubset(tags)


def test_structure_post_correct_structure(client, structure_query_string):
    structure = client.get(url_for('get_structure'), query_string=structure_query_string).json
    data = {'structure': structure}
    data.update(structure_query_string)

    res = client.post(url_for('post_structure'), json=data)

    assert res.status_code == 200
    assert res.json.get('is_correct')


def test_structure_post_incorrect_structure(client, structure_query_string):
    structure = client.get(url_for('get_structure'), query_string=structure_query_string).json

    random_tag = random.choice(list(structure.keys()))
    structure[random_tag] += 1
    data = {'structure': structure}
    data.update(structure_query_string)

    res = client.post(url_for('post_structure'), json=data)

    assert res.status_code == 200
    assert not res.json.get('is_correct')
    assert random_tag in res.json['difference']
