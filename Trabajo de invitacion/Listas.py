import time
aprendices_edades = [['Sebastian Tovar', 'Juan Mahecha', 'Maria Buenaventura', 'Mathew Guarnizo', 'Kevin Hernan', 'Melissa Lopez', 'Vanesa Ladino', 'Stiven Ramirez', 'Esteban Prada', 'Kevin Botero', 'Sebastian Pinzon', 'Camila Alape', 'Kevin Londoño', 'Nicolas Fierro', 'Santiago Gomez', 'Marlon Lopez ', 'Stiwar Perez', 'Miguel Bernal', 'Maria Molano', 'Nicolas Paulo', 'Laura Benavides', 'Wilfrank', 'Dahiana', 'Nataly', 'Maria José', 'Cristian Peña', 'Paula', 'Kevin Eduardo', 'Yency', 'Matias Guzman'],
                      [17, 17, 17, 17, 17, 17, 17, 18, 17, 17, 17, 18, 23, 18, 18, 19, 18, 17, 18, 17, 17, 18, 18, 18, 18, 18, 18, 18, 18, 18]]




print("----------------APRENDICES---------------------------")
for nombre, edad in zip(aprendices_edades[0], aprendices_edades[1]):
    print(f"Nombre: {nombre} Edad: {edad}")

#aprendices_edades >= 18

print("------------APRENDICES MAYORES DE 18--------------")
for nombre, edad in zip(aprendices_edades[0], aprendices_edades[1]):
    if edad >= 18:
        print(f" Personas con mayor de 18 años \n Nombre: {nombre} Edad: {edad}") 

#poner el nombre de la instructora en el primero

aprendices_edades[0].insert(0, "Adriana lucia rincon Forero" )
    
print("----------------INSTRUCTORA---------------------------")
print(aprendices_edades [0])

#aprendices_edad[1] max age

edadMax=max(aprendices_edades[1])
print("---------- la edad maxima es ------------")
print(edadMax)


# cuantos aprendices tienen 18 

print("---------- cuantas personas con 18 hay?-----------")
conteoEdad18 = print(aprendices_edades[1].count(18))

#agregar una persona random al final
print("--------- estudiante al final de la lista---------------------")
aprendices_edades[0].remove("Matias Guzman")
aprendices_edades[0].append("Matias Guzman")

print(aprendices_edades[0])

#eliminar a la instructora 

aprendices_edades[0].remove("Adriana lucia rincon Forero")
print("------- INSTRUCTORA ELIMINADA CON EXITO -----------")
print(aprendices_edades[0])

#Indique un dato a buscar en la lista de aprendices

print("-------------- persona encontrada en el indice ----------------")
datoABuscar="Sebastian Tovar" 
if datoABuscar in aprendices_edades[0]:
    indiceDatoBuscado=aprendices_edades[0].index(datoABuscar)
    print ("El dato fue encontrado en la posicion",indiceDatoBuscado+1,"de la lista.")

#Mostrar los primeros 10 datos de la lista 
print("------PRIMEROS 10 DATOS DE LA LISTA----")
print (aprendices_edades[0][:10])

#Mostrar los 10 ultimos datos de la lista
print("------ULTIMOS 10 DATOS DE LA LISTA----")
print (aprendices_edades[0][-10:])

#Mostrar del elemento 10 al elemento 20
print("------DEL 10 AL 20----")
print (aprendices_edades[0][9:20])

