#aca se crea una funcion donde valide si existe en este caso un parametro llamado objeto
def validarsiexiste(obj):
    #aca se le crea unas condicion si exste un objeto saldra true... si no false
    if obj:
        print(f"{obj} is True")
    else:
        print(f"{obj} is False")

#se llama la funcion
validarsiexiste(1)