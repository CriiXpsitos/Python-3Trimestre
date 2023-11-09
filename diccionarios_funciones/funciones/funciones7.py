#aca se hace lo mismo que el archivo pasado
def compra(marca,cantidad,valor):
 return dict(
 marca=marca,
 cantidad=cantidad,
 valor=valor*cantidad
 )
#con la unica novedad que estos son parametro nominales donde se les asigna el valor explicitamente en el print
print(f' lo comprado fue:{compra(marca="AMD",cantidad=3,valor=2500000)}')