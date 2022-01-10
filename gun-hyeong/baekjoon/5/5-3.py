a = int(input())
b = int(input())
c = int(input())

multi = str(a * b * c)
list=[0,0,0,0,0,0,0,0,0,0]
for i in range(len(multi)):
    list[int(multi[i])] += 1

for i in list:
    print (i)