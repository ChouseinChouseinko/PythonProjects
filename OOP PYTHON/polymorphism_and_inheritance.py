# inheritance
class Animal():

    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

# the dog class can have common methods with the animal class


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def who_am_i(self):
        print("I am a dog")

    def bark(self):
        print("WOOOOFF!")


animal = Animal()
animal.eat()
animal.who_am_i()
dog = Dog()
dog.who_am_i()
dog.eat()
dog.bark()


# POLYMORPHISM
class Dog1():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says wooof!"


class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meooow!"


niko = Dog1("Niko")
felix = Cat("Felix")

print(niko.speak())
print(felix.speak())

for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())


def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)

# Abstract Classes


class Zwa():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError(
            "Subclass must implement this abstract method")


class skilo(Zwa):
    def speak(self):
        return self.name + " says woooof"


class gata(Zwa):
    def speak(self):
        return self.name + " says meeeeeeow"


fido = skilo("Fido")
print(fido.speak())

isis = gata("isis")
print(isis.speak())
