from datetime import timedelta, datetime

tamanho = "P"
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.today()

if tamanho == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro irá sair {data_estimada}")
elif tamanho == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro irá sair {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro irá sair {data_estimada}")


data_hora = datetime.now()
data_str = "2000-01-24 16:00"
mascara_ptbr = "%d/%m/%Y %a"

print(data_hora.strftime(mascara_ptbr))