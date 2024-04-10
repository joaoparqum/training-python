class Animal:
    def __init__(self, num_patas):
        self.num_patas = num_patas

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class Gato(Mamifero):
    pass

class Onitorrinco(Mamifero, Ave):
    pass

orni = Onitorrinco(num_patas=4, cor_pelo="marrom", cor_bico="preto")
print(orni)