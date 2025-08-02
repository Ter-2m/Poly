# This program demonstrates polymorphism in Python.
# Polymorphism allows objects of different classes to be treated as objects
# of a common type, while each object can respond to the same method call
# in its own specific way. In this example, we have a list of animals and
# vehicles, and we call the `move()` method on each one. Even though the
# method call is the same, the output is different for each object.

# --- Define the Classes ---

class Car:
    """A class representing a car."""
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        """Defines how the car moves."""
        print(f"The {self.make} {self.model} is Driving 🚗")

class Plane:
    """A class representing a plane."""
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name

    def move(self):
        """Defines how the plane moves."""
        print(f"The {self.brand} {self.name} is Flying ✈️")

class Dog:
    """A class representing a dog."""
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def move(self):
        """Defines how the dog moves."""
        print(f"{self.name} the {self.breed} is Running 🐕")

class Cat:
    """A class representing a cat."""
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def move(self):
        """Defines how the cat moves."""
        print(f"{self.name} the {self.breed} is Pouncing 🐈")

# --- Create Instances of the Classes ---

# Create a list that can hold objects of different types
# (Car, Plane, Dog, Cat, etc.). This is key for polymorphism.
vehicles_and_animals = [
    Car("Tesla", "Model S"),
    Plane("Boeing", "747"),
    Dog("Fido", "Golden Retriever"),
    Cat("Whiskers", "Siamese"),
    Car("Ford", "Mustang"),
]

# --- Demonstrate Polymorphism ---

print("--- Calling the 'move()' method on each object ---")

# Loop through the list and call the 'move()' method on each object.
# The program automatically knows which version of `move()` to call
# based on the object's class at runtime.
for item in vehicles_and_animals:
    item.move()

print("\n--- Program finished ---")