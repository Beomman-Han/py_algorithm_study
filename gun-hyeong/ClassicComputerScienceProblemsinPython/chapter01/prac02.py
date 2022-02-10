# 파이썬 int 타입을 사용하여 단순히 비트 문자열을 표한하는 방법을 살펴봣다. 일반저긍로
# 일련의 비트로 사용할 수 있는 int 타입 래퍼 클래스를 작성하라. (iterable 하며, __getitem__()메서드를 구현한다.)

from typing import Iterator

class INT:
    def __init__(self,n:int) -> None :
        self.n_bytes = bin(n)
        self.bytes_list = [ x for x in str(self.n_bytes)[2:]]

    def __str__(self):  
        return self.n_bytes

    def __getitem__(self, n: int) -> None:     #인덱싱을 사용하기 위한 메소드 오버라이딩 ?
        return self.bytes_list[n]

    def __iter__(self) -> Iterator:   #iterable 객체 반환을 위한 메소드 오버라이딩 
        return iter(self.bytes_list)

a = INT(10)

for i in a:
    print(i)
print(a[0])

print(a)