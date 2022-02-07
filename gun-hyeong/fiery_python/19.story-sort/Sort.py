#sort mutable 객체에서만 가능하다

a="bcad"

ns = [3,1,4,2]
ns.sort()
print(sorted(ns, key = lambda x : x))

#정렬기준 -> 함수 객체를 만들어 보낸다

def age(t):
    return t[1]

ns = [('Yoon',33),("lee",12),("Park",29)]


ns.sort(key= lambda x : x[1])

print(ns) 

#sort 함수는 -> 리스트 자체를 수정해버린다. (메소드)
#sorted 함수 -> 새로운 객체를 생성 (immutable 객체도 사용이 가능하다)

st_ns = sorted(ns, key = lambda x : x[1])

#sorted 함수는 정렬된 사본을 새로 생성하기 때문에 iterable 객체면 무었이든 전달 할 수 있다. (리스트로 반환 한다.)
