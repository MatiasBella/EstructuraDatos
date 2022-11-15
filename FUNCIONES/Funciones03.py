'''def saludar(persona='Desconocido'):
    return 'Hola ' + persona

print(saludar('Matias'))
print(saludar())
'''
'''def calcular_volumen(base=1, altura=1, profundidad=1):
    return base*altura*profundidad

print(calcular_volumen(2,4,4))
'''
'''def sumar(a,b,c):
    return a+b+c

print(sumar())
'''
def funcion(a,b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print(args)
    print(kwargs)

funcion(3,4,5,6,7,8,'f','a', color='rojo',size=12)