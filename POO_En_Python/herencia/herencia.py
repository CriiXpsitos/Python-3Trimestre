class Publicacion:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"


class Libro(Publicacion):
    def __init__(self, titulo, autor, paginas):
        super().__init__(titulo, autor)  
        self.paginas = paginas

    def __str__(self):
        return f"{super().__str__()}, Páginas: {self.paginas}"


# Creación de una instancia de la clase Libro (heredando de Publicacion)
libro_1 = Libro("El Alquimista", "Paulo Coelho", 208)

# Impresión usando el método __str__ de la subclase Libro
print(str(libro_1))  # Imprime la representación de cadena del libro, incluyendo título, autor y páginas

# Llama al método __init__ de la superclase Publicacion
