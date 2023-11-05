from Foodie.Noodles import Noodles

# Test setup: create an instance of Biryani
noodles = Noodles("Egg Noodles", "Delhi", 720, "Serves 3", "Texture is crucial")

# tests are written as functions that start with the word "test"
def test_noodles_category():
    # The assert statement checks for the result of a boolean expression
    # True means the test passed
    assert noodles.category() == "It is a Fast-food"

def test_noodles_price():
    assert noodles.price() == "It costs around $50"

 
