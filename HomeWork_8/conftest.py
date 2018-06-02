import pytest
import requests
import json


@pytest.fixture(scope='session')
def base_url():
    return 'http://pulse-rest-testing.herokuapp.com/'


# @pytest.fixture(scope="module")
# def add_remove_book(base_url, request):
#     book = {'title': 'Alice in Wonderland', 'author': 'Lewis Carroll'}
#     r = requests.post(url=base_url + 'books/', data=book)
# #    book.update([('id', r.json()['id'])])
#     book['id'] = r.json()['id']
#
#     def fin():
#         requests.delete(url=base_url + 'books/' + str(book['id']) + '/')
#     request.addfinalizer(fin)
#     return book

@pytest.fixture(scope="module")
def add_remove_book(base_url):
    book = {'title': 'Alice in Wonderland', 'author': 'Lewis Carroll'}
    r = requests.post(url=base_url + 'books/', data=book)
    book['id'] = r.json()['id']
    yield book
    requests.delete(url=base_url + 'books/' + str(book['id']) + '/')


@pytest.fixture(scope="function")
def add_remove_book_upd(base_url):
    book = {'title': 'Shantaram', 'author': 'Gregory David Roberts'}
    r = requests.post(url=base_url + 'books/', data=book)
    book.update([('id', r.json()['id'])])
    yield book
    requests.delete(url=base_url + 'books/' + str(book['id']) + '/')


@pytest.fixture(scope="function")
def add_remove_book_del(base_url):
    book = {'title': 'Anna Karenina', 'author': 'Leo Tolstoy'}
    r = requests.post(url=base_url + 'books/', data=book)
    book.update([('id', r.json()['id'])])
    yield book
    requests.delete(url=base_url + 'books/' + str(book['id']) + '/')

# Usual parametrization
# new_info = [{'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
#             {'title': '112233', 'author': '445566'},
#             {'title': '!£$%^()>?', 'author': '<>?@:}{^&'}]
# names_of_tests = ['letters', 'numbers', 'special symbols']
#
#
# @pytest.fixture(params=new_info, ids=names_of_tests, scope="function")
# def parametrization_upd(request):
#     new_book = request.param
#     yield new_book


# Parametrization with reading data from json file
with open('info.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

names_of_tests = ['letters', 'numbers', 'special symbols']


@pytest.fixture(params=data, ids=names_of_tests, scope="function")
def parametrization_upd(request):
    new_book = request.param
    yield new_book


@pytest.fixture(scope='function')
def remove_book_cre(base_url):
    book = {}
    yield book
    if 'id' in book.keys():
        requests.delete(url=base_url + 'books/' + str(book['id']) + '/')
