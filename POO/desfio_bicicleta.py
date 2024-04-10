class Bicicleta:

    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("FOOOOON")

    def parar(self):
        print("Parando bicicleta")
        print("Parou")

    def correr(self):
        print("VRRRUMMMMM")

    #outra forma de printar os atributos
    def __str__(self):
        return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"

b1 = Bicicleta("Vermelho","Caloi",2017,900)

b1.buzinar()
b1.correr
b1.parar()

print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("Preta","Caloi",2017,900)

b2.buzinar()
Bicicleta.buzinar()