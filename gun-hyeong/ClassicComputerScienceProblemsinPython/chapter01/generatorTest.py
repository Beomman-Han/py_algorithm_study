from typing import Generator


def gen_test(n: int) -> Generator:
    yield 0
    #if n > 0 : yield 1

    for i in range(1,n):
        yield i

#for i in gen_test(3): #내부적으로 어떻게 실행되는지 테스트 for문 밖에 있는 것들은 모두 반환 for문 안에 있는 것들은 for문돌면서 하나씩 반환
#    print(i)



a = gen_test(4)

print(next(a))
print(next(a))
print(next(a))
print(next(a))

