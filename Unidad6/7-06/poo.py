class Libro:
    def __init__(self, title, autor, pages, room) -> None:
        self.title = title
        self.autor = autor
        self.pages = pages
        self.room = room

    def show_data(self):
        return f'Titulo:{self.title}, Autor:{self.autor} Pages:{self.pages}'

    def get_pages(self):
        return self.pages


class Sala:
    def __init__(self, name, capacity) -> None:
        self.name = name
        self.capacity = capacity
        self.books = []

    def show_data(self):
        return f'Nombre sala: {self.name}'

    def addLibro(self, libro):  # este metodo recibe por parametro un objeto de tipo Libro
        self.books.append(libro)

    def addBook(self, title, autor, pages):  # este metodo recibe los atributos del libro
        libro = Libro(title, autor, pages)  # luego crea un objeto de tipo Libro
        self.books.append(libro)


class Biblioteca:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, name, capacity):
        sala = Sala(name, capacity)
        self.rooms.append(sala)

    def get_rooms(self):
        return [room.show_data() for room in self.rooms]


""" libro1 = Libro('Codigo Davinci', 'Brown', 200)


sala1 = Sala('Historia', 20)
sala2 = Sala('Matematicas', 5)
sala1.addBook('Fuego y sangre', 'George Martin', 1800)
sala1.addBook('Angeles y demonios', 'Dan Brown', 1980)

biblioteca1 = Biblioteca('Bibliotek')
biblioteca1.addSalas(sala1)
biblioteca1.addSalas(sala2)
 """
