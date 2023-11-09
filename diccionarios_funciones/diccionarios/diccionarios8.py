
#aca se crea otra vez el diccionario de las calificaciones
calificaciones = {
 'Sandra': 5.0,
 'Adriana':5.0,
 'Mauricio':4.5,
 'Jose':2.5
 }

#aca se eleminina la clave jose de los items del diccionario como tambien su valor
#ya que el bucle lo que va hacer es iterar en las claves y valores del diccionario
del(calificaciones['Jose'])
for i, j in calificaciones.items():

 print(i,j)

