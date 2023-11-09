#creamos una funcion llamada lista... donde tiene dos parametros uno que se llama arg (argumento)
#otro llamado resultado donde se le pone fijo una lista
def lista(arg, result=[]):
 #aca a la lista resultado se le agrega todos los parametros de argumentos
 result.append(arg)
 #se imprime el resultado
 print(result)

#aca se llama la funcion y se le asigna los valores a los parametros
lista(' lunes' ' martes' ' miercoles' ' jueves' ' viernes' ' sabado' ' domingo' , [])

#aca se modifica los parametros de forma mutable del ejercicio anterior
def listalimpia(arg, result=None):
  if result is None:
    result = []
    result.append(arg)
    print(result)
listalimpia("a")
listalimpia("b") 