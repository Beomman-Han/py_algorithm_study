#a,b=map(int,input().split())
a=int(input())
b=int(input())
if (a < 100 and a > 1000) and ( b < 100 and b > 1000 ):
    print("3자리 자연수를 입력하세요") 
else :
    print(a * int(str(b)[2]))
    print(a * int(str(b)[1]))
    print(a * int(str(b)[0]))
    print(a*b)

