class Camisa:
    def __init__(self):
        self.__tamanho: str = ""

    def setTamanho(self, valor: str):
        tamanhos_validos = ["PP", "P", "M", "G", "GG", "XG"]
        if valor not in tamanhos_validos:
            print("fail: Valor invalido, tente PP, P, M, G, GG ou XG")
            return
        self.__tamanho = valor

    def getTamanho(self):
        return self.__tamanho

camisa = Camisa()

while camisa.getTamanho() == "":
    print("Digite seu tamanho de camisa")
    tamanho = int(input())
    camisa.setTamanho(tamanho)

print("Parabens, voce comprou uma camisa tamanho", camisa.getTamanho())
