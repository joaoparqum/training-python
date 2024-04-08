conta_normal = True
conta_uni = False

SALDO = 500
saque = float(input("digite o quanto você quer sacar: "))

if conta_normal:
    if SALDO:
        print("seu saldo é de 500 reais")
        saque = float(input("digite o quanto você quer sacar: "))
    elif saque > SALDO:
        print("voce nao tem saldo suficiente!")
elif conta_uni:
    if SALDO:
        print("seu saldo é de 500 reais")
        saque = float(input("digite o quanto você quer sacar: "))   
    elif saque > SALDO:
        print("voce nao tem saldo suficiente!")