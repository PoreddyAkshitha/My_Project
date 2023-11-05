from Foodie.foodie import Foodie

class Noodles(Foodie):
    def __init__(self, item, famous_place, calories, quantity, quality):
        super().__init__(item, famous_place, calories, quantity)
        self.quality = quality

    def category(self):
         return f"It is a Fast-food"

    def price(self):
         return f"It costs around $50"
