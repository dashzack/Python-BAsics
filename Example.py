#crear lista
lista=[1,5,25,100,500]

print("inicial :",lista)

#comando append/agregar objeto o dato al final de la lista

lista.append(250)
print("Append:",lista)

#comando extend/toma una segunda lista y agrega sus datos al final

lista2=[75,125]
lista.extend(lista2)
print("Extend: ",lista)

#comando insert, permite poner un elemento en poscicion determinada

lista.insert(2,400)
print("Insert: ",lista)


#comando remove, permite eliminar un dato de la lista

lista.remove(400)
print("Remove: ",lista)

# comando pop, elima el ultimo numero de la lista/sin embargo si le entregas un valor elimina la poscicion que le diste

lista.pop()
print("Pop: ", lista)

#comando reverse invierte la lista [1,2,3]-> [3,2,1]

lista.reverse()
print("Reverse :",lista)

#comando sort, ordena de mayor a menos

lista.sort()
print("reverse", lista)

#comando sort

lista.sort(reverse=True)
print("Sort(reverse=True):", lista)
