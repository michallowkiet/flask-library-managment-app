class Category:
    def __init__(self, name):
        self.id = -1
        self.name = name


class Client:
    def __init__(self, first_name, last_name):
        self._id = -1
        self.first_name = first_name
        self.last_name = last_name

    @property
    def id(self):
        return self._id


class Book:
    def __init__(self, isbn, name, description, is_loaned, author_id, category_id):
        self.id = -1
        self.isbn = isbn
        self.name = name
        self.description = description
        self.is_loaned = is_loaned
        self.author_id = author_id
        self.category_id = category_id


class BookCategory:
    def __init__(self, book_id, category_id):
        self.book_id = book_id
        self.category_id = category_id


class ClientBook:
    def __init__(self, client_id, book_id, loan_date, return_date):
        self.client_id = client_id
        self.book_id = book_id
        self.loan_date = loan_date
        self.return_date = return_date
