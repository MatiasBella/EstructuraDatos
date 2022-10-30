# [valor, valor, valor]
'''
CLAVE NO SE PUEDE REPETIR
'''
'''
dicc = {}
print(dicc)
print('--------------------')
#carga un valor
#dicc[clave] = valor

dicc['nombre'] = 'Matias'
print(dicc)
# SI LA CALVE NO EXISTE, LA CREA
# PERO SI LA CLAVE YA EXISTE, MODIFICA LA ANTERIOR
print('--------------------')
dicc['nombre'] = 'MICA'
print(dicc)
print('--------------------')
dicc['telefono'] = 3612651564156
print(dicc)
print('--------------------')
# PARA VER UN VALOR NECESARUI LA CLAVE
#print(dicc['nombre'])

#solo recorre las claves
for x in dicc:
    print(x)
print('--------------------')

#para recorrer clave valor
#se usan dos variables: la primera es la clave y la 2da el valor.
for k,v in dicc.items():
    print(f'{k}---->{v}')
'''
'''
    OP1
    agenda = [
                {'nombre':___, 'telefono':___, 'email':___}
            ]
    agenda[0]['nombre']
    agenda[0]['nombre']
    agenda[0]['nombre']
    OP2
    agenda = {
                'nombre':{'telefono':___, 'email':___}
                'nombre':{'telefono':___, 'email':___}
                'nombre':{'telefono':___, 'email':___}
            }
    agenda['nombre'] --> {'telefo:___}
'''

def menu():
    print('QUE QUIERE HACER:')
    print('1-agregar')
    print('2-mostrar')
    print('3-buscar')
    print('5-SALIR')
    opcion = int(input())
    return opcion

def agregar(agenda):
    nom = input('Ingrese nuevo nombre:\t')
    tel = int(input(f'Ingrese telefono de {nom}:\t'))
    mail = input('Ingrese mail de {nom}:\t')

    #OP1
    dic = {'telefono':tel, 'mail':mail}
    #OP2
    #dic = {}
    #dic['telefono'] = tel
    #dic['mail'] = mail
    if nom in agenda.keys():
        print(f'El contacto {nom} ya existe!!!')
        print(f'Si quiere modificarlo ejecute la opcion modificar')
    else:
        agenda[nom] = dic
    print(agenda)
    return agenda

def mostrar(agenda):

    for nombre,datos in agenda.items():

def buscar(agenda):

    buscado = input('A quien quiere buscar?')
    encontro = False
    for nombre,datos in agenda.items():
        if buscado == :
            print(f'El telefono de {} es: {}')

'''Un programa que me permita cargar los datos de los alumnos del info nombre, localidad y dni
Me permita agregar la nota de los exámenes, teniendo en cuenta que hay dos módulos y 3 notas para cada uno.
Debe tener un menú interactivo que permita:
Mostrar el alumno con mayor promedio
Mostrar todos los que aprobaron ambos módulos
Dado el DNI de un alumno, me muestre sus notas.
'''

