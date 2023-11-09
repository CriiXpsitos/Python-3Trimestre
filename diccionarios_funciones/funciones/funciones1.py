#aca se crea una funcion llamada saludar 
def saludar():
 print("saludo")

#aca se crea una funcion que retorne un numero
def retornarnumero():
 return 1
#aca llamamos la funcion saludar y e imprime "saludo"
saludar()
#aca retorna un numero sea en este caso 1
retornarnumero()

#aca se hace una condicional donde si es igual e igual a 1... imprime que si se deovlvio el 1.. si no, imprimira otra cosa
if retornarnumero()==1:
 print("devolvió un uno")
else:
 print("No devolvió un uno")