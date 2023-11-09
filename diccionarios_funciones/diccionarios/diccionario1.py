# se puede llamar un diccionario de dos formas... las que ven en estre codigo
diccionario = dict()
diccionario= {}
#se le puede dar al diccionario algunos valores como nombres y edades
Diccionario = {'nombre':'Sandra' , 'edad': 44}

#aca se pueden imprimir lo que esta adentro del diccionario... lo que se pida
#si la edad o el nombre como el siguiente ejemplo
print(Diccionario ['nombre']) #se imprime los nombres de los diccionarios
print(Diccionario ['edad']) #se imprime la edad

#aca se obtiene tambien los elementos del diccionario, sea nombre o edad
#si no existe... imprime "no existe"
print(Diccionario.get('oficio','No existe')) 


