x = 3.0 

type(x)

print(dir(x))

print(x.is_integer())

def fct_fac(n):
    def exp(x):
        return x ** n
    return exp

f2 = fct_fac(2)

print(f2(3))

def show(s):
    print(s)

ref = show

ref("ho")

ref = lambda s: print(s)

ref("hi")


f1 = lambda n1, n2: print(n1+n2) 
f1(1,2)


def fct_fac(n) :
    return lambda x : x ** n 

f2 = fct_fac(2)

print(f2(4))
