import time  # Importa el módulo 'time' para manejar operaciones relacionadas con el tiempo

# Define una función para agregar una novedad
def agregar_novedad(id, fecha, descripcion, equipo):
    novedad = {
        "id": id,
        "fecha": fecha,
        "descripcion": descripcion,
        "equipo": equipo
    }
    return novedad

# Define una función para registrar un equipo de cómputo
def registrar_equipo(id, nombre, cargador, mouse):
    equipo = {
        "id": id,
        "nombre": nombre,
        "cargador": cargador,
        "mouse": mouse
    }
    return equipo

# Define una función para generar un reporte de novedades asociadas a un equipo específico
def reporte_novedades_por_equipo(id_equipo, novedades):
    novedades_equipo = []
    for novedad in novedades:
        if novedad["equipo"] == id_equipo:
            novedades_equipo.append(novedad)
    return novedades_equipo

# Define una función para buscar un equipo por su ID
def buscar_equipo_por_ID(id, equipos_computo):
    for equipo in equipos_computo:
        if equipo["id"] == id:
            return equipo
    return None

# Define una función para eliminar equipos por su ID
def eliminar_equipos(id, equipos_computo):
    equipo = None
    for e in equipos_computo:
        if e["id"] == id:
            equipo = e
            break
    if equipo:
        equipos_computo.remove(equipo)
        print("El equipo con ID", id, "ha sido eliminado correctamente")

# Define una función para actualizar la información de un equipo por su ID
def actualizar_equipo(id, nuevo_nombre, nuevo_cargador, nuevo_mouse, equipos_computo):
    equipo = None
    for e in equipos_computo:
        if e["id"] == id:
            equipo = e
            break
    if equipo:
        equipo["nombre"] = nuevo_nombre
        equipo["cargador"] = nuevo_cargador
        equipo["mouse"] = nuevo_mouse
        print("Se ha actualizado el equipo con éxito.")
    else:
        print("No se encontró el equipo a actualizar")

# Inicialización de listas y variables
novedades = []
equipos_computo = []
vacio = True

# Bucle principal del programa
while True:
    # Menú de opciones
    print("Opciones \n 1. Agregar equipo \n 2. Mostrar lista de equipos \n 3. Menú de novedades \n 4. Buscar equipo por ID \n 5. Eliminar equipo y novedades por ID \n 6. Actualizar equipo por ID \n 7. Salir")
    opcion = input("Agrega una de las opciones \n Esperando Opcion: ")
    opcion = opcion.strip()

    # Opción 1: Agregar equipo
    if opcion == "1":
        id = int(input("Ingrese el ID del equipo: "))
        nombre = str(input("Ingrese el nombre del equipo: "))
        cargador = input("Ingrese el cargador del equipo: ")
        mouse = input("Ingrese el mouse del equipo: ")
        equipo = registrar_equipo(id, nombre, cargador, mouse)
        equipos_computo.append(equipo)
        vacio = False

    # Opción 2: Mostrar lista de equipos
    elif opcion == "2":
        if vacio == False:
            print("Lista de equipos de cómputo:")
            for i, equipo in enumerate(equipos_computo):
                print(f"{i + 1}. ID: {equipo['id']}, Nombre: {equipo['nombre']}, Cargador: {equipo['cargador']}, Mouse: {equipo['mouse']}")
                time.sleep(2)

    # Opción 3: Menú de novedades
    elif opcion == "3":
        if vacio == False:
            while True:
                print("Bienvenido al menú de novedades \n 1. Agregar novedades \n 2. Consultar novedades \n 0. Para salir")
                opcion = int(input("Ingrese una opción: "))

                if opcion == 0:
                    print("Saliendo...")
                    time.sleep(2)
                    break

                # Submenú de agregar novedades
                elif opcion == 1:
                    if vacio == False:
                        id = int(input("Agregue el ID del computador afectado: "))
                        fecha = input("Fecha de la novedad: ")
                        descripcion = input("Descripción de la novedad: ")
                        equipo = input("Equipo afectado por la novedad: ")
                        novedad = agregar_novedad(id, fecha, descripcion, equipo)
                        novedades.append(novedad)
                        time.sleep(2)

                # Submenú de consultar novedades
                elif opcion == 2:
                    if not vacio:
                        id = int(input("Ingrese el ID del equipo que desea buscar: "))
                        print("Novedades relacionadas al equipo con ID", id)
                        novedades_encontradas = False  # Variable para controlar si se encontraron novedades
                        for i, novedad in enumerate(novedades):
                                print("ID Novedad: ", novedad["id"], "\t Descripción: ", novedad["descripcion"])
                                time.sleep(2)

                    else:
                        print("La base de datos está vacía.")
                        time.sleep(2)

                else:
                    print("Opción no válida.")

    # Opción 4: Buscar equipo por ID
    elif opcion == "4":
        if vacio == False:
            id = int(input("Ingrese el ID del equipo a buscar: "))
            equipo = buscar_equipo_por_ID(id, equipos_computo)
            if equipo != None:
                print(f"Nombre: {equipo['nombre']}, Cargador: {equipo['cargador']}, Mouse: {equipo['mouse']}")
                time.sleep(2)
        else:
            print("La base de datos está vacía.")
            time.sleep(2)

    # Opción 5: Eliminar equipo y novedades por ID
    elif opcion == "5":
        if vacio == False:
            id = int(input("Ingrese el ID del equipo a eliminar: "))
            eliminar_equipos(id, equipos_computo)
        else:
            print("La base de datos está vacía.")
            time.sleep(2)

    # Opción 6: Actualizar equipo por ID
    elif opcion == "6":
        if vacio == False:
            id = int(input("Ingrese el ID del equipo a actualizar: "))
            nuevo_nombre = input("Nuevo nombre del equipo: ")
            nuevo_cargador = input("Nuevo estado del cargador: ")
            nuevo_mouse = input("Nuevo estado del mouse: ")
            actualizar_equipo(id, nuevo_nombre, nuevo_cargador, nuevo_mouse, equipos_computo)
            time.sleep(2)
        else:
            print("La base de datos está vacía")
            time.sleep(2)

    # Opción 7: Salir
    elif opcion == "7":
        print("HASTA LUEGOOOOOOOOOOOOOOOOOOO")
        break

    # Opción inválida
    else:
        print("Opción inválida, por favor ingrese una opción válida.")
        time.sleep(2)
