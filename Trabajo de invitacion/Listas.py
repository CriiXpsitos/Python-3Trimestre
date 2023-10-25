import time
aprendices_edades = [[], []]


confirmacion = input("¿Iniciar verificación? \n")

while confirmacion.lower() == "si":
    print("Vamos a agregar los nombres y la edades de los aprendices")
    time.sleep(1)
    
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    
    aprendices_edades[0].append(nombre)
    aprendices_edades[1].append(edad)
    
    confirmacion = input("¿Desea continuar? (si/no): ")
    
    if confirmacion.lower()!= "si":
        break

print("----------------APRENDICES---------------------------")
for nombre, edad in zip(aprendices_edades[0], aprendices_edades[1]):
    print(f"Nombre: {nombre} Edad: {edad}")

#aprendices_edades >= 18

print("------------APRENDICES MAYORES DE 18--------------")
for nombre, edad in zip(aprendices_edades[0], aprendices_edades[1]):
    if edad >= 18:
        print(f" Personas con mayor de 18 años \n Nombre: {nombre} Edad: {edad}") 



    