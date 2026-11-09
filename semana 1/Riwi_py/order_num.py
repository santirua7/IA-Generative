n1 = input("ingrese primer numero: \n")
n2 = input("ingrese segundo numero: \n")
n3 = input("ingrese tercer numero: \n")

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if n1 < n2 and n1 < n3:
    if n2 < n3:
        print("el numero es:", n1, n3, n2)
elif n2 < n1 and n2 < n3:
    print("los numeros son:", n2, n1, n3)
elif n3 < n1:
    print("los numeros son:", n2, n3, n1)
elif n3 < n2 and n3 < n1:
    print("los numeros son:", n3, n1, n2)
else:
    print("los numeros son:", n3, n2, n1)


print("listo")
