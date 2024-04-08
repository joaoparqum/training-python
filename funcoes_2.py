#antes da barra printa sem variavel, depois da barra printa com variavel
#Posição/Chaves

def criar_carro(modelo,ano,placa, /, marca,motor,combustivel):
    print(modelo,ano,placa,marca,motor,combustivel)

criar_carro("uno",1992,"ERTW", marca="Fiat", motor="V8", combustivel="gasolina")

#apenas por chaves
def criar_carro2(*,modelo,ano,placa,marca,motor,combustivel):
    print(modelo,ano,placa,marca,motor,combustivel)

#colocar um por posicao
def criar_carro3(modelo,ano,placa, /,marca,*,motor,combustivel):
    print(modelo,ano,placa,marca,motor,combustivel)

def somar(a, b):
    return a + b

def result(a, b, funcao):
    resultado = funcao(a, b)
    print(f"Resultado = {resultado}")

result(10,20, somar)
