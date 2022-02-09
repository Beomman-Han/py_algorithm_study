from typing import Dict
memo: Dict[int, int] = {0:0, 1: 1} #기저조건

def fib3(n: int) -> int:
    if n  not in memo:
        memo[n] = fib3(n-1) + fib3(n-2) #메모이제이션
    return memo[n]


## 메모이제이션 데커레이터 



