import pytest

from app.app import init_app


@pytest.fixture
def app():
    app = init_app()
    return app


@pytest.fixture
def phone():
    return '+7 (123) 456-78-90'


@pytest.fixture
def login_query_string(phone):
    return {'phone': phone}


@pytest.fixture
def structure_query_string():
    return {'link': 'http://google.com'}


@pytest.fixture
def tags():
    return {'html', 'div', 'p'}
