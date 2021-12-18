#!/usr/bin/env python3

class Animal:

    def get_food_preference(self):
        return self.food_preference

    def get_sleep_time(self):
        return self.sleep_time

    def get_noise(self):
        return self.noise

class Cat(Animal):
    
    # Overridden Attributes
    def __init__(self):
        self.food_preference = "Meat Pebbles"
        self.sleep_time = 16
        self.noise = "Meow"

class Seal(Animal):

    # Overridden Attributes
    def __init__(self):
        self.food_preference = "Penguins"
        self.sleep_time = 4
        self.noise = "Hwarghs"

class Lizard(Animal):

    # Overridden Attributes
    def __init__(self):
        self.food_preference = "Insects"
        self.sleep_time = 6
        self.noise = "Creck"


bixby = Cat()
jaguar = Seal()
leeroy = Lizard()

print(bixby.get_noise())
print(jaguar.get_food_preference())
print(leeroy.get_sleep_time())
