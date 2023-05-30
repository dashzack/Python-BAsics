list=[]
numero=int(input("ingrese un numero:"))

while numero>0:
    numero=int(input("ingrese un numero:"))
    
    if numero<=0:
        print("numero no valido")
    else:
        list.append(numero)

print(list)
