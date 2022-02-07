def smile():
    print("^_^")

def confused():
    print("@_@")

smile()
confused()

#데코레이터 : 꾸며주는 역할을 하는 함수 또는 클래스를 말함

def deco(func):
    def df():
        print("emoticon!")
        func()
        print("emoticon!")
    return df

smile = deco(smile)

smile()


#전달인자가 있는경우 

def adder2(n1,n2):
    return n1 + n2

def adder3(n1,n2,n3):
    return n1 + n2 + n3



def adder_deco(func):
    def ad(*args):  #튜플 패킹, 매개변수가 선언되면 전달인자는 그 수에 상관없이 튜플로 묶인다. 
        print(*args, sep = ' + ' , end =' ')
        print(f'= {func(*args)}')
    return ad

adder2 = adder_deco(adder2)

adder2(3,4)

d =(1,2,3)

print(*d, d)


a,*b,c = d 

print(b)



# @기반으로


def deco(func):
    def df():
        print("emoticon!")
        func()
        print("emoticon!")

    return df

def smile():
    print("smile")



@deco
def smile():
    print("smile")

smile()


#데코레이터 함수 두번 이상 통과하기 

# @deco1
# @deco2


