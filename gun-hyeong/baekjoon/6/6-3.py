n = int(input())
han = 0
for i in range(1,n+1):
    if i < 100 :
        han += 1
    else :
        if int(str(i)[1]) - int(str(i)[0]) == int(str(i)[2]) - int(str(i)[1]):
            han += 1
print (han)
