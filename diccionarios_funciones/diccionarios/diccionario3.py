
#aca hay dos formas de iterar en un diccionario
calificaciones = {
 'nombre': 'Sandra',
 'notafinal': 5.0
 }
calificaciones = {
 'Sandra': 5.0,
 'Adriana':5.0,
 'Mauricio':4.5,
 'Jose':2.5
 }

#y como las listas... se hace un for in range... pero se le da dos variables
#j e i... ya que uno accede a las claves y el otro a los valores
for i, j in calificaciones.items():
 print(i, j)

