# -*- coding: utf-8 -*-

# isinstance

#상속한다 상속 받는다 헷갈린다 ... 

class Simple:
    pass

s = Simple()
print(isinstance(s, Simple))

print(isinstance([1,2], list))

#상속 하는 경우에도 같은 클래스로 인식

class Fruit:
    pass

class Apple(Fruit):
    pass
 
class SuperApple(Apple):
    pass

sa = SuperApple()
f = Fruit()
print(isinstance(sa, SuperApple))
print(isinstance(sa, Apple))  #Apple 객체를 상속하는 클래스의 객체인가?
print(isinstance(sa, Fruit)) #Fruit 객체를 상속하는 클래스의 객체인가? #간접상속 
print(isinstance(f, SuperApple)) 

#Object 클래스 
#파이썬의 모든 클래스는 object 클래스를 직접 혹은 간접 상속한다.
#모든 클래스는 object클래스의 기능을 모두 갖는다.

print(isinstance(f, object))
print(isinstance(sa, object))

class A:
    pass
class B(A):
    pass

print(issubclass(B,A)) #B가 A를 상속 하는가?

print(issubclass(type, object))