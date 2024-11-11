class Animal:
    def eat(self):
        print("Eating...")

    def sleep(self):
        print("Sleeping...")

class Dog(Animal):
    def bark(self):
        print("Woof!")

# Demonstration
dog = Dog()
dog.eat()
dog.sleep()
dog.bark()
