#제너레이터 함수
#제너레이터 표현식 

def gen_num():
    print("first Num")
    yield 1
    print("second Num")
    yield 2
    print("third Num")
    yield 3

gen = gen_num()


print(type(gen))

print(next(gen))

next1 = next(gen)

print(next1)
print(next1)




## next를 사용하지 않았는데 왜 값이 만들어지나 ?
def gpows(s):
    print("gpows")
    for i in s:
        yield i ** 2

st =gpows([1,2,3,4,5,6,7,8,9])



print(st)

for i in st:
    print(i)


#yield from

def get_nums():
    ns = [0,1,0,1,0,1]
    for i in ns:
        yield i

sd = get_nums()

print(sd)

for i in sd:  ## for문에서 다음 인자로 넘어간 것과 next() 가 동일한가 ?
    print(i)


def get_nums():
    ns = [0,1,0,1,0,1]
    yield from ns


sd = get_nums()

print(next(sd))


def test():
    yield 1
    yield 2
    yield 3

t1 = test()

for i in t1:
    print(i)
t1 = test()
print(next(t1))