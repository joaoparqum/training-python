def recomendar_plano(a):
    if a <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    elif a > 10 and a < 20:
        return "Plano Prata Fibra - 100Mbps"
    elif a > 20:
        return "Plano Premium Fibra - 300Mbps"

consumo = float(input("Digite o consumo médio mensal dos dados:\n"))

print(recomendar_plano(consumo))