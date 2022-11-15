#UN POCO MÁS COMPLICADO....
#) Ingresar una palabra, carácter por carácter, en una lista y determinar si es palíndromo.
'''poli = (input('Ingrese una palabra para saber si es POLIDROMO: ')).upper()
lista = []

for i in poli:
    lista.append(i)
print(lista)

lista2 = lista.copy()
lista2.reverse()
if lista == lista2:
    print('ES PALINDROMO')
else:
    print('NO ES POLINDROMO')'''
    
#b) Leer una frase y luego invierta el orden de las palabras en la frase. Por Ejemplo: “una imagen vale por
# mil palabras” debe convertirse en “palabras mil por vale imagen una”.
'''frase = input('Ingrese una frase para ser invertida: ')
palabra = ''
lista = []
frase_final = ''

for i in frase:
    if i != " ":
        palabra += i
    elif i == " ":
        lista.append(palabra)
        palabra = ''
lista.append(palabra)

lista.reverse()

for i in lista:
    frase_final += i + ' '
print(frase_final)'''

#c) Simular la operación de colas de un Rapipago, que funciona con dos colas diferentes. El usuario llega y
# se ubica en la cola de menor cantidad de personas. Al finalizar el proceso indique cuántos elementos tiene cada cola.
'''cola1 = []
cola2 = []
nuevo_cliente = input('Ingreso un cliente? (SI o NO): ').upper()
while nuevo_cliente != 'NO':
    if len(cola1) <= len(cola2):
        cola1.append(nuevo_cliente)
        print('Dirijase a la cola 1')
    elif len(cola2) < len(cola1):
        cola2.append(nuevo_cliente)
        print('Dirijase a la cola 2')
    nuevo_cliente = input('Ingreso un cliente? (SI o NO): ').upper()
print(f'En la cola1 hay {len(cola1)} clientes.')
print(f'En la cola2 hay {len(cola2)} clientes.')'''

#d) En un almacén se guarda mercadería en contenedores. No es posible colocar más de (n - 1) contenedores uno encima
# del otro y, no hay área para más de 5 pilas de contenedores. Elabore un programa que permita gestionar el
# ingreso y salida de contenedores. Note que para retirar un contenedor es necesario retirar los contenedores
# que están encima de él y colocarlos en otra pila.

#OPCION 1:

'''n = int(input('Ingrese la cantidad maxima de contenedores que se pueden apilar: '))
pila1 = []
pila2 = []
pila3 = []
pila4 = []
pila5 = []
contenedor = int(input('Seleccione la operacion que desea hacer:\n\t1- AGREGAR CONTENEDOR\n\t2- SACAR CONTENEDOR\n\t5- EXIT\n\t'))

while contenedor !=5:
    if contenedor == 1:
        if len(pila1) <= (n - 1):
            pila1.append(contenedor)
        elif len(pila2) <= (n - 1):
            pila2.append(contenedor)
        elif len(pila3) <= (n - 1):
            pila3.append(contenedor)
        elif len(pila4) <= (n - 1):
            pila4.append(contenedor)
        elif len(pila5) < (n - (n - 1)):
            pila5.append(contenedor)
        else:
            print('\t\t\tERROR: Capacidad maxima de deposito alcanzada!!!\n\n\t\t\tSeleccione otra opcion')
            pass
    
    if contenedor == 2:
        print('De que pila desea extraer el contenedor:')
        print(f'PILA1: {len(pila1)}, PILA2: {len(pila2)}, PILA3: {len(pila3)}, PILA4: {len(pila4)}, PILA5: {len(pila5)}')
        e = int(input('\n\t1- Pila1\n\t2- Pila2\n\t3- Pila3\n\t4- Pila4\n\t5- Pila5\n\t'))
        if e == 1:
            pila1.pop()
        if e == 2:
            pila2.pop()
        if e == 3:
            pila3.pop()
        if e == 4:
            pila4.pop()
        if e == 5:
            pila5.pop()
    print(pila1)
    print(pila2)
    print(pila3)
    print(pila4)
    print(pila5)
    contenedor = int(input('Seleccione la operacion que desea hacer:\n\t1- AGREGAR CONTENEDOR\n\t2- SACAR CONTENEDOR\n\t5- EXIT\n\t'))'''

#OPCION 2: DOBLE LISTA

'''n = int(input('Ingrese la cantidad maxima de contenedores que se pueden apilar: '))
pila1 = []
pila2 = []
pila3 = []
pila4 = []
pila5 = []
deposito = [pila1, pila2, pila3, pila4, pila5]

print('Seleccione la operacion que desea hacer:')
contenedor = int(input('\n\t1- AGREGAR CONTENEDOR\n\t2- SACAR CONTENEDOR\n\t5- EXIT\n\t'))
while contenedor != 5:
    if contenedor == 1:
        if len(pila1) <= (n - 1):
            pila1.append(contenedor)
        elif len(pila2) <= (n - 1):
            pila2.append(contenedor)
        elif len(pila3) <= (n - 1):
            pila3.append(contenedor)
        elif len(pila4) <= (n - 1):
            pila4.append(contenedor)
        elif len(pila5) < (n - (n - 1)):
            pila5.append(contenedor)
        else:
            print('\t\t\tERROR: Capacidad maxima de deposito alcanzada!!!\n\n\t\t\tSeleccione otra opcion')
            pass
    
    if contenedor == 2:
        print('De que pila desea extraer el contenedor:')
        print(f'PILA1: {len(pila1)}, PILA2: {len(pila2)}, PILA3: {len(pila3)}, PILA4: {len(pila4)}, PILA5: {len(pila5)}')
        e = int(input('\n\t1- Pila1\t2- Pila2\t3- Pila3\n\t4- Pila4\n\t5- Pila5\t'))
        deposito[(e-1)].pop()
    print(deposito)
    contenedor = int(input('Seleccione la operacion que desea hacer:\n\t1- AGREGAR CONTENEDOR\n\t2- SACAR CONTENEDOR\n\t5- EXIT\n\t'))'''

#e) Se tiene una lista que contiene mensajes encriptados de varios usuarios. Cada mensaje se encierra entre {},
# y para indicar que se terminó el área de mensajes de un usuario se usa un signo &. Indique cuántos usuarios y
# cuántos mensajes hay en la lista, teniendo en cuenta que todos los mensajes están correctamente formados, es
# decir comienzan con { y terminan con }. Y que es seguro que al menos exista un usuario en la lista.
'''
lista = [{'hola soy juan'}, {'hola soy pedro'}, '&',  {'hola soy yo'}]
user = 1
sms = 0

for i in lista:
    if i != '&':
        sms += 1
    elif i == '&':
        user += 1
print(f'Hay {user} usuarios y {sms} mensajes en la lista')
'''

#f) Se tiene una lista con los datos de los clientes de una compañía de telefonía celular, los cuales pueden
# aparecer repetidos en la lista, si tienen registrado más de un número telefónico. La compañía para su próximo
# aniversario desea enviar un regalo a sus clientes, sin repetir regalos a un mismo cliente. En una lista se
# almacenan los regalos disponibles en orden. Se desea un programa que cree una nueva lista con los clientes,
# sin repetir y ordenada. Y que al final muestre el regalo que le corresponde a cada cliente.

#g) Se tiene una lista que almacena pedidos en orden de llegada, por ende puede haber más de un pedido para el
# mismo artículo. Crear una lista donde se almacene la cantidad de pedidos por artículo.

pedidos = ['pan', 'facturas', 'pan', 'chipa', 'chipa', 'pan']
articulos = []
cant_art = []

for i in pedidos:
    if i not in articulos:
        articulos.append(i)
for i in articulos:
    cant = pedidos.count(i)
    cant = str(cant)
    temp = i + ': ' + cant
    cant_art.append(temp)
print(cant_art)
    