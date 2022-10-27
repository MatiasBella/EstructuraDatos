'''print('Hola trolo, estamos probando git para que dejes de mankear XD')
print('Estamos en windows en este momento. Vamos a verificar si funciona este show')

def saludo(n, s):
    print(f'Hola {n}, pedazo de {s}!!!')

nombre = input('Nombre: ')
insulto = input('Insulto: ')

saludo(nombre, insulto)'''

'''def suma(n1, n2):
    c = n1 + n2
    print(c)


numero1 = int(input('Ingrese un numero: '))
numero2 = int(input('Ingrese otro: '))
suma(numero1, numero2)'''

def elimina_elementos(L, n):
    a = (L).count(n)
    while a != 0:
        (L).remove(n)
        a = (L).count(n)

lista1 = [1, 2, 5, 7, 10, 1]
print(lista1)
numero = int(input('Ingresa un numero entero: '))
elimina_elementos(lista1, numero)
#a = list(lista1).count(numero)
#print(list(lista1))
#print(a)
#while a != 0:
#    (lista1).remove(numero)
#    print(list(lista1))
#    a = (lista1).count(numero)
#    print(a)
print(lista1)


