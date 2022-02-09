class Person:
    def __init__(self, n,a):
        self._name = n
        self._age = a
    def add_age(self, a):
        if(a<0):
            print("나이정보 오류")
        else:
            self._age += a

    def __str__(self):
        return f'{self._name}: {self._age}'

###########################################################
#__붙이면 왜 접근이 안되는지 ?                                  #
#_ 한개만 붙이면 접근은 가능하나 접근하지말라고 규칙을 정함             # 
###########################################################

def main():
    p = Person("james", 24)
    #p.__age += 1 #?? 왜 ???
    p._age += 1
    p.add_age(1)
    print(p)
    print(p.__dict__)

    p.len = 140
    p.adr ="Korea"
    print(p.__dict__)
main()


class Person:
    def __init__(self,n,a):
        self.__name = n
        self.__age = a


def main():
    p = Person("james", 20)

    print(p.__dict__)

    p._Person__name = "lee" # !!!!!!!!!! 강제로 __으로 했음에도 직접 접근 가능 함 
    print(p.__dict__)
main()