from Foodie.panipuri import panipuri

# Test setup: create an instance of Biryani
panipuri = panipuri("Large Pani-Puri", "Mumbai", 340, "Serves 1", "Sweet-Sour taste")

# tests are written as functions that start with the word "test"
def test_panipuri_category():
    # The assert statement checks for the result of a boolean expression
    # True means the test passed
    assert panipuri.category() == "It is a best snack item"

def test_panipuri_price():
    assert panipuri.price() == "It costs around $35"

 

