'''Un programa que me permita cargar los datos de los alumnos del info nombre, localidad y dni
Me permita agregar la nota de los exámenes, teniendo en cuenta que hay dos módulos y 3 notas para cada uno.
Debe tener un menú interactivo que permita:
Mostrar el alumno con mayor promedio
Mostrar todos los que aprobaron ambos módulos
Dado el DNI de un alumno, me muestre sus notas.
'''

#alumnos = {30111222:'Juan Perez'}

def menu():
    print('1- Cargar ALUMNO')
    print('2- Cargar NOTA')
    print('3- Buscar ALUMNO')
    print('4- Mostrar ALUMNOS APROBADOS')
    print('5- Mostrar ALUMNO CON MEJOR PROMEDIO')
    print('6- EXIT')
    op = input()
    return op

