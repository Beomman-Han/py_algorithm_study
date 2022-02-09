from functools import lru_cache

@lru_cache(maxsize=None) #메모제이션 데커레이터 다음에 반환된 값을 메모리에 캐싱한후 다시 동일한 인자와 function이 실행되면 캐시도니 값을 검색하여반환한다.
def fib4(n: int) -> int:
    if(n<2) :
        return n
    else:
        return fib4(n-1) + fib4(n-2)


if __name__ == "__main__":
    print(fib4(10))
    print(fib4(20))


    