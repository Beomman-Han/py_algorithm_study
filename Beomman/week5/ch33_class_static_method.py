## Materials
## static method, class method: https://nirsa.tistory.com/113
## why @staticmethod deco need? : https://stackoverflow.com/questions/43587044/do-we-really-need-staticmethod-decorator-in-python-to-declare-static-method
## => if we need to access to staticmethod from instance, @staticmethod need
## f1 = class(); f1.method_wo_deco() # Error; class.method_wo_deco() # Only;

from typing import Type


class Simple(object):
    count = 0

    def method():
        print('method')

    @staticmethod
    def static_method():
        print('static method')
        print(f'{Simple.count}')
    
    @classmethod
    def class_method(cls):
        print('class method')
        print(f'{cls.count}')

    def __init__(self):
        Simple.count += 1
    
    def get_count(self):
        return Simple.count

s1 = Simple()
s2 = Simple()
s3 = Simple()
print(Simple.count)
Simple.method() ## Only
# s1.method() ## Error

class Date(object):
    def __init__(self, year: int, month: int, day: int) -> None:
        self.year = year
        self.month = month
        self.day = day
    
    def show(self) -> None:
        print(f'{self.year}, {self.month}, {self.day}')

    @classmethod
    def next_day(cls, today: Type['Date']) -> Type['Date']:
        return cls(today.year, today.month, today.day + 1)
    
    @staticmethod
    def next_day_sm(today: Type['Date']) -> Type['Date']:
        return Date(today.year, today.month, today.day + 1)


class KDate(Date):
    def show(self) -> None:
        print(f'KOR: {self.year}, {self.month}, {self.day}')


class JDate(Date):
    def show(self) -> None:
        print(f'JPN: {self.year}, {self.month}, {self.day}')


def main():
    # d1 = Date(2025, 4, 5)
    # d1.show()
    # d2 = Date.next_day(d1)
    # d2.show()
    kd1 = KDate(2025, 4, 12)
    kd1.show()
    kd2 = KDate.next_day(kd1)
    kd2.show()
    kd3 = KDate.next_day_sm(kd2)
    kd3.show()

    jd1 = JDate(2027, 5, 19)
    jd1.show()
    jd2 = JDate.next_day(jd1)
    jd2.show()
    jd3 = JDate.next_day_sm(jd2)
    jd3.show()

main()