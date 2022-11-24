class Bus:
    def __init__(self,name,colour,number):
        self.name=name
        self.colour=colour
        self.number=number
    def display(self):
        print(self.name,self.colour,self.number)
class Auto(Bus):
    def __init__(self,name,colour,number,auto_name):
        super().__init__(name,colour,number)
        self.auto_name=auto_name
    def display(self):
       super().display() 
       print(self.auto_name)

a=Auto('Ashok leyland','blue','AP27R3514',"Ape Auto")
a.display()