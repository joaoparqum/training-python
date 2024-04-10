class Cachorro:

    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Excluindo a instancia da classe")

    def latir(self):
        print("Au au")

c = Cachorro("Bengo","Preto")
c.latir()