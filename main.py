from models import Book, StudentMember
from library_service import LibraryManager
from storage import Storage

library = LibraryManager()

book = Book("B101", "Python Programming")
student = StudentMember("S101", "Rahul")

library.register_item(book)
library.register_member(student)

library.borrow_item("S101", "B101")
library.return_item("B101")
from models import StudentMember

student = StudentMember("S101", "Rahul")

print(student.to_dict())

print(book.available)
print(student.borrowed_count)


print(LibraryManager.max_active_loans_default)

LibraryManager.update_default_limit(5)

print(LibraryManager.max_active_loans_default)

