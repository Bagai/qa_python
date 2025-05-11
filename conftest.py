import pytest
import data
from main import BooksCollector

@pytest.fixture
def books_collector():
    return BooksCollector()


@pytest.fixture
def books_collector_w_one_book_name(books_collector):
    collector = books_collector
    collector.add_new_book(data.books_name[0])
    return collector


@pytest.fixture
def books_collector_w_one_book_and_genre(books_collector):
    collector = books_collector
    collector.add_new_book(data.books_name[0])
    collector.set_book_genre(data.books_name[0], data.books_genre[1])   
    return collector


@pytest.fixture
def books_collector_w_one_book_and_genre_for_children(books_collector):
    collector = books_collector
    collector.add_new_book(data.books_name[2])
    collector.set_book_genre(data.books_name[2], data.books_genre[3])   
    return collector


@pytest.fixture
def books_collector_w_one_book_name_in_favorites(books_collector):
    collector = books_collector
    collector.add_new_book(data.books_name[0])
    collector.add_book_in_favorites(data.books_name[0])
    return collector
