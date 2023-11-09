def valorVocal(vocal):
    vocales = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    for i in range(len(vocales)):
        if vocal == vocales[i]:
            return vocales.index(vocal)
        else:
            return -1
            
#vocales con input y si esta devuelve true y si no esta devuelve false con input
vocal1 = str(input("ingrese una vocal: "))
print("True" if valorVocal(vocal1) >= 0 else "False")
