class Duck:
    def talk(self):
        print("Quack")
class Human:
    def talk(self):
        print("Hello")
def callTalk(obj):
    obj.talk()
d=Duck()
callTalk(d)

h=Human()
callTalk(h)

#Dependency injection in duck typing
class Flight:
    def __init__(self,engine):
        self.engine=engine
    def startEngine(self):
        self.engine.start()
class BoeingEngine:
    def start(self):
        print("Starting Boeing Engine")
class AirbusEngine:
    def start(self):
        print("Starting Airbus Engine")
b=BoeingEngine()
f=Flight(b)
f.startEngine()
ae=AirbusEngine()
f=Flight(ae)
f.startEngine()
# Flight(BoeingEngine).startEngine()