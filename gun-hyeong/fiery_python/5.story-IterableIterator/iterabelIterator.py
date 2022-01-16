#iterable : iter 함수에 인자로 전달 가능한 객체
#iterator : iter 함수가 생성해서 반환하는 객체 ( 리스트, 튜플, 문자열 ) 

ds = [1,2,3]

ir = iter(ds)

print(next(ir), next(ir), next(ir))

## 스페셜 메소드 
ir = ds.__iter__()   # ==     ir = iter(ds)
print(ir.__next__(), ir.__next__(), ir.__next__())

tp = (1,2,3)

tp_ir = iter(tp)

print(next(tp_ir))

print(dir(list()))   ## dir 함수 : 메소드 확인 함수 
print(hasattr(list(), "__iter__")) # hasattr : 특정 메소드확인 함수 

#for : for문의 반복 대상은 반드시 iterable객체여야 한다.

for i in [1,2,3]:
    print(i)

# == 

ir = iter([1,2,3])
while True :
    try :
        i = next(ir)
        print(i, end=" ")
    except StopIteration :
        break


## iterator 객체도 iter 함수에 인자가 될수 있다. iterator 객체그대로를 반환 한다. 

list1 = [1,2,3]
ir = iter(list1)

ir1 = iter(ir)

print(ir is ir1)