class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Páginas: {self.paginas}"

    def __len__(self):
        return self.paginas
    def __del__(self):
        print(f'Se ha eliminado el libro "{self.titulo}".')

# Creación de un objeto de la clase Libro
libro_1 = Libro("El Alquimista", "Paulo Coelho", 208)

# Impresión usando el método __str__
print(str(libro_1))  # Imprime la representación de cadena del libro

# Obtención de la longitud usando el método __len__
print(len(libro_1))  # Imprime la cantidad de páginas del libro
# Eliminación del libro (llamada al destructor __del__)
del libro_1

# Comentarios:
# __init__ es el constructor que inicializa los atributos de la clase.
# __str__ devuelve una representación de cadena de la instancia.
# __len__ devuelve la longitud o algún valor asociado a la instancia (en este caso, la cantidad de páginas del libro).
# __del__ borra la informacion de l memoria 
