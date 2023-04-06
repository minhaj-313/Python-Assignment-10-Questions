# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name + " makes a sound.")

# Child class
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        print(self.name + " barks.")

# Child class
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        print(self.name + " meows.")

# create objects of each class
animal = Animal("Animal")
dog = Dog("Dog")
cat = Cat("Cat")

# call the speak method of each object
animal.speak()
dog.speak()
cat.speak()
