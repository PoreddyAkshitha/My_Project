from Foodie.foodie import Foodie

def test_foodie_is_abstract():
    try:
        Foodie("VadaPav", "famous_place", 202, "Serves 1 ")
    except TypeError as e:
        assert "Can't instantiate abstract class Foodie" in str(e)