#Desafío 2	
#Crea una tupla con los factores que más afectan a los mares. Luego para jugar con niños y niñas,
#aprendiendo sobre contaminación del agua crea un programa que pida números, si el numero esta entre 1 y
#la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.
#El programa termina cuando el usuario introduce un cero.

tupla = ('calentamiento', 'plastico', 'petroleo', 'sobrepesca', 'acidificacion')
t = len(tupla)
print(t)
print('Cuantos son los factores que afectan a los mares?')
print('Ingresa 0 (cero) para salir o un numero para jugar:')
op = int(input())
while op != 0:
    if op <= t:
        print(tupla[op-1])
    if op > t:
        print('ERROR!!!')
    op = int(input('Ingresa otro numero o O (cero) para terminar: '))

print('JUEGO FINALIZADO')