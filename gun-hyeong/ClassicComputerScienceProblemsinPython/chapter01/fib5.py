def fib5(n: int) -> int:
        if n == 0 : return 0
        last: int = 0
        next: int = 1
        for _ in range(1,n):
            last, next = next, last + next  # 튜플 언패킹  임시변수를 만들지 않음 
        return next

#last next
# 0    1
# 1    1
# 1    2
# 2    3
# 4    5
#   .
#   .
#   .
#   . 


#제너레이터와 피보나치 수 