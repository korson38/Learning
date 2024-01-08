# task 1


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_grades = sum(self.marks) / sum(self.name)
        return average_grades


stud1 = Student("Walo", [50, 60, 70, 80])
stud2 = Student("Spejson", [30, 30, 50, 45])
res1 = stud1.is_passed()
res2 = stud2.is_passed()
# task 2


class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library: \n City: {self.city} Street: {self.street}  " \
               f"zip_code: {self.zip_code} open hours: {self.open_hours}" \
               f"phone: {self.phone}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self. last_name = last_name
        self.hire_date = hire_date
        self. birth_date = birth_date
        self. city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        f"Employee: {self.first_name} {self.last_name} \nhire date: {self.hire_date} birth date: {self.birth_date}" \
        f"City: {self.city} Street: {self.street} \nzip code: {self.zip_code} phone: {self.phone}"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book:\n Library: {self.library} publication date: {self.publication_date}" \
               f"Author: {self.author_name} {self.author_surname}" \
               f"number of pages: {self.number_of_pages}"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_Date = order_date

    def __str__(self):
        book_list = "\n".join([f"  - {book}" for book in self.books])
        return f"Order: Prepared by: {self.employee} Student: {self.student} books: {book_list} Order date: {self.order_Date}"


library1 = Library("City1", "Street1", "12345", "9 AM - 6 PM", "123-456-789")
library2 = Library("City2", "Street2", "67890", "10 AM - 7 PM", "987-654-321")
employee1 = Employee("John", "Doe", "2022-01-01", "1990-05-15", "City1", "Street1", "12345", "555-1234")
employee2 = Employee("Jane", "Smith", "2022-02-01", "1985-08-20", "City2", "Street2", "67890", "555-5678")
employee3 = Employee("Bob", "Johnson", "2022-03-01", "1995-03-10", "City1", "Street1", "12345", "555-4321")
book1 = Book(library1, "2021-01-01", "Author1", "Surname1", 200)
book2 = Book(library1, "2021-02-01", "Author2", "Surname2", 250)
book3 = Book(library2, "2021-03-01", "Author3", "Surname3", 180)
book4 = Book(library2, "2021-04-01", "Author4", "Surname4", 300)
book5 = Book(library1, "2021-05-01", "Author5", "Surname5", 220)
order1 = Order(employee1, "Student1", [book1, book2, book3], "2022-04-01")
order2 = Order(employee2, "Student2", [book4, book5], "2022-05-01")

print(order1)
print("\n----------------------\n")
print(order2)


# ZAD 3
class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property: {self.area} sq. meters, {self.rooms} rooms\nPrice: ${self.price}\nAddress: {self.address}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House\n{super().__str__()}\nPlot Size: {self.plot} sq. meters"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat\n{super().__str__()}\nFloor: {self.floor}"


house = House(200, 4, 250000, "123 Main St", 500)
flat = Flat(100, 2, 120000, "456 Side St", 3)
print(house)
print("\n----------------------\n")
print(flat)
