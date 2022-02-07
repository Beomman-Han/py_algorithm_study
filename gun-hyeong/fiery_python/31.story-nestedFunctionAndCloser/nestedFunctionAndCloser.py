
def maker(m):
    def inner(n):
        return m * n
    return inner

f1 =maker(2)

print(f1(7))


print(f1.__closure__[0].cell_contents)   #안쪽에 위치한 inner함수가 자신이 필요한 변수의 값을 어딘가에 저장해 놓고 쓰는 테크닉을 closer라고 함다. 