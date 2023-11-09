# Crea una función llamada `operadorand` que toma dos números como argumentos y devuelve el resultado de la operación AND bit a bit entre ellos.
operadorand = lambda x, y: x & y

# Usa un bucle `for` para iterar desde 0 hasta 1.
for i in range(2):

    # Usa otro bucle `for` para iterar desde 0 hasta 1.
    for j in range(2):

        # Imprime el resultado de la operación AND bit a bit entre `i` y `j`.
        print(f"{i} & {j} = {operadorand(i, j)}")

