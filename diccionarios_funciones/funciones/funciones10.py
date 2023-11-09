#aca se crea una variable llamada numero_palabras donde se crea una funcion lambda
#se le asigna el parametro t y esto es igual a que se lea, divida cada espacio y elimine el espaciado en cada elemento
numero_palabras = lambda t: len(t.strip().split())
#aca se llama a la función y se le pasa el texto que queremos contar las palabras 

print(numero_palabras("hola, esto es una prueba con lambda"))
