# is 와 == 의 차이

# == : 내용이 같은가
# is : 같은 객체를 참조하는가

# 객체의 타입이 Immutable, Mutable인지에따라 다름 
 
list1 = [1,2,3,"123",[1,2]]
list2 = [1,2,3,"123",[1,2]]

print(1,list1 == list2)  #True
print(2,list1 is list2) # False


string1 = "123"
string2 = "123"

print(3,string1 == string2) #True
print(4,string1 is string2) # True

print(5,list1[3] is string1) #True

#얕은 복사와 깊은 복사




print()




 # 얕은 복사 = immutable, mutable 모두 얕은 복사 진행 
list1 = list(list2)

print(1,list1,list2)
list2[4][1] += 1 
print(2,list1)
list2[4] = [1,2,3]
print(3,list1)
print(4,list2)


print()



 # 깊은 복사 = immutable 얕은복사, mutable 깊은 복사 진행 

import copy
list1 = [1,2,3]
list2 = copy.deepcopy(list1)
list1[2] = 4
print(1,list1,list2)


print()


#????
list1 = [1,2,3]
list2 = list(list1)   # list2 = list1 과 비교 
print(1, id(list1), id(list2))
list2[0] += 1 
print(2, list1,list2)

list1 = [1,2,3,[1,2,3]]  
list2 = list(list1)
print(3, id(list1),id(list2))
print(4, id(list1[3]),id(list2[3]))
print(5, id(list1[0]), id(list2[0]))
list2[3][0] = 2
list2[0] = 2 
print(6,list1,list2)


list1 =[1,2,3,[1,2,3]]
list2 = list1
list2[0] = 2
list2[3][0] = 2
print(7, list1,list2)
print(8, id(list1), id(list2))

list1[3] = 4

print(list1,list2)