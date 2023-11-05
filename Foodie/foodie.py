from abc import ABC, abstractmethod

# Define the abstract parent class 'Vehicle'
class Foodie(ABC):
    def __init__(self, item, famous_place, calories, quantity):
        self.item = item
        self.famous_place = famous_place
        self.calories = calories
        self.quantity = quantity

    @property
    @abstractmethod
    def category(self):
        pass

    @abstractmethod
    def price(self):
        pass

       
