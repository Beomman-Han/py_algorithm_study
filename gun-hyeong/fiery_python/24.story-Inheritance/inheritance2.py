class Father:
    def run(self):
        print("so fast!, father style")

class Son(Father):
    def run(self):
        print("so fast!, son style")
    def run2(self):
        super().run()



s = Son()

s.run()
s.run2()