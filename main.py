from Foodie.Biryani import Biryani
from Foodie.Noodles import Noodles
from Foodie.panipuri import panipuri

biryani = Biryani("Chicken Biryani", "Hyderabad", 560, "Serves 2", "Golden-Orange")
noodles = Noodles("Egg Noodles", "Delhi", 720, "Serves 3", "Texture is crucial")
panipuri = panipuri("Large Pani-Puri", "Mumbai", 340, "Serves 1", "Sweet-Sour taste")


print(biryani.category())
print(biryani.price())
print(noodles.category())
print(noodles.price())
print(panipuri.category())
print(panipuri.price())
