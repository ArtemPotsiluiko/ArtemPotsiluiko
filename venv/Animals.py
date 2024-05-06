class Animal:
    food = "feed"
    paws = "4"
class Dog(Animal):
    sound = "bark"
    name = "Sherlock"

class Cat(Animal):
    sound = "meow"
    name = "Mozart"

Dog = (Dog)
Cat = (Cat)

print("Dog:", Dog.food, Dog.paws, Dog.sound, Dog.name)
print("Cat:", Cat.food, Cat.paws, Cat.sound, Cat.name)
