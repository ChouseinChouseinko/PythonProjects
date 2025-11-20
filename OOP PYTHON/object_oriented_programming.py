# ObjectOrientedProgramming
class Dog():

    # class object attribute
    # same for any instanceof a class
    species = 'mammal'
    # let's create some attributes

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name

        # expected boolean true or false
        self.spots = spots
    # operation/actions -----> methods

    def bark(self, number):
        print("Woofffff! My name is {} and the number is {}".format(self.name, number))


class Circle():
    # class object attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def get_circumference(self):
        return self.radius * self.pi * 2


# This is for the class Dog()
mydog = Dog(breed='Doberman', name='Max', spots=False)
print(mydog.breed)
print(mydog.species)  # class object attribute
print(mydog.name)
mydog.bark(11)

# This is for the class Circle()
my_circle = Circle(30)
print(my_circle.pi)
print(my_circle.radius)
result = my_circle.get_circumference()
print(result)
