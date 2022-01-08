list1 = list()
while True :
    a,b = map(int,input().split(" "))
    if ( a == 0 and b == 0 ) :
        for i in list1:
            print(i[0]+i[1])
        break
    else:
        list1.append((a,b))

