class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print("Some animal sound")
        
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")
        
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")
        
animals=[Dog("Alex"), Cat("Nancy"), Dog("David")]
for animal in animals:
    animal.speak()