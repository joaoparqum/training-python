#usado mais em requisições http de APIs
def gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2


for i in gerador(numeros=[4,7,8]):
    print(i)