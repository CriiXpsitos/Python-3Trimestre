#aca se hace el diccionario

calificaciones = {
 'Sandra': 5.0,
 'Adriana':5.0,
 'Mauricio':4.5,
 'Jose':2.5
 }

#aca se imprimen como su nombre lo indican las claves 
print("Técnicas por clave")
for i in calificaciones.keys():
 print(i)
#y aca se extrae los valores de las claves correspondientes
print("Iterar por valor")
for j in calificaciones.values():
 print(j)