# Immutable : 객체가 지닌 값의 수정이 불가능한 객체 - int, float, tuple, str, bool 
# mutable : 객체가 지닌 값의 수정이 가능한 객체 - list, set, dictionary

r = [1,2]
r1 = [1,2]
print(id(r))
r += [3,4]
r2 = r
print(id(r))
print(id(r1))
print(id(r2))

print(r2) #[1,2,3,4]

#값을 새로 할당 할 경우 참조가 변하는지확인
r = [1,2]
print(id(r),id(r2))
##r2 -= [3,4]
##print(id(r2))



def add_last(m,n):
    m += n

add_last(r, [3,4])

print(r, id(r))


### tuple 테스트
print()

tuple1 = tuple()
print(id(tuple1))
tuple1 = (1,3)
tuple2 = (1,3)
print(id(tuple1), id(tuple2))  ## 두변수가 같은객체를 공유함 

add_last(tuple1, (5,7))

print(tuple1, id(tuple1))

list1 = [1,2,3]

list2 = list(list1)
print(id(list1), id(list2))

print(list1, list2)

#bool 테스트 - immutable 객체 

bool1 = True
bool2 = True

print(id(bool1), id(bool2))