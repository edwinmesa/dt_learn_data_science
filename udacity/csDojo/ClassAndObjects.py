from typing import List

class Robot:
    def __init__(self, name:str, color:str, weight: int) -> List[str]:
        self.name   = name
        self.color  = color
        self.weight = weight

    def introduceSelf(self) -> str:
        print("My Name is " + str(self.name) + ". I am a robot")

    
class Person:
    def __init__(self, name: str, personality: str, isSitting: bool) -> List[str]:
        self.name         = name
        self.personality  = personality
        self.isSitting    = isSitting
         
    def sitDown(self) -> bool:
        self.isSitting = True
    
    def standUp(self) -> bool:
        self.isSitting = False

r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

p1 = Person("Alice", "agressive", False)
p2 = Person("Becky", "talkactive", True)

r1.introduceSelf()
r2.introduceSelf()