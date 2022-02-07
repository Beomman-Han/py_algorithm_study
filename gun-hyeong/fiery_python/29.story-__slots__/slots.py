## __slots__

# 이 클래스를 기반으로 생성한 객체의 변수를 xyz로 제한함 


# __slots__ 를 정의하면 객체별로 __dict__ 가 생기지 않는다. 그렇다고 해서 객체별로 __slots__를 하나씩 갖는 것도 아님. 클래스당 하나의 __slots__만 생성됨 

#이는 메모리상의 큰 이득이 있음 



class Point3D:
    __slots__ = ('x','y','z')

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'


def main():
    p1 = Point3D(1, 1, 1)
    #p1.c = 2   #장애발생 
    p2 = Point3D(24, 17, 31)

    print(p1,p2)

main()


###  객체.변수(속성) 의 접근은 사실 __dict__의 해당 키로 값을 가져오는 방법인데, __slots__를 사용할 경우에는 __dict__가 없기에 바로 접근이 가능하고 이는 속도상의 이득이 있다.

