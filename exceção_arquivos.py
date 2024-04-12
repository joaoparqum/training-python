from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH / "meuarquivo.py", "r")
except FileNotFoundError as exc:
    print("arquivo não encontrado!")
    print(exc)
except NotADirectoryError as exc:
    print("não foi possivel abrir o arquivo!")
    print(exc)