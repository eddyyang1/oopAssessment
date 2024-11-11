class Cat:
    def make_sound(self):
        print("Meow!")

class Dog:
    def make_sound(self):
        print("Bark!")

def animal_sound(animal):
    animal.make_sound()

# Demonstration
cat = Cat()
dog = Dog()
animal_sound(cat)
animal_sound(dog)
