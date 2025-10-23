class Pessoa:
    def __init__(self, nome: str, dinheiro: int):
        self.__nome = nome
        self.__dinheiro = dinheiro

    def getNome(self):
        return self.__nome

    def getDinheiro(self):
        return self.__dinheiro
    
    def setDinheiro(self, valor: int):
        self.__dinheiro = valor

    def __str__(self):
        return f"{self.getNome()}:{self.getDinheiro()}"

class Moto:
    def __init__(self):
        self.__motorista: Pessoa = None
        self.__passageiro: Pessoa = None
        self.__kmviagem = 0
        self.__custo = 0

    def setDriver(self, motorista: Pessoa):
        self.__motorista = motorista

    def getDriver(self):
        return self.__motorista

    def setPass(self, passageiro: Pessoa):
        self.__passageiro = passageiro

    def getPass(self):
        return self.__passageiro

    def subir(self, passageiro: Pessoa):
        if self.__motorista == None:
            print("fail: moto sem motorista")
            return
        if self.__passageiro != None:
            print("fail: moto ja tem passageiro")
            return
        self.__passageiro = passageiro


    def descer(self):
        if self.__passageiro == None:
            print("fail: moto sem passageiro")
            return None
            passageiro = self.__passageiro
            pagamento = min(passageiro.getDinheiro(), self.__custo)
            passageiro.setDinheiro(passageiro.getDinheiro() - pagamento)
            self.__motorista.setDinheiro(self.__motorista.getDinheiro() + self.__custo)
            resultado = f"{passageiro.getNome()}:{pagamento} left"
            self.__passageiro = None
            self.__custo = 0
            self.__kmviagem = 0
            return resultado

    def dirigir(self, km:int):
        if self.__motorista == None:
            print("fail: moto sem motorista")
            return
        if self.__passageiro == None:
            print("fail: moto sem passageiro")
            return
        self.__kmviagem += km
        self.__custo += km

    def __str__(self):
        return f"Cost: {self.__custo}, Driver: {self.__motorista}, Passenger: {self.__passageiro}"

def main():
    moto = Moto()

    while True:
        line = input()
        print("$" + line)
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(moto)
        elif args[0] == "setDriver":
            nome = args[1]
            dinheiro = int(args[2])
            motorista = Pessoa(nome, dinheiro)
            moto.setDriver(motorista)
        elif args[0] == "setPass":
            nome = args[1]
            dinheiro = int(args[2])
            passageiro = Pessoa(nome, dinheiro)
            moto.setPass(passageiro)
        elif args[0] == "drive":
            km = int(args[1])
            moto.dirigir(km)
        elif args[0] == "leavePass":
            resultado = moto.descer()
            if resultado != None:
                print(resultado)

main()
