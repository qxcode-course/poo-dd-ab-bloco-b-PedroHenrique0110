class Roupa:
    def __init__(self):
        self.__tamanho: str = ""

    def getTamanho(self):
        return self.__tamanho
    
    def setTamanho(self, valor: str):
        tamanhos_validos = ["PP", "P", "M", "G", "GG", "XG"]
        if valor not in tamanhos_validos:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG") 
        else:
            self.__tamanho = valor      

    def show(self):
        print(self)
    
    def __str__(self):
        return (f"size: ({self.getTamanho()})")

def main():
    roupa = Roupa()

    while True:
        line = input()
        print("$" + line)
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(roupa)
        elif args[0] == "size":
            valor = args[1]
            roupa.setTamanho(args[1])
main()