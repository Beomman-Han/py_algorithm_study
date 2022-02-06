## basic decorator concept
from typing import Callable, Tuple


def smile():
    print("^_^")

def confused():
    print("@_@")

def deco(func):
    def deco_func():
        print("emoticon!")
        func()
        print("emoticon!")
    return deco_func

smile = deco(smile)
smile()

confused = deco(confused)
confused()

## decorator for function having parameters
def adder2(n1: int, n2: int) -> int:
    """Adder for two integer"""
    return n1 + n2

print(adder2(2, 5))

def adder_deco(func: Callable) -> Callable:
    def deco_func(*args) -> None:
        print(*args, sep=" + ", end=" ")
        print(f'= {func(*args)}')
    # func = deco_func
    return deco_func

adder2 = adder_deco(adder2)
adder2(2, 5)

def adder3(n1: int, n2: int, n3: int) -> int:
    """Adder for three integer"""
    return n1 + n2 + n3

adder3 = adder_deco(adder3)
adder3(2, 5, 7)

## better syntax
@adder_deco
def adder4(n1: int, n2: int, n3: int, n4: int) -> int:
    return n1 + n2 + n3 + n4

adder4(2, 3, 4, 5)
print(adder4.__name__)

## complex decotator
def start_end_deco(func: Callable) -> Callable:
    def deco_func(*args) -> None:
        print(f'Start {func.__name__}')
        func(*args)
        print(f'End {func.__name__}')
    return deco_func

@start_end_deco
@adder_deco
def adder(*args: Tuple[int]) -> int:
    return sum(args)
adder(1, 2, 3, 4, 5)

# @adder_deco
def adder(*args: Tuple[int]) -> int:
    return sum(args)
adder = adder_deco(adder)
adder = start_end_deco(adder)
adder(1, 2, 3, 4, 5)
