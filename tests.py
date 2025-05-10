from main import BooksCollector
import data
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    # def test_add_new_book_add_two_books(self):
    #     # создаем экземпляр (объект) класса BooksCollector
    #     collector = BooksCollector()

    #     # добавляем две книги
    #     collector.add_new_book('Гордость и предубеждение и зомби')
    #     collector.add_new_book('Что делать, если ваш кот хочет вас убить')

    #     # проверяем, что добавилось именно две
    #     # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
    #     assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize(
        "book_name,result", ([data.books_name[0], 1], [data.books_name[1], 0])
    )
    def test_add_new_book_added_one_book(self, books_collector, book_name, result):
        collector = books_collector
        collector.add_new_book(book_name)
        assert len(collector.books_genre) == result

    def test_set_book_genre_assign_genre_to_book(self, books_collector_w_one_book_name):
        collector = books_collector_w_one_book_name
        collector.set_book_genre(data.books_name[0], data.books_genre[1])
        assert collector.books_genre.get(data.books_name[0]) == data.books_genre[1]

    def test_get_book_genre_success(self, books_collector_w_one_book_and_genre):
        collector = books_collector_w_one_book_and_genre
        assert collector.get_book_genre(data.books_name[0]) == data.books_genre[1]

    def test_get_books_with_specific_genre_success(
        self, books_collector_w_one_book_and_genre
    ):
        collector = books_collector_w_one_book_and_genre
        assert len(collector.get_books_with_specific_genre(data.books_genre[1])) == 1

    def test_get_books_genre_success(self, books_collector_w_one_book_and_genre):
        collector = books_collector_w_one_book_and_genre
        assert len(collector.get_books_genre()) == 1

    def test_get_books_for_children_success(
        self, books_collector_w_one_book_and_genre_for_children
    ):
        collector = books_collector_w_one_book_and_genre_for_children
        assert len(collector.get_books_for_children()) == 1

    def test_add_book_in_favorites_success(self, books_collector_w_one_book_name):
        collector = books_collector_w_one_book_name
        collector.add_book_in_favorites(data.books_name[0])
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_success(
        self, books_collector_w_one_book_name_in_favorites
    ):
        collector = books_collector_w_one_book_name_in_favorites
        collector.delete_book_from_favorites(data.books_name[0])
        assert len(collector.favorites) == 0

    def test_get_list_of_favorites_books_success(
        self, books_collector_w_one_book_name_in_favorites
    ):
        collector = books_collector_w_one_book_name_in_favorites
        assert len(collector.get_list_of_favorites_books()) == 1
