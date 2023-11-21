#Importa la biblioteca de tiempo
import time

#creamos una lista llamado equipos_computo... donde mas adelante vamos a agregar los equipos de computo correspondidos 
equipos_computo = []

#creamos una clase llamado Equipos
class Equipos:
    #donde creamos un metodo constructor donde va a tener unos parametros llamados... id, nombre, cargador y mouse... al principio ponemos el self para ponerloen los diferentes metodos
    def __init__(self, id, nombre, cargador, mouse):
        self.id = id
        self.nombre = nombre
        self.cargador = cargador
        self.mouse = mouse
        self.novedades = []  # creamos un atributo donde se puede usar en diferente metodos donde se crea una lista llamada novedades... donde se le agrega las novedades correspondiente

    #creamos un metodo donde nos dejen ver en forma de lista los equipos de computo 
    def mostrar_lista_de_equipos(self):
        #creamos un bucle llamado equipo dentro la lista equipos de computo... donde va imprimir todo... como el nombre, id, cargador y mouse
        for equipo in equipos_computo:
            print("ID del equipo: ", equipo.id)
            print("Nombre del equipo: ", equipo.nombre)
            print("Cargador del equipo: ", equipo.cargador)
            print("Mouse del equipo: ", equipo.mouse, "\n")
    #creamos un metodo que se deje registrar los equipos de computo
    def registrar_equipo(self):
        print("Registrando Equipo")
        #creamos una variable llamado equipo_nuevo donde llamamos la clase de equipo y traemos todos los atributos del constructor
        equipo_nuevo = Equipos(self.id, self.nombre, self.cargador, self.mouse)
        #donde al final se le agrrega a la lista vacia 
        equipos_computo.append(equipo_nuevo)
    
    #creamos un metodo donde puedo darle los reportes de los equipos... donde va a hacer el bucle en la lista... donde si
    #si el equipo de la lista de equipos de computo es == (igual igual) al self.id del id constructor 
    def reporte_novedades_por_equipo(self):
        for equipo in equipos_computo:
            if equipo.id == self.id:
                #si es asi se retorna el siguiente print
                return f"El Equipo con id: {equipo.id} \nIdentificado con el Nombre del equipo: {equipo.nombre}\nCon el Cargador: {equipo.cargador}\nProblema con el Mouse: {equipo.mouse}"
        return "Equipo no encontrado o sin novedades."
    #aca creamos un metodo donde podamos registrar las novedades de los equipos... y pasando los parametros del atributo novedad
    def registrar_novedad(self, novedad):
        #se crea una nueva variable lalmada timestap... donde se le pone un metodo gracias a la biblioteca time... algo nuevo que aprendi y es que 
        #las novedades van a tener la fecha, mes, dia, hora, minutos y segundos de la actualidad
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        #y al atributo que es una lista se le agrega la fecha y la novedad correspondiente 
        self.novedades.append({"fecha": timestamp, "novedad": novedad})
    #aca se crear un metodo donde se muestran las novedades 
    def mostrar_novedades(self):
        #si existe esa novedad va a imprimir el siguiente texto
        if self.novedades:
            print(f"Novedades para el equipo con ID {self.id}:")
            #a la vez que crea un bucle para poner las novedades de fecha y novedad de un diccionario
            for novedad in self.novedades:
                print(f"Fecha: {novedad['fecha']}, Novedad: {novedad['novedad']}")
        else:
            print("No hay novedades registradas para este equipo.")
    #aca creamos un metodo donde obtenemos los equipos por id
    def obtener_equipo_por_id(id_equipo):
        #donde creamos un bucle para saber si equipo.id es igual al prametro de input de mas adelante que es id_equipo
        for equipo in equipos_computo:
            if equipo.id == id_equipo:
                #si es asi... retorna el equipo que estamos buscando y si no... no retorna nada 
                return equipo
        return None
    #aca creamos un metodo donde eliminamos el equipo correspondiente 
    def eliminar_equipo(self):
        #donde creamos un bucle donde enumere gracias al indice y el equipo... en equipos de computo
        for i, equipo in enumerate(equipos_computo):
            #a la vez que si el equipo.id es igual al self.id
            if equipo.id == self.id:
                #se borra de equipos de computo en el indice exacto el id y todo lo referente 
                del equipos_computo[i]
                break
    #aca creamos otro metodo... donde actualizamos el equipo con los nuevos parametros 
    def actualizar_equipo(self, nuevo_nombre, nuevo_cargador, nuevo_mouse):
        #aca creamos un bucle para los equipo computo
        for equipo in equipos_computo:
            #en caso de ser el mismo equipo
            if equipo.id == self.id:
                #actualiza su nombre, cargador y mouse
                equipo.nombre = nuevo_nombre
                equipo.cargador = nuevo_cargador
                equipo.mouse = nuevo_mouse
                break
#aca se muestra una funcion que es la de crear un menu 
def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Mostrar lista de equipos")
    print("2. Registrar un nuevo equipo")
    print("3. Generar reporte de novedades por equipo")
    print("4. Buscar equipo por ID")
    print("5. Eliminar equipo por ID")
    print("6. Actualizar información de un equipo por ID")
    print("7. Salir")

# Función para ejecutar el programa
def ejecutar_programa():
    while True:
        mostrar_menu()  # Muestra el menú de opciones al usuario
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Opción para mostrar la lista de equipos existentes
            equipo = Equipos("", "", "", "")
            equipo.mostrar_lista_de_equipos()

        elif opcion == "2":
            # Opción para registrar un nuevo equipo solicitando información al usuario
            id_equipo = input("Ingrese ID del equipo: ")
            nombre_equipo = input("Ingrese nombre del equipo: ")
            cargador_equipo = input("Ingrese tipo de cargador: ")
            mouse_equipo = input("Ingrese tipo de mouse: ")
            equipo = Equipos(id_equipo, nombre_equipo, cargador_equipo, mouse_equipo)
            equipo.registrar_equipo()

        elif opcion == "3":
            # Menú para manejar las novedades de los equipos
            while True:
                opcion_novedades = input("Bienvenido al Menú de las novedades... ¿qué quieres hacer?\n1. Registrar la novedad del equipo\n2. Buscar las novedades de los equipos\n3. Volver al menú principal\nOpción: ")
                if opcion_novedades == '1':
                    # Opción para registrar una nueva novedad en un equipo específico
                    id_equipo = input("Ingrese ID del equipo para registrar novedad: ")
                    novedad = input("Ingrese la novedad a registrar: ")
                    equipo = Equipos.obtener_equipo_por_id(id_equipo)
                    if equipo:
                        equipo.registrar_novedad(novedad)
                        print("Novedad registrada correctamente.")
                    else:
                        print("Equipo no encontrado")

                elif opcion_novedades == '2':
                    # Opción para mostrar las novedades de un equipo específico
                    id_equipo = input('Ingrese ID del equipo que busca la novedad: ')
                    equipo = Equipos.obtener_equipo_por_id(id_equipo)
                    if equipo:
                        equipo.mostrar_novedades()
                    else:
                        print("No se ha registrado ninguna novedad en este equipo.")

                elif opcion_novedades == '3':
                    # Vuelve al menú principal
                    break
                else:
                    print("Opción inválida.")

        elif opcion == "4":
            # Opción para buscar un equipo por su ID y mostrar su reporte de novedades
            id_equipo = input("Ingrese ID del equipo a buscar: ")
            equipo = Equipos.obtener_equipo_por_id(id_equipo)
            if equipo:
                print("Equipo encontrado:")
                print(equipo.reporte_novedades_por_equipo())
            else:
                print("Equipo no encontrado.")

        elif opcion == "5":
            # Opción para eliminar un equipo por su ID
            id_equipo = input("Ingrese ID del equipo a eliminar: ")
            equipo = Equipos.obtener_equipo_por_id(id_equipo)
            if equipo:
                equipo.eliminar_equipo()
                print("Equipo eliminado, si existía.")
            else:
                print("Equipo no encontrado.")

        elif opcion == "6":
            # Opción para actualizar la información de un equipo por su ID
            id_equipo = input("Ingrese ID del equipo a actualizar: ")
            nuevo_nombre = input("Ingrese nuevo nombre: ")
            nuevo_cargador = input("Ingrese nuevo cargador: ")
            nuevo_mouse = input("Ingrese nuevo tipo de mouse: ")
            equipo = Equipos.obtener_equipo_por_id(id_equipo)
            if equipo:
                equipo.actualizar_equipo(nuevo_nombre, nuevo_cargador, nuevo_mouse)
                print("Información del equipo actualizada, si existía.")
            else:
                print("Equipo no encontrado.")

        elif opcion == "7":
            # Opción para salir del programa
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Inicializamos el programa
ejecutar_programa()
