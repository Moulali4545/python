class A:
    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature2 is working")
class B:
    def feature3(self):
        print("feature3 is working")
    def feature4(self):
        print("feature4 is working")
class C(A,B):
    def feature5(self):
        print("feature5 is working")

c=C()
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()



class A:
    def __init__(self):
        print("A in it")
    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature 2 is working")
class B:
    def __init__(self):
        super().__init__()
        print("B init")
    def feature3(self):
        print("feature3 is working")
    def feature4(self):
        print("feature4 is working")
class C(B,A):
    def __init__(self):
        super().__init__()
        print("C init")
    def feature5(self):
        print("feature5 is working")

c=C()
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()