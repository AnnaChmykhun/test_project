import requests


def test_read_by_id(base_url, add_remove_book):
    r = requests.get(url=base_url + 'books/' + str(add_remove_book['id']) + '/')
    assert r.status_code == 200
    assert add_remove_book == r.json()


def test_general_read(base_url, add_remove_book):
    r = requests.get(url=base_url + 'books/')
    assert r.status_code == 200
    assert add_remove_book in r.json()


def test_read_without_id(base_url):
    r = requests.get(url=base_url + 'books/' + '/')
    assert r.status_code == 404


def test_read_by_title(base_url, add_remove_book):
    r = requests.get(url=base_url + 'books/' + add_remove_book['title'] + '/')
    assert r.status_code == 404


def test_read_by_author(base_url, add_remove_book):
    r = requests.get(url=base_url + 'books/' + add_remove_book['author'] + '/')
    assert r.status_code == 404


def test_read_deleted_id(base_url):
    book = {'title': 'Learning Python', 'author': 'Mark Lutz'}
    r1 = requests.post(url=base_url + 'books/', data=book)
    book_id = r1.json()['id']
    requests.delete(url=base_url + 'books/' + str(book_id) + '/')
    r2 = requests.get(url=base_url + 'books/' + str(book_id) + '/')
    assert r2.status_code == 404


def test_read_not_used_id(base_url):
    book = {'title': 'Learning Python', 'author': 'Mark Lutz'}
    r1 = requests.post(url=base_url + 'books/', data=book)
    book_id = r1.json()['id']
    requests.delete(url=base_url + 'books/' + str(book_id) + '/')
    r2 = requests.get(url=base_url + 'books/' + str(book_id + 10) + '/')
    assert r2.status_code == 404
