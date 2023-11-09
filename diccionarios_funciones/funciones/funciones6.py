#aca se crea una funcion llamada compra donde se le asigna unos parametros
#que son, la marca, la cantidad y el valor
def compra(marca,cantidad,valor):
 #se les retorna apartir de un diccionario y cada parametro se le agrega al diccionario
 return dict(
 marca=marca,
 cantidad=cantidad,
 valor=valor*cantidad
 )
#se imprime y se llama la funcion y se le agrega valores al diccionario de forma posicional
print(f' lo comprado fue:{compra("AMD",3,2500000)}')
