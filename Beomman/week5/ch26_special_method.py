class Coll:
    def __init__(self, d):
        self.curr = 0
        self.d = d
    
    def __iter__(self):
        self.curr = 0
        return self
    
    def __next__(self):
        if len(self.d) <= self.curr:
            raise StopIteration
        else:
            self.curr += 1
            return self.d[self.curr - 1]


def main():
    co = Coll([1, 2, 3, 4, 5])
    for i in co:
        print(i)
    for i in co:
        print(i)
main()