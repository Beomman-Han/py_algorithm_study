class Account:
    def __init__(self,aid, ab1):
        self.aid = aid
        self.ab1 = ab1
    def __add__(self,m):
        self.ab1 += m  # !!!! 다른 객체가 생성됨 += 연산은 기본적으로 v1 + v2 => v1.__add__(v2)와 같음 그렇기에 __iadd__()를 정의해야 맞음

    def __sub__(self,m): ## __add__와 마찬가지 
        self.ab1 -= m 

    
# 메소스 __str__의 정의 

## print() 함수 호출시 __str__ 메소드 호출

class Simple:
    def __init__(self,i):
        self.i = i
    def __str__(self):
        return f'Simple({self.i})' #f-string 활용 , 객체이름 자체를반환 하도록 __str__ 오버로딩 진행, print() 호출시 반영 

s = Simple(10)

print(s)

# in-place 형태의 연산자 오버로딩 

#mutable 객체인가, immutable객체인가에 따라 적절하게 선택하여 사용해야함 

