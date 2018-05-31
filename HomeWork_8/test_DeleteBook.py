import requests


def test_positive_delete(base_url, add_remove_book_del):
    r1 = requests.delete(url=base_url + 'books/' + str(add_remove_book_del['id']) + '/')
    assert r1.status_code == 204
    r2 = requests.get(url=base_url + 'books/' + str(add_remove_book_del['id']) + '/')
    assert r2.status_code == 404


def test_without_id(base_url):
    r1 = requests.delete(url=base_url + 'books/' + '/')
    assert r1.status_code == 404


def test_delete_by_title(base_url, add_remove_book_del):
    r1 = requests.delete(url=base_url + 'books/' + add_remove_book_del['title'] + '/')
    assert r1.status_code == 404
    r2 = requests.get(url=base_url + 'books/' + str(add_remove_book_del['id']) + '/')
    assert r2.status_code == 200
    assert r2.json() == add_remove_book_del


def test_delete_by_author(base_url, add_remove_book_del):
    r1 = requests.delete(url=base_url + 'books/' + add_remove_book_del['author'] + '/')
    assert r1.status_code == 404
    r2 = requests.get(url=base_url + 'books/' + str(add_remove_book_del['id']) + '/')
    assert r2.status_code == 200
    assert r2.json() == add_remove_book_del


def test_deleted_id(base_url):
    book = {'title': 'Learning Python', 'author': 'Mark Lutz'}
    r1 = requests.post(url=base_url + 'books/', data=book)
    book_id = r1.json()['id']
    requests.delete(url=base_url + 'books/' + str(book_id) + '/')
    r2 = requests.delete(url=base_url + 'books/' + str(book_id) + '/')
    assert r2.status_code == 404


def test_not_used_id(base_url):
    book = {'title': 'Learning Python', 'author': 'Mark Lutz'}
    r1 = requests.post(url=base_url + 'books/', data=book)
    book_id = r1.json()['id']
    requests.delete(url=base_url + 'books/' + str(book_id) + '/')
    r2 = requests.delete(url=base_url + 'books/' + str(book_id + 10) + '/')
    assert r2.status_code == 404
