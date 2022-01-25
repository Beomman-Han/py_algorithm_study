# 딕셔너리 루핑 테크닉

#dict.keys(), dict.values(), dict.items()   -> view 를 반환함 (딕셔너리를 바라봄)

dic = dict(a=1,b=2,c=3)

print(type(dic.keys())) # ->뷰객체 반환 뷰객체는 iterable 객체


for kv in dic.items():
    print(kv, sep=",")


for k,v in dic.items() : # 튜플 언패킹 
    print(k,v, sep=', ')


#뷰가 바라보는 현제 상태 : 현재 딕셔너리의 상태를 그대로 반영한다. 



#dict 컴프리헨션

d1 = dict(a=1,b=2,c=3)

d2 = {k:v*2 for k,v in d1.items()}

print(d2)

d3 = {k:v for k,v in d1.items() if v % 2 != 0}

print(d3)


ks = ['a','b','c','d']
vs = [1,2,3,4]

d4 = {k:v for k,v in zip(ks,vs)}

print(d4)