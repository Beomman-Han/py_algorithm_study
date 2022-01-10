list1=[1]

cnt = 2
sum = 1

while list1[len(list1)-1] < 100000000 :
    sum += cnt
    list1.append(sum)
    cnt += 1
list1 = list1[:-1]

input1 = int(input())
for i in range(len(list1)):
    if list1[i] >= input1:
        posit = i+1
        break

max = list1[posit-1]

if posit % 2 == 1:
    bunmo = posit
    bunja = 1
    while max != input1:
        bunmo -= 1
        bunja += 1
        max -= 1
else:
    bunmo = 1
    bunja = posit
    while max != input1:
        bunmo += 1
        bunja -= 1
        max -= 1
print (str(bunja)+"/"+str(bunmo))