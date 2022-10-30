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
frase = input('Ingrese una frase para ser invertida: ')
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
print(frase_final)

#c) Simular la operación de colas de un Rapipago, que funciona con dos colas diferentes. El usuario llega y
# se ubica en la cola de menor cantidad de personas. Al finalizar el proceso indique cuántos elementos tiene cada cola.

#d) En un almacén se guarda mercadería en contenedores. No es posible colocar más de n contenedores uno encima
# del otro y, no hay área para más de 5 pilas de contenedores. Elabore un programa que permita gestionar el
# ingreso y salida de contenedores. Note que para retirar un contenedor es necesario retirar los contenedores
# que están encima de él y colocarlos en otra pila.

#e) Se tiene una lista que contiene mensajes encriptados de varios usuarios. Cada mensaje se encierra entre {},
# y para indicar que se terminó el área de mensajes de un usuario se usa un signo &. Indique cuántos usuarios y
# cuántos mensajes hay en la lista, teniendo en cuenta que todos los mensajes están correctamente formados, es
# decir comienzan con { y terminan con }. Y que es seguro que al menos exista un usuario en la lista.

#f) Se tiene una lista con los datos de los clientes de una compañía de telefonía celular, los cuales pueden
# aparecer repetidos en la lista, si tienen registrado más de un número telefónico. La compañía para su próximo
# aniversario desea enviar un regalo a sus clientes, sin repetir regalos a un mismo cliente. En una lista se
# almacenan los regalos disponibles en orden. Se desea un programa que cree una nueva lista con los clientes,
# sin repetir y ordenada. Y que al final muestre el regalo que le corresponde a cada cliente.

#g) Se tiene una lista que almacena pedidos en orden de llegada, por ende puede haber más de un pedido para el
# mismo artículo. Crear una lista donde se almacene la cantidad de pedidos por artículo.