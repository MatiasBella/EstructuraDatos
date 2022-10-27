#Crea lista random:
import random
#Opcion1:
'''lista = []
for i in range(10):
    i = random.randrange(0, 11)
    lista.append(i)'''
#Opcion2:
'''lista2 = []
for i in range(10):
    lista2.append(random.randrange(1, 20))
print(lista2)'''

#Ejercicio 1: Resuelva los siguientes enunciados teniendo en cuenta la implementación de Listas en Python:
# a) Ejecutá las siguientes expresiones y observá los resultados:
'''
a = [1, 2, 3]
print(a)

print(a is a)

print(a + [] is a)

print(a + [] == a)

print([10, 20, 3] > [1, 2, 3])

print([10, 2, 3] > [1, 2, 3])

print([1, 20, 30] > [1, 2, 3])

print([0, 2, 3] <= [1, 2, 3])

print([1] < [2, 3])

print([1] < [1, 2])

print([1, 2] < [0])

a = list(range(1, 4))
print(a)

print([1, 2] == [1, 2])

print([1, 2] is [1, 2])

a = [1, 2, 3]
b = [a[0], a[1], a[2]]

print(a == b)

print(a is b)

print(a[0] == b[1])

print(b is [b[0], b[1], b[2]])
'''

# b) Haz un programa que almacene 5 elementos en una variable del tipo lista, la modiﬁque para que cada componente sea
# igual al cuadrado del componente original. El programa mostrara la lista resultante por pantalla.
'''
lista = []

for i in range(5):
    i = random.randrange(0,10)
    lista.append(i)
print(lista)
#Opcion1: Con esta opcion puedo remplzar directamente los elemetos en la misma lista.
for i in range(len(lista)): #len se utiliza para recorrer la lista por indice.
    lista[i] = i ** 2 #cada i reperesenta una posicion de indice de la lista. No el elemento en si.
    print(i)
print(lista)
#Opcion2: Con esta opcion es necesario crear una lista nueva.
lista2 = []
for i in lista:
    i = i ** 2 #i representa al elemento. No al indice.
    print(i)
    lista2.append(i)
print(lista2)
'''

#c) Escriba un algoritmo que permita cargar una lista. Y que luego, una vez cargada, controle y sustituya cualquier elemento negativo por 0.
'''lista = []
for i in range(10):
    i = random.randrange(-10, 11)
    lista.append(i)
print(lista)

for i in range(len(lista)):
    if lista[i] < 0:
        lista[i] = 0
print(lista)'''

#d)	Realice una función que dada una lista de enteros L, y un número entero n. Elimine de la lista original los elementos que sean iguales a 
# ese número dado.
'''def encuentra_enteros(L, n):
    a = L.count(n)
    while a != 0:
        L.remove(n)
        a = L.count(n)

lista = []
for i in range(10):
    i = random.randrange(1, 11)
    lista.append(i)
print(lista)
numero = int(input('Ingerse un entero: '))

encuentra_enteros(lista, numero)
print(lista)'''

#e) Cargar m elementos en una pila, y luego copiarlos en una nueva lista.

#f) Cargar k elementos en una cola, y luego copiarlos en una nueva lista.

#g)	Cargar dos listas con la misma cantidad de elementos. Luego mezclarlas, cargándolas ordenadas en otra lista.
'''lista1 = [1, 3, 5]
lista2 = [2, 4, 6]
random.shuffle(lista1, random.random)#Mezcla los elementos de una lista
print(lista1)
listaMezcla = lista1 + lista2
print(listaMezcla)
listaMezcla.sort()
print(listaMezcla)'''

#h) Construya un algoritmo que sume todos los elementos en posición par de una lista.
'''lista = [1, 3, 5, 7, 9, 2, 4, 6, 8]
cont = 0
print(lista)
for i in range(len(lista)):
    if i % 2 == 0:
        cont += lista[i]
print(cont)'''

#i) Elabore un programa que dada una lista de 15 elementos, copie en otra lista los elementos pares multiplicados por 2.
'''lista = []
for i in range(15):
    i = random.randrange(1, 11)
    lista.append(i)
print(lista)
lista2 = []
for i in lista:
    if i % 2 == 0:
        lista2.append(i * 2)
print(lista2)'''

#j) Realizar un algoritmo que invierta el orden de una cola.
'''lista = [1, 2, 3, 4, 5]
print(lista)
lista.reverse()
print(lista)'''

#k) Cargue dos listas, y actualice la primer lista con los elementos que están en la segunda y no en la primera.
'''lista1 = [1, 3, 5, 7, 9]
lista2 = [2, 4, 6, 8, 5]
print(lista1)
print(lista2)'''
#Opcion1:
'''for i in lista2:
    if lista1.count(i) == 0:
        lista1.append(i)
print(lista1)'''
#Opcion2:
'''for i in lista2:
    if i not in lista1:
        lista1.append(i)
print(lista1)'''