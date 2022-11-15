#Desafío 3		
#Crea un diccionario donde la clave sea el nombre de biólogos y el valor sea el email (no es necesario validar).
#Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán insertar nombres repetidos.

agenda = {}


while True:

    print('AGENDA DE BIOLOGOS')
    print('Seleccione una opcion:')
    print('1- Agregar biologo')
    print('2- Mostrar agenda')
    print('3- Exit')
    op = int(input())

    if op == 1:
        nombre = input('Ingrese el nombre del biologo: ').upper()
        while nombre in agenda:
            print(f'El nombre {nombre} ya esta registrado. Por favor elija otro')
            nombre = input('Ingrese el nombre del biologo: ').upper()
        email = input('Ingrese el email: ').lower()
        agenda[nombre] = email
    if op == 2:
        print(agenda)
    if op == 3:
        break
print(agenda)
print('Agenda finalizada')