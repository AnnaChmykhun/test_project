import requests


def test_id_title_author(base_url, add_remove_book_upd):
    new_book = {'id': 1500, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'}
    r = requests.put(url=base_url + 'books/' + str(add_remove_book_upd['id']) + '/', data=new_book)
    assert r.status_code == 200
    new_book.update([('id', add_remove_book_upd['id'])])
    assert r.json() == new_book


def test_title_author(base_url, add_remove_book_upd, parametrization_upd):
    r = requests.put(url=base_url + 'books/' + str(add_remove_book_upd['id']) + '/', data=parametrization_upd)
    assert r.status_code == 200
    parametrization_upd.update([('id', add_remove_book_upd['id'])])
    assert r.json() == parametrization_upd


def test_only_id(base_url, add_remove_book_upd):
    new_book = {'id': 1500}
    r = requests.put(url=base_url + 'books/' + str(add_remove_book_upd['id']) + '/', data=new_book)
    assert r.status_code == 200
    assert r.json() == add_remove_book_upd


def test_only_title(base_url, add_remove_book_upd):
    new_book = {'title': 'To Kill a Mockingbird'}
    r = requests.put(url=base_url + 'books/' + str(add_remove_book_upd['id']) + '/', data=new_book)
    assert r.status_code == 200
    new_book.update([('id', add_remove_book_upd['id']), ('author', add_remove_book_upd['author'])])
    assert r.json() == new_book


def test_only_author(base_url, add_remove_book_upd):
    new_book = {'author': 'Harper Lee'}
    r = requests.put(url=base_url + 'books/' + str(add_remove_book_upd['id']) + '/', data=new_book)
    assert r.status_code == 200
    new_book.update([('id', add_remove_book_upd['id']), ('title', add_remove_book_upd['title'])])
    assert r.json() == new_book


def test_empty_data(base_url, add_remove_book_upd):
    new_book = {}
    r = requests.put(url=base_url + 'books/' + str(add_remove_book_upd['id']) + '/', data=new_book)
    assert r.status_code == 200
    assert r.json() == add_remove_book_upd


def test_empty_params(base_url, add_remove_book_upd):
    new_book = {'title': '', 'author': ''}
    r1 = requests.put(url=base_url + 'books/' + str(add_remove_book_upd['id']) + '/', data=new_book)
    assert r1.status_code == 400
    exp_body = {'title': ['This field may not be blank.'], 'author': ['This field may not be blank.']}
    assert r1.json() == exp_body
    r2 = requests.get(url=base_url + 'books/' + str(add_remove_book_upd['id']) + '/')
    assert r2.json() == add_remove_book_upd


def test_empty_title(base_url, add_remove_book_upd):
    new_book = {'title': '', 'author': 'Harper Lee'}
    r1 = requests.put(url=base_url + 'books/' + str(add_remove_book_upd['id']) + '/', data=new_book)
    assert r1.status_code == 400
    exp_body = {'title': ['This field may not be blank.']}
    assert r1.json() == exp_body
    r2 = requests.get(url=base_url + 'books/' + str(add_remove_book_upd['id']) + '/')
    assert r2.json() == add_remove_book_upd


def test_empty_author(base_url, add_remove_book_upd):
    new_book = {'title': 'To Kill a Mockingbird', 'author': ''}
    r1 = requests.put(url=base_url + 'books/' + str(add_remove_book_upd['id']) + '/', data=new_book)
    assert r1.status_code == 400
    exp_body = {'author': ['This field may not be blank.']}
    assert r1.json() == exp_body
    r2 = requests.get(url=base_url + 'books/' + str(add_remove_book_upd['id']) + '/')
    assert r2.json() == add_remove_book_upd


def test_length_limit_params(base_url, add_remove_book_upd):
    new_book = {'title': '12345678901234567890123456789012345678901234567890A',
                'author': '12345678901234567890123456789012345678901234567890B'}
    r1 = requests.put(url=base_url + 'books/' + str(add_remove_book_upd['id']) + '/', data=new_book)
    assert r1.status_code == 400
    exp_body = {'title': ['Ensure this field has no more than 50 characters.'],
                'author': ['Ensure this field has no more than 50 characters.']}
    assert r1.json() == exp_body
    r2 = requests.get(url=base_url + 'books/' + str(add_remove_book_upd['id']) + '/')
    assert r2.json() == add_remove_book_upd


def test_length_limit_title(base_url, add_remove_book_upd):
    new_book = {'title': '12345678901234567890123456789012345678901234567890A',
                'author': 'Harper Lee'}
    r1 = requests.put(url=base_url + 'books/' + str(add_remove_book_upd['id']) + '/', data=new_book)
    assert r1.status_code == 400
    exp_body = {'title': ['Ensure this field has no more than 50 characters.']}
    assert r1.json() == exp_body
    r2 = requests.get(url=base_url + 'books/' + str(add_remove_book_upd['id']) + '/')
    assert r2.json() == add_remove_book_upd


def test_length_limit_author(base_url, add_remove_book_upd):
    new_book = {'title': 'To Kill a Mockingbird',
                'author': '12345678901234567890123456789012345678901234567890B'}
    r1 = requests.put(url=base_url + 'books/' + str(add_remove_book_upd['id']) + '/', data=new_book)
    assert r1.status_code == 400
    exp_body = {'author': ['Ensure this field has no more than 50 characters.']}
    assert r1.json() == exp_body
    r2 = requests.get(url=base_url + 'books/' + str(add_remove_book_upd['id']) + '/')
    assert r2.json() == add_remove_book_upd
