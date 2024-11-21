#data abstraction
#enscapsilation
#polymophis
#inheritance

class Animal():
    def __init__(self,name):
        self.animalname=name
class Cat(Animal):
        def speak(self):
            print("meow")
class Cow(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        self.animal_age=age
    def speak(self):
        print("moo")

obj1=Animal("budyy")
obj2=Cat("Pinky")
#obj3=Cow("Daisy")
obj4=Cow("Daisey","10")
obj2.speak()
#obj3.speak()
print(obj4.animal_age)

























































