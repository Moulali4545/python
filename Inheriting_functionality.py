#Inheriting Functionality
class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def start(self):
        print("Starting the car")
    def stop(self):
        print("Stopping the car")


class ThreeSeries(BMW):
    def __init__(self,cruiseControlEnabled,make,model,year):
        BMW.__init__(self,make,model,year)
        self.cruiseControlEnabled=cruiseControlEnabled


ts=ThreeSeries("True",'BMW','328i',2003)
print(ts.cruiseControlEnabled)
print(ts.make)
print(ts.model)
print(ts.year)
ts.start()
ts.stop()