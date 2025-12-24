class Dog:
    animal = "canine"

    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour
    
    def __str__(self):
        return (f"  Animal Type: {self.animal}\n"
                f"  Breed: {self.breed}\n"
                f"  Colour: {self.colour}")

dog1 = Dog("Labrador", "Golden")
dog2 = Dog("German Shepherd", "Black and Tan")
