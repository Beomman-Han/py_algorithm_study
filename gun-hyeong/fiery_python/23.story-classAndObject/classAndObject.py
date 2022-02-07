#객체 내에서 해당 변수를 대상으로 대입 연ㅅ나을 처음 진행하는 순간 객체내에 변수가 생성된다.


#self는 인스턴스 자체를 의미 한다.
class Simple:
    def __init__(self):   # __init__() 메소드는 객체 생성시 호출된다. 따라서 객체 생성시 변수 i를 초기화 해 준다. 
        self.i = 0
    def seti(self,i):
        self.i = i
    def geti(self):
        print(self.i)
        return self.i


s1 = Simple()

#s1.seti(10)
s1.geti()



##객체에 변수와 메소드 붙였다 떼었다 해보기

## 파이썬의 객체에는 변수와 메소드를 붙이기도 하고 떼기도 할 수 있다. 

class SoSimple:
    def geti(self):
        return self.i

ss = SoSimple()
ss.i = 5

print(ss.geti())

ss.hello = lambda : print("hi~")

ss.hello()


## 클래스에 변수 추가하기

# 클래스는 객체와 달리 설계도일 뿐인데 어떻게 변수를 추가할 수 있는가 -> 파이썬의 클래스는 클래스이자 객체이다. 

class simple1:
    def __init__(self, i):   # 질문 seti 아닌지?
        self.i = i

s1 = simple1(2)

print(s1.i)

s1.n = 5 

print(s1.n)

## 프로그래머가 직접 정의하는 클래스들은 type이라는 클래스의 객체이다. 

## 클래스에 속하는 변수를 만들 수 있다. 
## 객체에 찾는 변수가 없으면 해당 객체의 클래스로 찾아가서 그 변수를 찾는다 (type 객체)

print(type)
#타입이 함수라면 <function tpye at ~>의 형태로 출력이 됫을것, 클래스이기 때문에 클래스로 출력

print(type(list)) #리스트 클래스는 사실 type이라는 클래스의 객체

#파이썬의 클래스는 그자체로 객체임 , 변수에 클래스를담을 수 있는 것도 클래스가 객체이기 떄문 


# 빈클래스를 만들면 type클래스의 객체임
class Sim:
    pass


print(type(Sim))



class one:
    pass

o1 = one()
o1.a = 5
print(o1.a)