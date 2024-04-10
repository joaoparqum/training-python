class Pessoa:

    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_data(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return Pessoa(nome, idade)

    @staticmethod
    def eh_maior_idade(idade):
        return idade >= 18    

p = Pessoa.criar_data(2000,1,24,"João")
print(p.nome, p.idade)

print(Pessoa.eh_maior_idade(24))