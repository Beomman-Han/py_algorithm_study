a = [1,2,3]


a = [x for x in range(1,4)]

print(a)


a = [ x*2 for x in range(1,4) if x % 2]  # 나누어 떨어지면 0 이기에 false 즉, 홀수만 

print(a)


a = [ str(x) + " * " + str(y) + " = " + str(x*y) for x in range(2,9) for y in range(1,10) if (x * y) % 2]  #중첩 for문 

for i in a:
    print(i)                         