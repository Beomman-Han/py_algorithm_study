input1 = int(input())

for i in range(input1):
    apartment = [[0 for rows in range(14)] for cols in range(15)]
    apartment[0] = [x for x in range(1, 15)]
    k = int(input())
    n = int(input())
    for t in range(1,k+1):
        for j in range(n):
            for z in range(1+j):
                apartment[t][j] += apartment[t-1][z]
    print(apartment[k][n - 1])