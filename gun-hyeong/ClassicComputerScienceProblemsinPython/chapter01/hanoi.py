from typing import TypeVar, Generic, List

T = TypeVar('T')  # T는 어떤 타입이든 될수 있다. 


#stack 구현 
class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []
    def push(self, item: T) -> None:
        self._container.append(item)
    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:   #Stack 객체가 print()함수에 출력될 때 나타나는 내용이다. 
        return repr(self._container)


S = Stack()

S.push(2)
S.push(1)
S.push(5)
S.push("2")
print(S)
S.pop()
print(S)

#################################
num_discs: int = 3

tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()

for i in range(1, num_discs + 1):
    tower_a.push(i)

print(tower_a)


def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n : int) -> None:
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n-1)
        hanoi(begin,end, temp, 1)
        hanoi(temp, end, begin, n-1)

if __name__ == "__main__":
    hanoi(tower_a, tower_b, tower_c, num_discs)
    print(tower_a)
    print(tower_b)
    print(tower_c)