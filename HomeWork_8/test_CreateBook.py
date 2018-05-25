import requests


def remove_book(info):
    requests.delete(url='http://pulse-rest-testing.herokuapp.com/' + 'books/' + str(info) + '/')


def test_create_positive(base_url):
    book = {'title': 'Eat.Pray.Love', 'author': 'Elizabeth Gilbert'}
    r = requests.post(url=base_url + 'books/', data=book)
    assert r.status_code == 201
    act_body = r.json()
    book.update([('id', act_body['id'])])
    assert act_body == book
    remove_book(book['id'])


def test_create_no_data(base_url):
    book = {}
    r = requests.post(url=base_url + 'books/', data=book)
    assert r.status_code == 400
    act_body = r.json()
    exp_body = {'title': ['This field is required.'], 'author': ['This field is required.']}
    assert act_body == exp_body


def test_create_only_title(base_url):
    book = {'title': 'The Girl on the Train'}
    r = requests.post(url=base_url + 'books/', data=book)
    assert r.status_code == 400
    act_body = r.json()
    exp_body = {'author': ['This field is required.']}
    assert act_body == exp_body


def test_create_only_author(base_url):
    book = {'author': 'Paula Hawkins'}
    r = requests.post(url=base_url + 'books/', data=book)
    assert r.status_code == 400
    act_body = r.json()
    exp_body = {'title': ['This field is required.']}
    assert act_body == exp_body


def test_create_empty_title_author(base_url):
    book = {'title': None, 'author': None}
    r = requests.post(url=base_url + 'books/', data=book)
    assert r.status_code == 400
    act_body = r.json()
    exp_body = {'title': ['This field is required.'], 'author': ['This field is required.']}
    assert act_body == exp_body


def test_create_empty_title(base_url):
    book = {'title': None, 'author': 'Paula Hawkins'}
    r = requests.post(url=base_url + 'books/', data=book)
    assert r.status_code == 400
    act_body = r.json()
    exp_body = {'title': ['This field is required.']}
    assert act_body == exp_body


def test_create_empty_author(base_url):
    book = {'title': 'The Girl on the Train', 'author': None}
    r = requests.post(url=base_url + 'books/', data=book)
    assert r.status_code == 400
    act_body = r.json()
    exp_body = {'author': ['This field is required.']}
    assert act_body == exp_body


def test_create_length_limit_title_author(base_url):
    book = {'title': '12345678901234567890123456789012345678901234567890A',
            'author': '12345678901234567890123456789012345678901234567890B'}
    r = requests.post(url=base_url + 'books/', data=book)
    assert r.status_code == 400
    act_body = r.json()
    exp_body = {'title': ['Ensure this field has no more than 50 characters.'],
                'author': ['Ensure this field has no more than 50 characters.']}
    assert act_body == exp_body


def test_create_length_limit_title(base_url):
    book = {'title': '12345678901234567890123456789012345678901234567890A',
            'author': 'Paula Hawkins'}
    r = requests.post(url=base_url + 'books/', data=book)
    assert r.status_code == 400
    act_body = r.json()
    exp_body = {'title': ['Ensure this field has no more than 50 characters.']}
    assert act_body == exp_body


def test_create_length_limit_author(base_url):
    book = {'title': 'The Girl on the Train',
            'author': '12345678901234567890123456789012345678901234567890B'}
    r = requests.post(url=base_url + 'books/', data=book)
    assert r.status_code == 400
    act_body = r.json()
    exp_body = {'author': ['Ensure this field has no more than 50 characters.']}
    assert act_body == exp_body


def test_create_wrong_data_type(base_url):
    book = {'title': 102589, 'author': 15.289}
    r = requests.post(url=base_url + 'books/', data=book)
    assert r.status_code == 201
    act_body = r.json()
    exp_body = {'title': '102589', 'author': '15.289'}
    exp_body.update([('id', act_body['id'])])
    assert act_body == exp_body
    remove_book(exp_body['id'])


def test_create_already_created_book(base_url):
    book = {'title': 'The Girl on the Train', 'author': 'Paula Hawkins'}
    r_created = requests.post(url=base_url + 'books/', data=book)
    r = requests.post(url=base_url + 'books/', data=book)
    assert r.status_code == 201
    act_body = r.json()
    book.update([('id', act_body['id'])])
    assert act_body == book
    remove_book(r_created.json()['id'])
    remove_book(book['id'])
