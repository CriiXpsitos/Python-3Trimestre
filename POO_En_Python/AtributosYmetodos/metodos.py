#creamos una clase llamada calculadora 
class Calculadora:
    #donde obtienes unos metodos con atributos a y b
    #este es el metodo de sumar donde retorna las suma de los atributos
    def suma(a, b):
        return a + b

    #aca creamos el metodo de restar donde principlmente como su nombre lo indica restamos los parametros a y b
    def resta(a, b):
        return a - b
    #aca creamos el metodo de multiplicacion donde principlmente como su nombre lo indica multiplicamos los parametros a y b
    def multiplicacion(a, b):
        return a * b
    
    ##aca creamos el metodo de division donde principlmente como su nombre lo indica dividimos los parametros a y b
    def division(a, b):
        #aca tenemos un condicional si donde b es indiferente de 0 entonces pra retonar la division de los parametros
        if b != 0:
            return a / b
        #de lo contrario no se va a poder dividir
        else:
            return "No es posible dividir por cero"

# Ejemplo de uso donde primero que todo, tenemos una instancia llamado resultado_suma y se le agrega el metodo
resultado_suma = Calculadora.suma(5, 3)
print("Suma:", resultado_suma)  # Imprime: Suma: 8

#aqui hacemos exactamente lo mismo pero llamando el metodo de restar poniendole los atributos de 10 y 4
resultado_resta = Calculadora.resta(10, 4)
print("Resta:", resultado_resta)  # Imprime: Resta: 6
#aqui hacemos lo mismo pero llamando el otro metodo de multiplicacion y poniendole dentro de un instancia y agregandole los argumentos 7 y 2 a los parametros
resultado_multiplicacion = Calculadora.multiplicacion(7, 2)
print("Multiplicación:", resultado_multiplicacion)  # Imprime: Multiplicación: 14
#aqui hacemos exactamente lo mismo pero llamando el metodo de division con sus argumentos de 9 y 3
resultado_division = Calculadora.division(9, 3)
print("División:", resultado_division)  # Imprime: División: 3.0

#aca volvemos a llamar al metodo pero dejandole al parametro en b que sea igual a 0 para no poder dividir
resultado_division_cero = Calculadora.division(10, 0)
print("División por cero:", resultado_division_cero)  # Imprime: División por cero: No es posible dividir por cero
