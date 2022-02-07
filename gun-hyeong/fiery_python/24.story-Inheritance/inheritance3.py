class Car:
    """
    practice class

	Methods
	-------
	__init__ : 초기화
	drive() : 운전 메소드
    add_fuel(f) : 연료 충전 
    show_info() : 차량 번호와 현재 남은 연료 상태 출력 

	"""
    def __init__(self,id,f):
        """초기화 함수
        Arguments:
            id {["Sting"]} -- [description]
            f {["int"]} -- [description]
        """
        self.id = id
        self.fuel = f

    def drive(self) -> None :
        """
        함수 호출시, 연료 -10 만큼 감소 
        return -> None
        """
        self.fuel -= 10
    def add_fuel(self, f) -> None :
        self.fuel += f
    def show_info(self) -> None :
        print("id : ", self.id)
        print("fuel: ", self.fuel)

class Truck(Car):
    def __init__(self, id, f, c):
        super().__init__(id, f)
        self.cargo = c
    def add_cargo(self,c):
        self.cargo += c
    def show_info(self): # 메소드 오버라이딩
        super().show_info()
        print("cargo :", self.cargo)


def main():
    t = Truck("42가 2311", 0, 0)
    t.add_fuel(100)
    t.add_cargo(50)
    t.drive()
    t.show_info()


main()