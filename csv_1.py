import csv

from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / 'usuarios.csv', 'w', encoding='utf=8') as arquivo:
        escrever = csv.writer(arquivo)
        escrever.writerow(["0","Paulo"])
        escrever.writerow(["1","Camila"])
        escrever.writerow(["2","João"])
except IOError as exc:
    print(f"Erro ao criar o arquivo! {exc}")
