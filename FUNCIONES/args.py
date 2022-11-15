def sumar(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sumar(2,4,5,6,6,8,10,25))

def saludar(*personas):
    for i in personas:
        print('Hola ' + i)

saludar('matias', 'maia', 'tizi', 'gio')