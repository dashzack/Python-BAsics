lista=[]

numero=int(input("ingrese un numero: "))

for i in range (1,11):
    #random.randint(A;B) genera un numero aleatorio entre el rango a hasta b
    #print (random.radiant(1,500))
    lista.append(numero*i)
print(lista)
