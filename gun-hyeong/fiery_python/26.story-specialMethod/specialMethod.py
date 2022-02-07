#스페셜 메소드 : 약속된 메소드 - > 호출시점이 약속된 메소드 

t= (1,2,3)
len(t) # t.__len__()

itr = iter(t) # itr.__iter__()



#클래스에 스페셜 메소드 정의하기

class Car:
    def __init__(self, id):
        self.id = id

    def __len__(self):
        return len(self.id) 
    def __str__(self):
        return 'Vehicle number :' + self.id

def main():
    c = Car("!23")

    print(len(c))
    print(c) #왜 str()이 출력되는지? 질문   -> 프린트는 무조건 문자열로 바꾸기 때문 (str 함수 사용 )
main()


## iterable 객체가 되게끔 하기

#iterable 객체 iter함수에 인자로 전달가능한 객체, 그결과로 iterator객체 반환
#iterator 객체 next함수의 인자로 전달 가능한 객체    

class Car:
    def __init__(self,id):
        self.id = id

    def __iter__(self):
        return iter(self.id)  #String 객체에 있는 __init__() 스페셜 메소드 호출한 결과를 리턴



def main():
    c = Car("32러5234")
    for i in c:
        print(i,end =" ")


main()

print()

#iterator 객체가 되게끔 하기
# __next__ 메솓를 갖고 있으면 된다.

# 조건1: 가지고 있는 값을 하나씩 반환한다
# 조건2: 더이상 반환할 값이 없는 경우 StopInteration 예외를 발생시킨다.


class Coll:
    def __init__(self,d):
        self.ds = d
        self.cc = 0
    
    def __next__(self):
        if len(self.ds) <= self.cc :
            raise StopIteration
        self.cc += 1
        return self.ds[self.cc - 1 ]  #내부적으로 next가 이런식으로 구현이 되어있는지 ?
    
    

def main():
    co = Coll([1,2,3,4])
    while True:
        try:
            print(next(co))
        except StopIteration:
            break
main()


#iterator 객체이자 iterable객체가 되게끔 하기 

class Coll2:
    def __init__(self,d):
        self.ds = d

    def __next__(self):
        if len(self.ds) <= self.cc :
            raise StopIteration
        self.cc += 1
        return self.ds[self.cc - 1 ]

    def __iter__(self):  #객체 자체를 반환 그 객체는 next 스페셜 메소드를 가지고 있으므로 iterator 객체임   # iterable객체 : iter함수의 인자가 될 수 있는 객체 
        self.cc = 0
        return self