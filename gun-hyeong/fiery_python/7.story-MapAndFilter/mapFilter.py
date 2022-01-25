
pow = lambda x: x**2

list1 = [1,2,3]

list2 = map(pow,list1)  ## map은 iterator 객체를 반환함 

print(list2)

l1 = [1,2,3]
l2 = [1,2,3]
l3 = l1 + l2

l3 = map((lambda x,y: x+y),l1,l2)

##람다 함수는 매개변수가 둘이므로 map은 두개의 iterable객체를 요구하게 된다. 

print(next(l3),next(l3),next(l3))


st = [ "one", "two", "three"]

rev = list(map(lambda x: x[::-1] , st))

print(rev)


#filter
# filter(function, iterable) function의 경우에 true false를 반환하는 값들만 
rev1 = list(filter(lambda x: len(x) == 3, st))

print(rev1)

st = range(1,11)

fil = list(filter(lambda y: y % 3 == 0, map(lambda x: x**2,st)))

print(fil)