#crea una funcion donde se le pone los parametros y deja uno fijo con un valor
def compra(marca, cantidad, valor=2500000):
    # Returna el resultado del diccionario
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor * cantidad
    )
#aca se llama la funcion la imprime le asigna los valores a la funcion y de una vez pone el valor sabiendo que no 
#tenemos que darle un valor sabiendo que esta fijo
print(f' lo comprado fue:{compra("AMD",3)}')