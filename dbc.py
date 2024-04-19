lista = [4]
lista_aux = [4]
for i in range(4):
    numeros = int(input(""))
    lista.append(numeros)

soma = int(input(""))

lista_aux.append(lista)

for nums in lista:
    for num in lista_aux:
        if nums + num == soma:
            print(nums, num)
