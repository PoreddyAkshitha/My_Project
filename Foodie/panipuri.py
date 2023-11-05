from Foodie.foodie import Foodie

class panipuri(Foodie):
    def __init__(self, item, famous_place, calories, quantity, taste):
        super().__init__(item, famous_place, calories, quantity)
        self.taste = taste

    def category(self):
         return f"It is a best snack item"

    def price(self):
         return f"It costs around $35"

