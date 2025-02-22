from app import app


def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b'Hi from flask app!!!' in response.data


def test_health():
    tester = app.test_client()
    response = tester.get('/actuator/healthz')
    assert response.status_code == 200
    assert b'UP' in response.data


def test_user():
    tester = app.test_client()
    response = tester.get('/user')
    assert response.status_code == 200
    assert b'tao' in response.data
