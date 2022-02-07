from tkinter import N


class Natural(object):
    """chapter30 property practice"""

    N = 10

    def __init__(self, n: int) -> None:
        self.setn(n)

    n = property()

    def getn(self) -> int:
        """get self.__n"""
        return self.__n
    
    n = n.getter(getn)

    def setn(self, n: int) -> None:
        """set self.__n"""
        if(n < 1):
            self.__n = 1
        else:
            self.__n = n
        return
    
    n = n.setter(setn)

def main():
    n1 = Natural(1)
    n2 = Natural(2)
    n3 = Natural(3)
    n1.n = n2.n + n3.n
    print(n1.n)
    print(n1.N)
    print(Natural.N)

main()

