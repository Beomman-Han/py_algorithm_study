class Natural:
    def __init__(self,n):
        self.setn(n)
    def getn(self):
        return self.__n
    def setn(self,n):
        if (n<1):
            self.__n = 1
        else:
            self.__n = n
    n = property(getn,setn)
    #속성의 값을 참조하는 경우에는 getn을 호출해서 반환되는 값을 전달하겠다.
    #속성의 값을 저장하는 경우에는 setn을 호출해서 그 값을 전달 하겠다 .

def main():
    n1 = Natural(1)
    n2 = Natural(2)
    n3 = Natural(3)

    n1.setn(n2.getn() + n3.getn())
    n1.n = n2.n + n3.n
    print(n1.getn())
    print(n1.n)

main()

class Natural:
    def __init__(self,n):
        self.n = n
    @property
    def s(self): # 메소드 이름 관련 질문 !!!!
        return self.__n
    @s.setter
    def s(self, n):
        if (n < 1):
            self.__n = 1
        else:
            self.__n = n

def main():
    n1 = Natural(1)
    n2 = Natural(2)
    n3 = Natural(3)
    n1.n = n2.n + n3.n
    print(n1.n)
main()