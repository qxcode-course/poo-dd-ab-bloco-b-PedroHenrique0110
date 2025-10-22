class Watch:
    def __init__(self, hora: int, minuto: int, segundo: int):
        self.__hora = 0
        self.__minuto = 0
        self.__segundo = 0
        self.setHora(hora)
        self.setMinuto(minuto)
        self.setSegundo(segundo)

    def getHora(self):
        return self.__hora

    def getMinuto(self):
        return self.__minuto

    def getSegundo(self):0
        return self.__segundo

    def setHora(self, hora: int):
        if hora < 0 or hora > 23:
            print("fail: hora invalida")
        else:
            self.__hora = hora

    def setMinuto(self, minuto: int):
        if minuto < 0 or minuto > 59:
            print("fail: minuto invalido")
        else:
            self.__minuto = minuto

    def setSegundo(self, segundo: int):
        if segundo < 0 or segundo > 59:
            print("fail: segundo invalido")
        else:
            self.__segundo = segundo

    def __str__(self):
        return f"{self.getHora():02}:{self.getMinuto():02}:{self.getSegundo():02}"

    def nextSecond(self):
        self.__segundo += 1
        if self.__segundo == 60:
            self.__segundo = 0
            self.__minuto += 1
            if self.__minuto == 60:
                self.__minuto = 0
                self.__hora += 1
                if self.__hora == 24:
                    self.__hora = 0


def main():
    relogio = Watch(0, 0, 0)

    while True:
        line = input()
        print("$" + line)
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(relogio)
        elif args[0] == "set":
            hora = int(args[1])
            minuto = int(args[2])
            segundo = int(args[3])
            relogio.setHora(hora)
            relogio.setMinuto(minuto)
            relogio.setSegundo(segundo)
        elif args[0] == "next":
            relogio.nextSecond()
        elif args[0] == "init":
            hora = int(args[1])
            minuto = int(args[2])
            segundo = int(args[3])
            relogio = Watch(hora, minuto, segundo)


main()