class Estudante:

    escola = "IFBA"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    

jp = Estudante("João",1)
cam = Estudante("Camila",2)

print(jp)
print(cam)