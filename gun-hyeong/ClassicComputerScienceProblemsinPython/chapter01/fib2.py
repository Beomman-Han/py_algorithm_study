
def fib2(n: int) -> int:
    if n < 2 :
        return n
    print("함수호출")
    return fib2(n-1) + fib2(n-2)

if __name__ == "__main__":
    print((fib2(10)))

