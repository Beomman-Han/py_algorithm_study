test_cnt = int(input())
list1 = list()
for i in range(test_cnt):
    a,b =map(int,input().split(" "))
    if ( 0 < a and b < 10):
        list1.append((a,b))
    else:
        print("범위내 수를 입력 하세요 (0 < A, B < 10)")

for i in enumerate(list1):
        print("Case #{} {} + {} = {}".format(i[0]+1,i[1][0],i[1][1],i[1][0]+i[1][1]))

