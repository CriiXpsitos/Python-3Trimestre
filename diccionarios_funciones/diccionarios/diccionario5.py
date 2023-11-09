#aca se crean dos listas... nombres y edades
nombres = ['Maria', 'Sebastian', 'Ana']
edades = ['18', '25', '30']

#aca se crea un bucle donde se itera con n y e ya que este bucle lo que va a hacer
#es pasar todos los datos de las listas y los va a convertir en diccionario
#gracias al .format
for n, e in zip(nombres, edades):
 print('Tú nombre es {0} y tu edad {1}.'.format(n, e))