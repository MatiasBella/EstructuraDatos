
'''
lista = []
seguir = 'SI'
while seguir != 'NO':
    e = int(input('Ingrese un elemento: '))
    lista.append(e)
    seguir = input('Desea seguir? SI o NO: ').upper()
print(lista)
for i in range(len(lista)):
    if lista[i] < 0:
        lista[i] = 0
print(lista)
'''
from random import randrange

lista1 = []
for i in range(10):
    lista1.append(randrange(1, 20))
print(lista1)

lista2 = []
for i in range(10):
    lista2.append(randrange(1, 20))
print(lista2)

for i in lista2:
    if i not in lista1:
        lista1.append(i)
print(lista1)