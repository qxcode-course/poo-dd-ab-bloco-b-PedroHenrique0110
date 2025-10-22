#fiz mais de 40 linhas sem estar com o tko aberto quando percebi aí eu abri ele por isso surgem 40 linhas do nada
class Lead:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.__thickness = thickness
        self.__hardness = hardness
        self.__size = size

    def usagePerSheet(self) -> float:
        if self.__hardness == "HB":
            return 1.0
        elif self.__hardness == "2B":
            return 2.0
        elif self.__hardnes == "4B":
            return 4.0
        elif self.__hardness == "6B":
            return 6.0
        else:
            return 0.0
        
    def 

class Pencil:
    def __init__(self, thickness: float):
        self.__thickness = thickness
        self.__tip = None

    def inserir(self, thickness: float, hardness: str, size: int):
        if thickness != self.__thickness:
            print("fail: calibre incompativel")
            return
        if self.__tip != None:
            print("fail: ja existe grafite")
            return
        self.__tip = Lead(thickness, hardness, size)

    def remover(self):
        if self.__tip == None:
            print("fail: nao existe grafite")
            return
        tip = self.__tip
        self.__tip = None
        return tip

    def escrever(self)
        if self.__tip == None:
            print("fail: nao existe grafite")
            return
        if self.__tip.size <= 0:
            print("fail: tamanho insuficiente")
            return
        usage = self.__tip.usagePerSheet()
        tamanhofinal = self.__tip.size - usage

        if tamanhofinal < 10:
            tamanhoatual = self.__tip.size - 10
            self.__tip.size = 10
            print("fail: folha incompleta")
            return
            self.__tipe.size = tamanhofinal

        def __str__(self):
            return f"calibre: {self.__thickness}, grafite: {self.__tip}"

        
def main():
    pencil = Pencil(0)
    while True:
        line = input()
        print("$")


main()

