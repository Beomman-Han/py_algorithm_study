from typing import Generator

#변수명이 헷갈려서 이해하기 힘들어 변수명 변경 

def fib6_1(n: int) -> Generator:
    yield 0
    if n > 0 : yield 1
    first: int = 0
    next: int = 1

    for _ in range(1,n):
        first, next = next, first + next #튜플 언패킹
        yield next

if __name__ == "__main__":
    for i in fib6_1(10):
        print(i)

bytes([1,2,3])