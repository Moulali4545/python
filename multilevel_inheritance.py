class A:
    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature2 is working")
class B(A):
    def feature3(self):
        print("feature3 is working")
    def feature4(self):
        print("feature4 is working")
class C(B):
    def feature5(self):
        print("feature5 is working")

c=C()
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()