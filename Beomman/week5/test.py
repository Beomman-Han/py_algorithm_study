class Account:
    def __init__(self,aid,abl):
        self.aid=aid
        self.abl=abl
    def __add__(self,m):
        self.abl += m
        return self
    # def __add__(self,m):
    #     self.abl += m
    #     return self
    def __sub__(self,m):
        self.abl -= m
        return self
    # def __sub__(self,m):
    #     self.abl -= m
    #     return self
    def __str__(self):
        return '{0},{1}'.format(self.aid,self.abl)
    
def main():
    acnt=Account('James01', 100)
    print(acnt, id(acnt))
    acnt += 130
    print(acnt, id(acnt)) #id 같다 왜??
    acnt -= 50
    print(acnt, id(acnt))
    
main()