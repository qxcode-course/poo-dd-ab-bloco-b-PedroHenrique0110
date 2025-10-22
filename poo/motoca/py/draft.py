class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade

    def getNome(self):
        return self.__nome

    def getIdade(self):
        return self.__idade

    def __str__(self):
        return f"{self.getNome()}:{self.getIdade()}"

class Moto:
    def __init__(self, potencia: int):
        self.__potencia = potencia
        self.__minutos = 0
        self.__pessoa: Pessoa = None

    def getPotencia(self):
        return self.__potencia

    def getMinutos(self):
        return self.__minutos

    def getPessoa(self):
        return self.__pessoa

    def subir(self, pessoa: Pessoa) -> bool:
        if self.__pessoa != None:
            print("fail: busy motorcycle")
            return False
        else:
            self.__pessoa = pessoa
        return True

    def descer(self) -> Pessoa | None:
        if self.__pessoa == None:
            print("fail: empty motorcycle")
            return None
        pessoa = self.__pessoa
        self.__pessoa = None
        return pessoa

    def comprarTempo(self, minutos: int):
        self.__minutos += minutos

    def honk(self):
        return "P" + "e" * self.__potencia + "m"

    def dirigir(self, minutos: int):
        if self.__minutos <= 0:
            print("fail: buy time first")
            return
        if self.__pessoa == None:
            print("fail: empty motorcycle")
            return
        if self.__pessoa.getIdade() > 10:
            print("fail: too old to drive")
            return
        if minutos > self.__minutos:
            print(f"fail: time finished after {self.__minutos} minutes")
            self.__minutos = 0
            return
        self.__minutos -= minutos

    def __str__(self):
        pessoa_str = f"({self.__pessoa})" if self.__pessoa != None else "(empty)"
        return f"power:{self.__potencia}, time:{self.__minutos}, person:{pessoa_str}"
    
def main():
    moto = Moto(1)
    while True:
        line = input()
        print("$" + line)
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "init":
            potencia = int(args[1])
            moto = Moto(potencia)
        elif args[0] == "show":
            print(moto)
        elif args[0] == "enter":
            nome = args[1]
            idade = int(args[2])
            pessoa = Pessoa(nome, idade)
            moto.subir(pessoa)
        elif args[0] == "leave":
            p = moto.descer()
            if p != None:
                print(p)
        elif args[0] == "buy":
            minutos = int(args[1])
            moto.comprarTempo(minutos)
        elif args[0] == "drive":
            minutos = int(args[1])
            moto.dirigir(minutos)
        elif args[0] == "honk":
            print(moto.honk())

main()
