from abc import ABC, abstractmethod


class LibraryItem(ABC):

    def __init__(self, item_id, title):
        self.item_id = item_id
        self.title = title
        self._available = True

    @abstractmethod
    def loan_period_days(self):
        pass

    @property
    def available(self):
        return self._available

    def mark_borrowed(self):
        self._available = False

    def mark_returned(self):
        self._available = True

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "title": self.title,
            "available": self.available,
            "type": self.__class__.__name__
        }

class Book(LibraryItem):

    def loan_period_days(self):
        return 14


class Magazine(LibraryItem):

    def loan_period_days(self):
        return 7


class ReferenceBook(LibraryItem):

    def loan_period_days(self):
        return 0

class Member:

    def __init__(self, member_id, name, borrowing_limit):
        self.member_id = member_id
        self.name = name
        self.borrowing_limit = borrowing_limit
        self._active_loans = []

    @property
    def active_loans(self):
        return tuple(self._active_loans)

    @property
    def borrowed_count(self):
        return len(self._active_loans)

    def add_loan(self, item_id):
        if self.borrowed_count < self.borrowing_limit:
            self._active_loans.append(item_id)
        else:
            print("Borrowing limit reached!")

    def remove_loan(self, item_id):
        if item_id in self._active_loans:
            self._active_loans.remove(item_id)

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "borrowing_limit": self.borrowing_limit,
            "active_loans": self._active_loans,
            "type": self.__class__.__name__
        }


class StudentMember(Member):

    def __init__(self, member_id, name):
        super().__init__(member_id, name, borrowing_limit=3)


class FacultyMember(Member):

    def __init__(self, member_id, name):
        super().__init__(member_id, name, borrowing_limit=5)

class ResearchStudent(StudentMember):

    def __init__(self, member_id, name):
        super().__init__(member_id, name)
    def to_dict(self):
        return {
        "member_id": self.member_id,
        "name": self.name,
        "borrowing_limit": self.borrowing_limit,
        "active_loans": self._active_loans,
        "type": self.__class__.__name__
    }


class NotificationMixin:

    def send_notice(self, message):
        print(f"NOTIFICATION: {message}")


class NotifiedMember(Member, NotificationMixin):
    pass
