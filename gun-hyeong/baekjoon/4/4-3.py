n = int(input())
n1 = n
cycle = 0

if n >= 0 and n <= 99 :
    if n < 10 :
      n = n*11
      cycle += 1
    while True:
        n = int((n / 10 + n % 10) % 10) + ((n % 10) * 10)
        cycle +=1
        if (n == n1):
            break
    print(cycle) 