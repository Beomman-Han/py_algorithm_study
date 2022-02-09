#파이 계산 하기 

#수식을 코드로 -> 기계변환 ()


def calculate_pi(n_terms: int) -> float:
    numerator: float = 4.0         #분자 (고정)
    denominator: float = 1.0       #분모 (2씩 증가)
    operation: float = 1.0         #(한번은 더하고 한번은 뺴고)
    pi: float = 0.0

    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *=  -1.0
    return pi



if __name__ == "__main__":
    print(calculate_pi(100000000))
