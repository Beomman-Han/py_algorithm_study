# class A -> class Z A를 Z가 상속

# A : 부모 클래스 수퍼클래스 상위 클래스
# Z : 자식 클래스 서브클래스 하위 클래스 

#   ㅁ  <-  ㅁ    
#   부모    자식


class Father():
    def run(self):
        print("so fast!!")

class Mother():
    def dive(self):
        print("so deep!")

class Son(Father, Mother):    #Father class를 상속 하는 Son class
    def run(self):  #메소드 오버라이딩, Father 클래스의 run 메소드를 가림(오버라이딩 함 )  -> 기능 보강을 위하여 
        print("so fast, Son style")
    def jump(self):
        print("so high!")


def main():
    s = Son()
    s.run()
    s.jump()
    s.dive()

main()