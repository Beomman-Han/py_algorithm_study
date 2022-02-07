###########Story23

from inspect import classify_class_attrs
from re import A, M
from timeit import timeit
from tkinter.messagebox import YES


class Simple:
    def __init__(self): #변수초기화
        self.i = 0
    
    def seti(self, i: int) -> None:
        self.i = i
    
    def geti(self) -> int:
        return self.i
    
s = Simple()
s.geti()
print(s.geti())
s.seti(25)


class SoSimple:
    def geti(self):
        return self.i

ss=SoSimple()
ss.i=27
ss.geti()  
print(ss.geti())          
ss.hello = lambda : print('hi~')
ss.hello()

class Simple:
    def __init__(self,i):
        self.i=i
    def geti(self):
        return self.i
Simple.n=7
print(Simple.n)    
s1=Simple(3)
s2=Simple(5)
print(s1.n, s1.geti(), sep=',')
print(s2.n, s2.geti(), sep=',')

print(type) 

class Simple:
    pass

simple2=Simple
s1=Simple()
s2=simple2()
print(s1 is s2)
print(s1 == s2)
print(s1)
print(s2)
s3=simple2()
print(s3)


###########Story24
#father_son.py
class Father:
    def run(self):
        print("so fast")
        
class Son(Father): #상속
    def jump(self):
        print("so high")
        
def main():
    s=Son()
    s.run()
    s.jump()
   
main() 

#parent_son.py
class Mother:
    def dive(self):
        print("so deep")

class Son(Father,Mother):
    def jump(self):
        print("so high")

def main():
    s=Son()
    s.run()
    s.dive()
    s.jump()
main()


#father_son3.py
class Father:
    def run(self):
        print("so fast, dad style")
        
class Son(Father):
    def run(self):
        print("so fast,son style")
    def run2(self):
        super().run()
        
def main():
    s=Son()
    s.run()
    s.run2()
main()

#car.py
class Car:
    def __init__(self,id,f):
        self.id=id #차량번호
        self.fuel=f #연료
    def drive(self): #주행
        self.fuel-=10 #연료감소
    def add_fuel(self,f):
        self.fuel += f #연료보충
    def show_info(self): #차 상태출력
        print("id:",self.id)
        print("fuel:",self.fuel)

#truck.py
class Truck(Car):
    def __init__(self, id, f, c): #상속받은 값 초기화
        super().__init__(id, f)
        self.cargo=c #짐 
    def add_cargo(self,c):
        self.cargo += c #짐 추가
    def show_info(self):
        super().show_info()
        print("cargo:",self.cargo)

def main():
    c=Car("32러5234",0)
    c.add_fuel(100)
    c.drive()
    t=Truck("42럭5959",0,0)
    t.add_fuel(100)
    t.add_cargo(50)
    t.drive()
    c.show_info()
    t.show_info()
main()


##########Story25
class Simple:
    pass

simple2=Simple
s1=Simple()
s2=simple2()
print(s1 is s2)
print(s1 == s2)
print(s1)
print(s2)
s3=simple2()
print(s3)

print(isinstance(s1,Simple))  #True
print(isinstance(s2,Simple))  #True
print(isinstance(s3,Simple))  #True

class Simple:
    pass

class Simple2(Simple):
    pass

print(isinstance(Simple,object)) #True
print(isinstance(Simple,object)) #True
print(issubclass(Simple2,Simple)) #True
print(issubclass(Simple2,object)) #True
print(issubclass(type,object)) #True
print(issubclass(object,type)) #False



##########Story26
#car_special.py
class Car:
    def __init__(self,id):
        self.id = id
    def __len__(self):
        return len(self.id)
    def __str__(self):
        return 'Vehicle number:' + self.id
    
def main():
    c=Car("32러5234")
    print(len(c))
    print(str(c))

main()


#car_iterable.py
class Car:
    def __init__(self,id) :
        self.id=id
    def __iter__(self):
        return iter(self.id)
    
def main():
    c=Car("32러5234")
    for i in c:
        print(i, end=' ')
    print()    
main()

#my_iterator.py
class Coll:
    def __init__(self,d):
        self.ds=d
        self.cc=0
    def __next__(self):
        if len(self.ds)<=self.cc:
            raise StopIteration
        self.cc += 1
        return self.ds[self.cc -1]
    
def main():
    co=Coll([1,2,3,4,5])
    while True:
        try:
            i=next(co)
            print(i, end=' ')
        except StopIteration:
            print()
            break
main()

Coll=iter([1,2,3,4,5])
print(next(Coll))
print(next(Coll))

#my_iterator2.py
class Coll2:
    def __init__(self,d):
        self.ds=d
    def __next__(self):
        if len(self.ds)<=self.cc:
            raise StopIteration
        self.cc += 1
        return self.ds[self.cc -1]
    def __iter__(self):
        self.cc=0
        print('__iter__호출됨')
        return self
    
def main():
    co=Coll2([1,2,3,4,5])
    for i in co:
            print(i, end=' ')
            print()
    for i in co:
            print(i, end=' ')
            print()
    for i in co:
            print(i, end=' ')
            print()

main()


#############Story27
n1=3
n2=5
print(n1+n2) #8

s1='Y'
s2='eon'
print(s1+s2) #Yeon

l1=[1,2]
l2=[3,4]
print(l1+l2) #[1,2,3,4]

t1=(1,2)
t2=(3,4)
print(t1+t2) #(1,2,3,4)

#vector_add.py
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,o):
        return Vector(self.x+o.x, self.y+o.y)
    def __call__(self):
        return 'Vector({0},{1})'.format(self.x,self.y)
    
def main():
    v1=Vector(3,3)
    v2=Vector(7,7)
    v3=v1+v2
    print(v1())
    print(v2())
    print(v3())
    
main()

#vector_str.py
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,o):
        return Vector(self.x+o.x, self.y+o.y)
    def __str__(self):
        return 'Vector({0},{1})'.format(self.x,self.y)
    
def main():
    v1=Vector(3,3)
    v2=Vector(7,7)
    v3=v1+v2
    print(v1)
    print(v2)
    print(v3)
    
main()


n=[1,2]
n += [3]
print(n)

#vector_inp1.py
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,o):
        return Vector(self.x+o.x, self.y+o.y)
    def __str__(self):
        return 'Vector({0},{1})'.format(self.x,self.y)
    
def main():
    v1=Vector(2,2)
    v2=Vector(7,7)
    print(v1,id(v1))
    v1 += v2
    print(v1,id(v1)) #다르다
    
main()

#vector_inp2.py
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,o):
        return Vector(self.x+o.x, self.y+o.y)
    def __iadd__(self,o):
        self.x += o.x
        self.y += o.y
        return self
    def __str__(self):
        return 'Vector({0},{1})'.format(self.x,self.y)
    
def main():
    v1=Vector(2,2)
    v2=Vector(7,7)
    print(v1,id(v1))
    v1 += v2
    print(v1,id(v1)) #같다
    
main()

#account.py
class Account:
    def __init__(self,aid,abl):
        self.aid=aid
        self.abl=abl
    def __iadd__(self,m):
        self.abl += m
        return self
    def __isub__(self,m):
        self.abl -= m
        return self
    def __str__(self):
        return '{0},{1}'.format(self.aid,self.abl)
    
def main():
    acnt=Account('James01',100)
    acnt += 130
    print(acnt,id(acnt)) #id 같다 왜??
    acnt -= 50
    print(acnt,id(acnt))
    
main()



########Story28
#person3.py
class Person:
    def __init__(self,n,a):
        self.__name = n
        self.__age = a
    def add_age(self,a):
        if(a<0):
            print('나이정보오류')
        else:
            self.__age += a
    def __str__(self):
        return '{0}:{1}'.format(self.__name,self.__age)
        
def main():
    p=Person('James',22) 
    #p.__age +=1
    p.add_age(1)
    print(p)
    print(p.__dict__)
    p.name="jeon"
    p.age=30
    print(p.__dict__) #딕셔너리
        
main()


#############Story29
#point_slots.py
import timeit
class Point3D:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return '{0},{1},{2}'.format(self.x,self.y,self.z)
    
def main():
    start=timeit.default_timer()
    p=Point3D(1,1,1)
    for i in range(3000):
        for i in range(3000):
            p.x+=1
            p.y+=1
            p.z+=1
    print(p)
    stop=timeit.default_timer()
    print(stop-start)
    
main()

class Point3D:
    __slots__=('x','y','z')
    
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return '{0},{1},{2}'.format(self.x,self.y,self.z)
    
def main():
    start=timeit.default_timer()
    p=Point3D(1,1,1)
    for i in range(3000):
        for i in range(3000):
            p.x+=1
            p.y+=1
            p.z+=1
    print(p)
    stop=timeit.default_timer()
    print(stop-start)
    
main()

#############Story30
#natural3.py
class Natural:
    def __init__(self, n):
        self.setn(n)
        
    def getn(self):
        return self.__n
    
    def setn(self,n):
        if(n<1):
            self.__n = n
        else:
            self.__n = n
            
    n=property(getn, setn) #property 생성
    
    
def main():
    n1=Natural(1)
    n2=Natural(2)
    n3=Natural(3)
    n1.n=n2.n+n3.n
    print(n1.n)

main()

#natural6.py
class Natural:
    def __init__(self, n):
        self.n = n
    @property
    def n(self):
        return self.__n
    
    @n.setter
    def n(self, n):
        if(n < 1):
            self.__n = 1
        else:
            self.__n = n

def main():
    n1=Natural(1)
    n2=Natural(2)
    n3=Natural(3)
    n1.n=n2.n+n3.n
    print(n1.n)
    
main()

################Story31
def maker(m):
    def inner(n):
        return m * n
    return inner

f1 = maker(2)
f2 = maker(3)
print(f1(7))
print(f2(7))
print(f1.__closure__[0].cell_contents) #closure

##############Story32
def smile():
    print("^_^")
    
smile()

def deco(func) :
    def df() :
        print('emotion!')
        func()
        print('emotion!')
    return df

smile = deco(smile)
smile()

def adder2(n1,n2):
    return n1+n2
    
adder2(3,4)

def adder_deco(func):
    def ad(*args):
        print(*args,sep=' + ', end=' ')
        print("= {0}".format(func(*args)))
    return ad

adder2=adder_deco(adder2)
adder2(3,4)


#deco_style.py
def adder_deco(func):
    def ad(*args):
        print(*args,sep=' + ', end=' ')
        print("= {0}".format(func(*args)))
    return ad

@adder_deco  #adder2=adder_deco(adder2)
def adder2(n1,n2):
    return n1+n2

def main():
    adder2(3,4)

main()


###########Story33
class Simple:
    cv=20
    def __init__(self):
        self.iv=10

print(Simple.cv)
#print(Simple.iv) 에러남
s=Simple()
print(s.cv)
print(s.iv)

#count_instance.py
class Simple:
    count=0
    def __init__(self) :
        Simple.count += 1
    def get_count(self) :
        return Simple.count
    
def main() :
    s1=Simple()
    print(s1.get_count())
    s2=Simple()
    print(s2.get_count())
    s3=Simple()
    print(s3.get_count())
    
main()

#static_method.py
class Simple():
    @staticmethod #sm = staticmethod(sm)
    def sm():
        print('static method')

    
def main():
    Simple.sm()
    s=Simple()
    s.sm()
    
main()

#count_instance2.py
class Simple:
    count=0
    def __init__(self):
        Simple.count+=1
        
    @staticmethod
    def get_count():
        return Simple.count
def main():
    print(Simple.get_count())
    s=Simple()
    print(Simple.get_count())
    
main()

#class_method3.py
class Natural:
    def __init__(self,n):
        self.n = n
    def getn(self):
        return self.n
    @classmethod
    def add(cls,n1,n2):
        return cls(n1.getn() + n2.getn())

def main():
    n1=Natural(1)
    n2=Natural(2)
    n3=Natural.add(n1,n2)
    print('{0} + {1} = {2}'.format(n1.getn(),n2.getn(),n3.getn()))
    
main()

#iternational_date.py
class Date:
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d
    def show(self):
        print('{0}, {1}, {2}'.format(self.y, self.m, self.d))    
    @classmethod
    def next_day(cls, today):
        return cls(today.y, today.m, today.d + 1)
    
class KDate(Date):
       def show(self):
           print('KOR: {0}, {1}, {2}'.format(self.y, self.m, self.d))
            
class JDate(Date):
        def show(self):
            print('JPN: {0}, {1}, {2}'.format(self.y, self.m, self.d))
            
def main():
    kd1 = KDate(2025, 4, 12)
    kd1.show()
    kd2 = KDate.next_day(kd1)
    kd2.show()
        
    jd1 = JDate(2027, 5, 19)
    jd1.show()
    jd2 = JDate.next_day(jd1)
    jd2.show()
        
main()

#############Story34

            
            