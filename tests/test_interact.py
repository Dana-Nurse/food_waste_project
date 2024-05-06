from lib.interact import FoodEntry

"""
FoodEntry constructs with a name, quantity, expiration weeks, and expiration months
"""
def test_food_entry_constructs():
    food_entry = FoodEntry("Test Food", 5, 2, 1)
    assert food_entry.name == "Test Food"
    assert food_entry.quantity == 5
    assert food_entry.expiration_weeks == 2
    assert food_entry.expiration_months == 1

"""
We can format food entries to strings nicely
"""
def test_food_entries_format_nicely():
    food_entry = FoodEntry("Test Food", 5, 2, 1)
    assert str(food_entry) == "FoodEntry(Test Food, 5, 2, 1)"

"""
We can compare two identical food entries
And have them be equal
"""
def test_food_entries_are_equal():
    food_entry1 = FoodEntry("Test Food", 5, 2, 1)
    food_entry2 = FoodEntry("Test Food", 5, 2, 1)
    assert food_entry1 == food_entry2
