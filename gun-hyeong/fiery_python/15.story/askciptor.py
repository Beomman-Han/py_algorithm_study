# *묶는다, 그러나 함수 호출하면서 인자를 전달할떄는 푼다.

def who(a,b,c):
    print(a,b,c)

who(*[1,2,3]) # iterable 객체
who(*'abc') # ITERABLE 객체

dic = dict(a=1,b=2,c=3)


who(*dic)
who(**dic)
who(*(dic.items() ))


#함수 정의시
# * 튜플로 묶는다
# ** 딕셔너리도 묶는다.


def test(**a):
    print(a)


##test({'a':1,'b':2})
test(a=1,b=2,c=3.)