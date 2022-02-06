## method overriding
## method overloading, overriding (python does not support method overloading)
## super()

class Father(object):
    def run(self):
        print('so fast, dad style')
    
class Son(Father):
    def run(self):
        print('so fast, son style')

def main():
    s = Son()
    s.run()
main()