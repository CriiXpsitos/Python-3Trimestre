#se crea una clase llamada libro donde tiene el "pass" que es una sentencia que no hace absolutamente nada 
class Libro:
    pass

# Creamos una instancia que dentro de la  variable va a contener la clase de libro 
libro_1 = Libro()
#aca ponemos los atributos correspondientes a la instancia del libro 1 que es
#titulo
libro_1.titulo = "El Alquimista"
#autor
libro_1.autor = "Paulo Coelho"
#isbn... identificacion del libro
libro_1.isbn = "9780062315007"
#el numero de paginas
libro_1.paginas = 208

# Aca usamos el ejemplo
print(libro_1.titulo)  # Imprime: El Alquimista
print(libro_1.autor)  # Imprime: Paulo Coelho
print(libro_1.isbn)  # Imprime: 9780062315007
print(libro_1.paginas)  # Imprime: 208
