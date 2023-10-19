
#se importa el diccionario time 
import time


#se crea las listas con primero que todo... los invitados, los aceptados, los no aceptados, los menores de 18
lista_Invitado = ["Cristian", "Matias", "Joan"]
aceptados = []
no_aceptados = []
menores_18 = []


#hacemos un input para empezar con el codigo 
confirmacion = input("¿Iniciar verificación? \n")

#creamos un while donde acepta la confirmacion sea un "si" y dijitamos nuestro nombre
while confirmacion.lower() == "si":
    print("Bienvenido A la fiesta de disfraces de ADSO")
    time.sleep(1)
    
    conInvitado = input("Cual es su nombre? \n")
#creamos una condicion donde si los conInvidado este en lista_invitado entonces se imprime 
# y se va a la siguiente pregunta, cuantos años tiene 
    if conInvitado in lista_Invitado:
        print(f"Bien, Siguiente pregunta Joven {conInvitado}")
        time.sleep(1.2)
        edad = float(input("Ingresa Su edad: "))
      #aca miramos las condiciones, si es mayor de edad lo agrega en la lista de aceptados
      # y si no se pone en la lista de menores de 18   
        if edad >= 18:
            print("Bien Prosiga")
            aceptados.append(conInvitado)
        else:
            print("Lo siento, eres menor de 18 años, puedes entrar pero sin tomar alcohol")
            menores_18.append(conInvitado)

    #aca es si la persona que escribimos no esta en la lista presente, lo pone en la lista
    #de no invitados y no lo deja ingresar
    else:
        time.sleep(1)
        print(f"No Señor, usted no está en la lista de invitados")
        no_aceptados.append(conInvitado)
    
    #aca volvemos a pedir la confirmacion, por si ya no quiere seguir, y si la 
    #respuesta es diferente a si... se toma el break
    confirmacion = input("¿Desea continuar verificando? (si/no): ")
    
    if confirmacion.lower() != "si":
        break

#se imprimen a los aceptados, no aceptados y los menores de 18
print("Invitados aceptados:", aceptados)
print("No aceptados:", no_aceptados)
print("Menores de 18:", menores_18)
