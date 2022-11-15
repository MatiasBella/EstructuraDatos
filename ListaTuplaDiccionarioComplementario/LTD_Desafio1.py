#Desafío 1
#Escribir un programa que pregunte a diferentes personas cuánto conocen sobre contaminación del 1 al 10,
#almacene estos valores en una lista y los muestre por pantalla ordenados de menor a mayor.

lista = ['tizi: 10', 'gio: 10', 'maia: 8', 'matias: 5']
lista_ordenada = []
lista1 = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []
lista6 = []
lista7 = []
lista8 = []
lista9 = []
lista10 = []


def seleccionar():
    print('Seleccione una opcion:')
    print('1- Nueva encuesta')
    print('2- Mostrar lista')
    print('3- Exit')
    return input()

def ingreso():
    persona = input('Ingrese su Nombre: ')
    print('Cuanto sabe sobre la contaminacion?\nIngrese un numero del 1 al 10, donde 1 es nada y 10 mucho\n')
    conocimiento = input()
    encu = persona + ': ' + conocimiento
    lista.append(encu)
    return lista

def ordenar():
    for i in lista1:
        lista_ordenada.append(i)
    for i in lista2:
        lista_ordenada.append(i)
    for i in lista3:
        lista_ordenada.append(i)
    for i in lista4:
        lista_ordenada.append(i)
    for i in lista5:
        lista_ordenada.append(i)
    for i in lista6:
        lista_ordenada.append(i)
    for i in lista7:
        lista_ordenada.append(i)
    for i in lista8:
        lista_ordenada.append(i)
    for i in lista9:
        lista_ordenada.append(i)
    for i in lista10:
        lista_ordenada.append(i)

print('ENCUESTA SOBRE CONTAMINACION')
while True:
    op = seleccionar()
    if op == '1':
        ingreso()
    elif op =='2':
        for i in lista:
            a = i[-1]
            if a == '0':
                lista10.append(i)
            elif a == '9':
                lista9.append(i)
            elif a == '8':
                lista8.append(i)
            elif a == '7':
                lista7.append(i)
            elif a == '6':
                lista6.append(i)
            elif a == '5':
                lista5.append(i)
            elif a == '4':
                lista4.append(i)
            elif a == '3':
                lista3.append(i)
            elif a == '2':
                lista2.append(i)
            else:
                lista1.append(i)
        ordenar()
        print(lista_ordenada)
        lista_ordenada = []
        lista1 = []
        lista2 = []
        lista3 = []
        lista4 = []
        lista5 = []
        lista6 = []
        lista7 = []
        lista8 = []
        lista9 = []
        lista10 = []
    elif op == '3':
        break


