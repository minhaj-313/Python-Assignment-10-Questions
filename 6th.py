# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name + " makes a sound.")

# Child class (inheritance type: single inheritance)
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        print(self.name + " barks.")

# Child class (inheritance type: multi-level inheritance)
class GoldenRetriever(Dog):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        print(self.name + " barks and wags its tail.")

# Child class (inheritance type: multiple inheritance)
class Bird:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name + " chirps.")

class Parrot(Bird, Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(self.name + " repeats words.")

# create objects of each class
animal = Animal("Animal")
dog = Dog("Dog")
golden = GoldenRetriever("Golden Retriever")
bird = Bird("Bird")
parrot = Parrot("Parrot")

# call the speak method of each object
animal.speak()
dog.speak()
golden.speak()
bird.speak()
parrot.speak()
