from nose.tools import *
from app import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 404)
    
    rv = web.get('/hello', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"Fill out this form", rv.data)
    
    data = {'name': 'Tai', 'greet': 'Xin chao'}
    rv = web.post('/hello', follow_redirects=True, data=data)
    assert_in(b'Tai', rv.data)
    assert_in(b'Xin chao', rv.data)
