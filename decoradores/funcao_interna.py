def pai():
    print("Função pai")

    def filho_1():
        print("Sou a função filho 1")

    def filho_2():
        print("Sou a função filho 2")

    filho_2()
    filho_1()

pai()