d = {'a' : 1, 'b' : 2, 'c': 3}

print(type({}))


dic = dict([('a',1),('b',2),('c',3)])

print(dic)

# 키가 문자열인 경우
dic = dict(a=1,b=2,c=3)

print(dic)

# 키는 키끼리 값은 값끼리

dic = dict(zip(['a','b','c'],[1,2,3]))

print(dic)

#zip 함수

a= zip([1,2,3],[4,5,6],[7,8,9]) #튜플로 묶여 있어도 가능 
b = zip("123","456","789") #스트링도 가능 

print(a)

for i in b:
    print(i)

dic = dict(zip('abc',[1,2,3]))

print(dic)
