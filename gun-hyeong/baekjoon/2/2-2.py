score=int(input())
if score < 0 and score > 100:
    print("정확한 점수를 입력하세요 (0~100)")
else:
    if score >= 90 and score <= 100 :
        print("A")
    elif score >= 80 and score < 90 :
        print("B")
    elif score >= 70 and score < 80 :
        print("C")
    elif score >= 60 and score < 70 :
        print("D")
    else:
        print("F")