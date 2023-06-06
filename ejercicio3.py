falta desarrollar
import random
import numpy as np

lista=[]

for i in range (9):
    lista.append(random.randint(0,100))

arr=np.array(lista).reshape((3,3))

print(arr)
print(f"EL promedio de la lista es de: {arr.mean()}")
print(f" El numero mas pequeño de la lista es: {arr.min()}")
print(f" El numero mas Grande de la lista es: {arr.max()}")
print(f" la suma de los numeros de la lista es: {arr.sum()}")
print("La diagonal es:")
print(arr[0,0])
print(arr[1,1])
print(arr[2,2])
