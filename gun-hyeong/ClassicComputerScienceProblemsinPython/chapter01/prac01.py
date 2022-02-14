#문제 : 자신의 설계 기법을 사용하여 피보나치 수열의 항목 n을 구하는 또 다른 함수를 작성하라. 
#이장의 피보나치 수열 코드와 비교하여 정확성과 성능을 평가하는 단위 테스트도 작성하라

def gun_fibo(n: int) -> int:
    set1 = set()
    
    try:
        if n < 2 :
            set1.add(n)
        else:
            set1.add(gun_fibo(n-1) + gun_fibo(n-2))
    except:
        pass
    return sum(set1)


a = gun_fibo(0)    
print(a)
