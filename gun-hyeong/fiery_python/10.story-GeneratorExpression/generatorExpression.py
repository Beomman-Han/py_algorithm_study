def two():
    print("two")
    return 2


g = ( two() * i for i in (range(1,11)))

print(g)


for i in g:
    print(i)



def show_all(s):
    for i in s:
        print(i,end=' ')

show_all(x * 2 for x in range(1,11))