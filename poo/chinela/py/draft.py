class Chinela:
    def __init__(self):
        self.__tamanho = 0

    def setTamanho(self, valor: int):
        if valor % 2 == 1 and valor < 20 or valor > 50:
            print("fail: tamanho invalido")
            return
        self.__tamanho = valor

    def getTamanho(self):
        return self.__tamanho

chinela = Chinela()

while chinela.getTamanho() == 0:
        print("Digite seu tamanho de Chinela")
        tamanho = int(input())
        chinela.setTamanho(tamanho)

print("Parabens, voce comprou uma chinela tamanho", chinela.getTamanho())
