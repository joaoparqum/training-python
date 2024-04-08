def exibir_mensagem():
    print("olá mundo!")

def mensagem_2(nome):
    print(f"Seja bem vindo {nome}")

exibir_mensagem()
mensagem_2(nome="João Paulo")

#com retorno
def calcular(numeros):
    return sum(numeros)

print(calcular([10,20,30]))

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat","gol", 1992, "QWER#%")
