from collections import OrderedDict

d= {}

d['a'] = 1
d['b'] = 2

#dict : 저장순서를 정보로 인정하지 않음
#Ordereddict : 저장순서를 정보로 인정함 

d1 = dict(a=1,b=2,c=3)
d2 = dict(b=2,a=1,c=3)

print(d1==d2)

od1 = OrderedDict(a=1,b=2,c=3)
od2 = OrderedDict(b=2,a=1,c=3)


print(od1 == od2) # False

od1.move_to_end('b',last=False)

print(od1 == od2) # True
