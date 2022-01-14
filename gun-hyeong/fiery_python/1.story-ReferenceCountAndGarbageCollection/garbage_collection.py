
#변수 s가 문자열 'Garbage Collection'을 참조한다.

s = "Garbage Collection"

#레퍼런스 카운트 : 객체를 참조하는 변수의 수를 가르킴
 # 레퍼런스 카운트가 0 이면 소멸대상이 됨 
list1 = [1,2,3]
list2 = [1,2,3]
list3 = list1

string1 = "123"
string2 = "123"
strign3 = string1

print(id(list1), id(list2), id(list3))

print(id(string1),id(string2),id(strign3))