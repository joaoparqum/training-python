#texto = input("digite uma palavra")
#VOGAIS = 'AEIOU'

#for letra in texto:
#    if letra.upper() in VOGAIS:
#        print(letra)

opcao = -1
while opcao != 0:
    opcao = int(input('1-Sacar\n2-depositar\n0-sair'))

else:
    print("obrigado, por usar o sistema!!")

#range(iniciação, condição, incremento)
for numero in range(0, 100, 10):
    print(numero, end="\n")