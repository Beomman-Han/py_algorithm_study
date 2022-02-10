#하노이탑 문제에서 탑 수에 상관없이 작동하는 코드를 작성하라.

#스택 구현 
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
