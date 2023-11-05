from Foodie.foodie import Foodie

class Biryani(Foodie):
    def __init__(self, item, famous_place, calories, quantity, color):
        super().__init__(item, famous_place, calories, quantity)
        self.color = color

    def category(self):
         return f"It is a Seasoned rice-dish"

    def price(self):
         return f"It costs around $30"