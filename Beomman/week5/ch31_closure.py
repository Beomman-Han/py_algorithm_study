from typing import Callable

def maker(m: int) -> Callable:
    def inner(n: int) -> int:
        return m * n
    return inner

f1 = maker(2)
print(f1.__closure__[0].cell_contents)
f2 = maker(3)
print(f2.__closure__[0].cell_contents)
print(f1(7))
print(f2(7))