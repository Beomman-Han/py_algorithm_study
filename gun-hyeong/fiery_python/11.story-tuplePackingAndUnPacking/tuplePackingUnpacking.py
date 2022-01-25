#튜플과 리스트의차이
#mutable(리스트), Imutable(튜플)의 차이  
#튜플이 메모리를 적게 사용 


#튜플 패킹
tri_one = (12,13)
tri_two = 12,13

print(tri_one, type(tri_one))
print(tri_two, type(tri_two))


#튜플 언패킹
one,two = tri_one

print(one,two)



nums = (1,2,3,4,5)
a,b, *c = nums  #일부를 리스트로 묶을때 *를 사용함   <-> 매개변수 앞에 붙는 * : 나머지 값들은 튜플로 묶어서 이 변수에 저장하겠다.

print(a,b,c)

a, *b, c = nums  
print(a,b,c)

*a,b,c= nums
print(a,b,c)


#언패킹 작업은 튜플뿐만 아니라 리스트에서도 작용한다 .

nums = [1,2,3,4,5]
a,b, *c = nums  #일부를 리스트로 묶을때 *를 사용함

print(a,b,c)

a, *b, c = nums  
print(a,b,c)

*a,b,c= nums
print(a,b,c)


#함수 호출 및 반환 과정에서의 패킹과 언패킹 
#패킹과 언패킹은 함수의 호출과 반환 과정에서도 일어남 

def ret_nums():
    return 1,2,3,4,5
a,*b = ret_nums()
print(a,b)

def show_nums(a,b,*c):
    print(a,b,c, end=" ")

show_nums(1,2,3,4,5,6)
print()
def sum(*nums):
    s = 0
    for i in nums:
        s += i
    return s

#매개변수에 * => 튜플로 패킹
#함수호출시 * => 언패킹 

print(sum(1,2,3))

def priNt(name,age,height):
    print(name,age,height , sep=",")

priNt("이건형", "30", 166)

man1 = ("lee","30",170)
priNt(*man1)

#튜플 안의 튜플 언패킹

t= (1,2,(3,4))

a,b,(c,d) = t

print(a,b,c,d,sep=",")



#튜플의 소괄호 생략한 경우도 마찬가지 

t= 1,2,(3,4)
a,b,(c,d) = t

print(a,b,c,d,sep=",")


p = "Hong",(32,178),"010-1234-5678","Korea"

na,(_,he),_,_ = p  # _ 도 변수임

print(na,he,_)


#for 루프에서의 언패킹
list1 = [(1,2),(3,4),(5,6)]

for x,y in list1:   #언패킹 
    print(x,y,sep=",")