from Foodie.Biryani import Biryani

# Test setup: create an instance of Biryani
biryani = Biryani("Chicken Biryani", "Hyderabad", 560, "Serves 2", "Golden-Orange")

# tests are written as functions that start with the word "test"
def test_biryani_category():
    # The assert statement checks for the result of a boolean expression
    # True means the test passed
    assert biryani.category() == "It is a Seasoned rice-dish"

def test_biryani_price():
    assert biryani.price() == "It costs around $30"

