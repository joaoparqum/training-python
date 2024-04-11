import functools
def decorador(funcao):
    @functools.wraps(funcao)
    def envelope(nome):
        print("faz alguma coisa antes da funcao")
        funcao(nome)
        print("faz alguma coisa depois da funcao")

    return envelope

@decorador #açucar sintaxe
def ola_mundo(nome):
    print(f"olá mundo {nome}")

#como fazer que a funcao ola mundo seja printada entre duas mensagens
#pode ser feito para mensagens de segurança
#ola_mundo = decorador(ola_mundo)
ola_mundo("João")