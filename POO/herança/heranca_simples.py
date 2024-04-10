class Veiculo:

    def __init__(self, cor, placa):
        self.cor = cor
        self.cor = placa

    def ligar_motor(self):
        print("Ligar motor...")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    pass

moto = Motocicleta("preta","CVBNB")
print(moto)
moto.ligar_motor()

carro = Carro("branco","HGJFGHJ")
print(carro)
carro.ligar_motor()

cam = Caminhao("Azul","JKLH")
print(cam)
cam.ligar_motor()