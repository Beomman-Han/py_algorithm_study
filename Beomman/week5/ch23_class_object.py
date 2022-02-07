class Car:
    def __init__(self, id, f):
        self.id = id
        self.fuel = f
    
    def drive(self):
        self.fuel -= 10
    
    def add_fuel(self, f):
        self.fuel += f
    
    def show_info(self):
        print(f'id: {self.id}')
        print(f'fuel: {self.fuel}')


class Truck(Car):
    def __init__(self, id, f, c):
        super().__init__(id, f)
        self.cargo = c
    
    def add_cargo(self, c):
        self.cargo += c

    def add_cargo(self, c, d):  ## overriding
        self.cargo += c
        self.cargo += d

    def show_info(self):
        super().show_info()
        print(f'cargo: {self.cargo}')

def main():
    t = Truck('42럭5959', 0, 1)
    t.show_info()
    t.add_cargo(1)
    t.show_info()
    t.add_cargo(1, 2)
    t.show_info()

main()