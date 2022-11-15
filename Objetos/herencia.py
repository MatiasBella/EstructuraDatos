class Vehiculo:

    def __init__(self, color, ruedas):
        self.color = color
        self. ruedas = ruedas

    def get_color(self):
        return self.color

    def get_ruedas(self):
        return self.ruedas

    def set_color(self, nuevo_color):
        self.color = nuevo_color

    def set_ruedas(self, nuevo_ruedas):
        self.ruedas = nuevo_ruedas

    def mostrar(self):
        return f'Clase "{self.__class__.__name__}"\n'\
            f'Color {self.color}\n'\
            f'Ruedas {self.ruedas}\n'

    #Es lo mismo q def mostrar
    #def __str__(self):
        #return f'Vehiculo:\n color {self.color}\n ruedas {self.ruedas}'

class Coche(Vehiculo):#En caso de tener varias la mas importante es la de la izq

    def __init__(self, color, ruedas, velo, cc):
        #Super es el padre. En el caso de tener mas de una herencia debemos poner el nombre en vez de super
        super().__init__(color, ruedas)

        self.velocidad = velo
        self.cilindrada = cc

    def get_cilindrada(self):
        return self.cilindrada

    def get_velocidad(self):
        return self.velocidad

    def set_cilindrada(self, nuevo_cilindrada):
        self.cilindrada = nuevo_cilindrada
    def set_rvelocidad(self, nuevo_velocidad):
        self.velocidad = nuevo_velocidad

class Camioneta(Coche):

    def __init__(self, color, ruedas, velo, cc, carga):
        Vehiculo().__init__(color, ruedas)
        Coche().__init__(velo, cc)

        self.carga = carga
    
    def get_carga(self):
        return self.carga
    
    def set_carga(self, nuevo_carga):
        self.carga = nuevo_carga

class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def get_tipo(self):
        return self.tipo
    
    def set_tipo(self, nuevo_tipo):
        self.tipo = nuevo_tipo
    
class Motocicleta(Bicicleta):

    def __inti__(self, color, ruedas, tipo, velo, cc):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velo
        self.cilindrada = cc
    
    def get_velocidad(self):
        return self.velocidad

    def get_cilindrada(self):
        return self.velocidad

    def set_cilindrada(self, nuevo_cilindrada):
        self.cilindrada = nuevo_cilindrada
    
    def mostrar(self):
        return super().mostrar()+\
            f'Cilindrada {self.cilindrada}\n'

def catalogar(lista):
    print('Lista de vehiculos\n')
    for i in lista:
        #No se que es i
        print(i.mostrar())

c1 = Coche('rojo',4,200,180)
camioneta1=Camioneta(5000,200,700,'azul',4)
bicicleta1=Bicicleta('deportiva', 'verde', 2)
moto1=Motocicleta(250, 500, 'urbana', 'negra', 2)

vehiculo=[c1, camioneta1, bicicleta1, moto1]

print(c1)
    

    