from collections import namedtuple

Tri = namedtuple('Triangle', ['bottom','height'])

t = Tri(3,7)

print(t[0],t[1])

print(t.bottom, t.height)

print(Tri)

#named tuple 권장 사용법

tri = namedtuple("tri", ["bottom","top"])  # == tri = namedtuple("tri", "bottom top")

t2 =tri(10,200)
print(tri)
print(t2)


# namedtuple도 언패킹 가능

a,b = t2

print(a,b)


# * 묶는다, 함수 호출시 사용되면 언패킹 기능 
