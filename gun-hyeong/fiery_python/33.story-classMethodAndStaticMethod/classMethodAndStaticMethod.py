

class Simple:
    cv =10
    def __init__(self):
        self.cv = 20
    def sm(): # static method 생성방법 self를 넣지 않음
        print("static method")
    sm = staticmethod(sm)


    @staticmethod
    def sm():
        print("static method!")

s = Simple()


print(Simple.cv)
print(s.cv)

print(Simple.sm())
print(s.sm())  #None 이왜 생기는지 ?? 


#class 메소드와 static메소드의 차이 상속했을 경우에 class 메소드를 사용하는 것이 더 잘어울린다. 
#변수 cls의 차이 

@staticmethod
def sm(i):
    pass

@classmethod
def cm(cls,i):
    pass 

