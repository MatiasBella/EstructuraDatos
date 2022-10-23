#EJERCIOCIO 1:
'''
print('A continuacion debera ingresar 10 numeros. Siga las instrucciones:')
n1 = int(input('Ingrese un numero: '))
ng = [n1]
n2 = 0
for i in range(n2, 9):
    n2 = int(input('Ingrese un numero: '))
    ng.append(n2)
    if n2 >= n1:
        n1 = n2
print(f'\n\tEl numero mas grande ingresado fue: {n1}\n\tLos numeros ingresados fueron: {ng}')
'''
#EJERCICIO 2:

#EJERCICIO 3:
'''
print('A continuacion ingrese los nuemeros que desea multiplicar:')
a = int(input('Ingrese el primer numero: '))
b = int(input('Ingrese el segundo numero: '))
c = 0
for i in range (b):
    c += a
    print(c)
print(f'\nEL RESULTADO DE {a} X {b} ES: {c}')
'''
#EJERCICIO 4:
'''
a = 100
print(a)
for i in range (100):
    a -= 1
    print(a)
'''
#EJERCICIO 5:
'''
print('A continuacion ingrese numeros para saber si el numero es PAR o IMPAR.\nPara finalizar ingrese 0 (cero)')
n = int(input('Ingrese un numero: '))
while n != 0:
    if n % 2 == 0:
        print(f'{n} es PAR')
    else:
        print(f'{n} es IMPRAR')
    n = int(input('Ingrese un numero o 0 para finalizar: '))
'''
#EJERCICIO 6:
'''
n = int(input('Ingrese un numero: '))
n1 = 0
cont = 0
suma = 0
while n != 'F':
    if n % 2 == 0:
        if n >= n1:
            print(n)
            cont += 1
            n1 = n
    n = input('Ingrese un numero o F para finalizar: ').upper()
    if n != 'F':
        n = int(n)
print(f'La cantidad de numeros que cumplieron los requisitos fueron: {cont}')
'''
#EJERCICIO 7:
'''
print('A continuacion ingrese dos numeros entre los que buscar y sumar los multiplos de 5.\nEl primer numero debe ser mayor que el segundo.')
n1 = int(input('Ingrese un numero mayor a 0: '))
n2 = int(input('Ingrese un numero mayor a 0: '))
nc = 0
suma = 0

while n1 < 0:
    n1 = int(input('NO se permiten numeros negativos. Ingrese otro numero: '))
while n2 < 0:
    n2 = int(input('NO se permiten numeros negativos. Ingrese otro numero: '))
if n1 > n2:
    nc = n1
    n1 = n2
    n2 = nc
for i in range(n1, n2 + 1):
    if i % 5 == 0:
        suma += i
        print(suma)
'''
#EJERCICIO 8:
'''
total = 0
cont = 0
print('PROGRAMA DE COMPRA')
cant = int(input('Ingrese cantidad del producto X: '))
precio = int(input('Ingrese precio de producto X: '))
while cant != 0:
    suma = cant * precio
    total += suma
    cont += cant
    cant = int(input('Ingrese cantidad del producto X o 0 (cero) para finalizar: '))
    if cant == 0:
        break
    precio = int(input('Ingrese precio de producto X: '))
print(f'Ud compro {cont} productos')
print(f'Total de la compra: {total}')
'''
#EJERCICIO 9:
'''
persona = 0
edu1 = 0
edu2 = 0
edu3 = 0
edu4 = 0
edu5 = 0
seguir = 'si'
print('CENSO NACIONAL DE ESTUDIO')
while seguir != 'NO':
    print('Ingrese ultimo nivel de estudio completado: ')
    censo = int(input('\t1- Primaria\n\t2- Secundaria\n\t3- Tecnica\n\t4- Profesional\n\t5- Posgrado\n\t'))
    persona += 1
    if censo == 1:
        edu1 += 1
    elif censo == 2:
        edu2 += 1
    elif censo == 3:
        edu3 += 1
    elif censo == 4:
        edu4 += 1
    elif censo == 5:
        edu5 += 1
    seguir = input('Otra persona? (SI o NO): ').upper()

edu1 = edu1 * 100 / persona
edu2 = edu2 * 100 / persona
edu3 = edu3 * 100 / persona
edu4 = edu4 * 100 / persona

print('PORCENTAJE DE ENTREVISTADOS EN EL DIA DE LA FECHA')
print(f'Personas entrevistadas: {persona}')
print(f'Educacion PRIMARIA \t{edu1}%\nEducacion SECUNDARIA \t{edu2}%\nCarrera TECNICA \t{edu3}%\nEducacion PROFESIONAL \t{edu4}%\nPOSGRADO \t\t{edu5}%')
'''
#EJERCICIO 10:
'''
otro = 'SI'
print('CALCULADOR DEL PERIMETRO DE UN TRIANGULO')
while otro != 'NO':
    l1 = float(input('Lado 1: '))
    l2 = float(input('Lado 2: '))
    l3 = float(input('Lado 3: '))
    perimetro = l1 + l2 + l3
    print(perimetro)
    otro = input('Desea continuar? (SI o NO): ').upper()
print('CALCULADORA FINALIZADA')
'''
#EJERCICIO 11:
'''
print('CALCULADORA RARA')
n_div = []
n = int(input('Ingrese un numero: '))
for i in range (1, n + 1):
    if n % i == 0:
        n_div.append(i)
print(f'Los divisores de {n} son: {n_div}')
'''
#EJERCICIO 12:
'''
tipo_a = 50
tipo_b = 55
tipo_c = 60
tipo = ''
diario = 0
print('Bienvenido a la Estacion')
while tipo != 'D':
    tipo = input('Ingrese tipo de cliente (A, B, C, o D): ').upper()
    if tipo == 'D':
        break
    fuel = float(input('Ingrese cantidad de litros: '))
    if tipo == 'A':
        fuel = fuel * tipo_a
    elif tipo == 'B':
        fuel = fuel * tipo_b
    elif tipo == 'C':
        fuel = fuel * tipo_c
    print(f'TOTAL a pagar por cliente: {fuel}')
    diario += fuel
print(f'TOTAL recaudado por la Estacion en el dia de la fecha: {diario}')
'''
#EJERCICIO 13:
'''
from random import randrange

cat1 = 0
cat2 = 0
cat3 = 0
cat4 = 0
grupo_examen = []

for i in range(1, 101):
    i = randrange(10, 100)
    grupo_examen.append(i)
    if i < 50:
        cat1 += 1
    elif (i >= 50) and (i < 70):
        cat2 += 1
    elif (i >= 70) and (i < 80):
        cat3 += 1
    else:
        cat4 += 1
print(grupo_examen)
print(f'TOTAL de Estudiantes: {cat1+cat2+cat3+cat4}')
print(f'{cat1} estudiantes obtuvieron una calificacion inferior a 50')
print(f'{cat2} estudiantes obtuvieron una calificacion entre 50 y 70')
print(f'{cat3} estudiantes obtuvieron una calificacion entre 70 y 80')
print(f'{cat4} estudiantes obtuvieron una calificacion igual o superior a 80')
'''
#EJERCICIO 14:
'''
hola = 3
precio_venta = 1.5
pizza_peque = 5
pizza_media = 8
pizza_grande = 10
precio_extra = 1
total_compra = 0
otra = 'SI'
print('BIENVENIDO A LA PIZZERIA')
print('Seleccione el tamaño de la pizza segun opciion: ')
while otra == 'SI':
    pizza = input('\t1- PEQUEÑA\n\t2-MEDIANA\n\t3- GRANDE\n\t')
    if pizza == '1':
        pizza = pizza_peque
    elif pizza == '2':
        pizza = pizza_media
    elif pizza == '3':
        pizza = pizza_grande
    extra = int(input('Ingrese cantidad de ingrediente extra quiere (PEPINILLOS, CHAMPIÑONES o CEBOLLAS): '))
    extra = extra * precio_extra
    total = (pizza + extra + hola) * precio_venta
    total_compra += total
    otra = input('Desea otra pizza?(SI o NO): ').upper()
print(f'Su compra es de {total_compra} pesos')
'''
#EJERCICIO 15
'''
from random import randint

print('BIENVENIDO AL SUPERMERCADO')
compra = float(input('Ingrese el valor de la compra: '))
n = randint(0, 99)
'''