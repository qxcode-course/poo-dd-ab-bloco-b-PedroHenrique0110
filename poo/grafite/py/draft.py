#fiz mais de 40 linhas sem estar com o tko aberto, quando percebi aí eu abri ele por isso surgem 40 linhas do nada
class Lead:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.__thickness = thickness
        self.__hardness = hardness
        self.__size = size

    def usagePerSheet(self) -> float:
        if self.__hardness == "HB":
            return 1
        elif self.__hardness == "2B":
            return 2
        elif self.__hardness == "4B":
            return 4
        elif self.__hardness == "6B":
            return 6
        else:
            return 0

    def getSize(self):
        return self.__size

    def setSize(self, size: int):
        self.__size = size

    def __str__(self):
        return f"[{self.__thickness}:{self.__hardness}:{self.__size}]"

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
            return None
        tip = self.__tip
        self.__tip = None
        return tip

    def escrever(self):
        if self.__tip == None:
            print("fail: nao existe grafite")
            return
        size = self.__tip.getSize()
        if size <= 10:
            print("fail: tamanho insuficiente")
            return
        usage = self.__tip.usagePerSheet()
        tamanhofinal = size - usage

        if tamanhofinal < 10:
            self.__tip.setSize(10)
            print("fail: folha incompleta")
            return

        self.__tip.setSize(tamanhofinal)

    def __str__(self):
        grafite_str = "null" if self.__tip == None else f"{self.__tip}"
        return f"calibre: {self.__thickness}, grafite: {grafite_str}"

        
def main():
    pencil = Pencil(0)
    while True:
        line = input()
        print("$" + line)
        args = line.split()
        if args[0] == "end":
            break
        if args[0] == "show":
            print(pencil)
        if args[0] == "init":
            thickness = float(args[1])
            pencil = Pencil(thickness)
        if args[0] == "insert":
            thickness = float(args[1])
            hardness = args[2]
            size = int(args[3])
            pencil.inserir(thickness, hardness, size)
        if args[0] == "remove":
            pencil.remover()
        if args[0] == "write":
            pencil.escrever()


main()

