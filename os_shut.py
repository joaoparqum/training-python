import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

#os.mkdir(ROOT_PATH / "novo_diretório")

arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()