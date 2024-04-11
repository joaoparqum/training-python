def decorador(funcao):
    def envelope():
        print("faz alguma coisa antes da funcao")
        funcao()
        print("faz alguma coisa depois da funcao")

    return envelope

@decorador #açucar sintaxe
def ola_mundo():
    print("olá mundo")

#como fazer que a funcao ola mundo seja printada entre duas mensagens
#pode ser feito para mensagens de segurança
#ola_mundo = decorador(ola_mundo)
ola_mundo()