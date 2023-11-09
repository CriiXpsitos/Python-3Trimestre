def max_de_tres( n1, n2, n3):

    if  n1 > n2 and  n1 >n3:
        return n1
    elif n2> n1 and n2>n3:
        return n2
    else:
        return n3
    
n1 = float(input("ingrese el numero 1: \n"))
n2 = float(input("Ingrese el numero 2: \n"))
n3 = float(input("ingrese el numero 3: \n"))

print (f"el numero maximo es el {max_de_tres(n1,n2,n3)}")


