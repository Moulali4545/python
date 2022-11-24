class Course:
    def __init__(self,name,ratings):
        self.name=name
        self.ratings=ratings
    def average(self):  #Instance Method
        numberofratings=sum(self.ratings)/len(self.ratings)
        print("Average of ratings of",self.name ,"is:",numberofratings)
        return numberofratings
c1=Course('python',[1,2,3,4,5])
print(c1.name)
print(c1.average())
