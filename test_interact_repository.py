from lib.interact_repository import FoodEntryRepository
from lib.interact import FoodEntry

"""
When FoodEntryRepository add_new_food is called,
a new record is added to the database.
"""
def test_add_new_food(db_connection):
    db_connection.seed("seeds/food_tracker.sql")
    repository = FoodEntryRepository(db_connection)

    repository.add_new_food(FoodEntry(None, "milk", 2, 4, 1))

    result = repository.view_existing_food()
    assert result == [
        FoodEntry(1, "dhal", 1, 1, 0),
        FoodEntry(2, "sandwiches", 5, 1, 0),
        FoodEntry(3, "onions", 10, 8, 2),
        FoodEntry(4, "yogurt", 6, 12, 3),
        FoodEntry(5, "milk", 2, 4, 1)
    ]

"""
When FoodEntryRepository view_existing_food is called,
a list of FoodEntry objects reflecting the seed data is returned.
"""
def test_view_existing_food(db_connection):
    db_connection.seed("seeds/food_tracker.sql")
    repository = FoodEntryRepository(db_connection)

    food_entries = repository.view_existing_food()

    assert food_entries == [
        FoodEntry(1, "dhal", 1, 1, 0),
        FoodEntry(2, "sandwiches", 5, 1, 0),
        FoodEntry(3, "onions", 10, 8, 2),
        FoodEntry(4, "yogurt", 6, 12, 3)
    ]

"""
When FoodEntryRepository update_food_quantities is called,
the quantity of a food entry in the database is updated.
"""
def test_update_food_quantities(db_connection):
    db_connection.seed("seeds/food_tracker.sql")
    repository = FoodEntryRepository(db_connection)

    repository.update_food_quantities("dhal", 3)

    result = repository.view_existing_food()
    assert result[0].quantity == 3

"""
When FoodEntryRepository update_expiration_dates is called,
the expiration weeks and months of a food entry in the database are updated.
"""
def test_update_expiration_dates(db_connection):
    db_connection.seed("seeds/food_tracker.sql")
    repository = FoodEntryRepository(db_connection)

    repository.update_expiration_dates("dhal", 2, 2)

    result = repository.view_existing_food()
    assert result[0].expiration_weeks == 2
    assert result[0].expiration_months == 2

"""
When FoodEntryRepository delete_food_entry is called,
a food entry is removed from the database.
"""
def test_delete_food_entry(db_connection):
    db_connection.seed("seeds/food_tracker.sql")
    repository = FoodEntryRepository(db_connection)

    repository.delete_food_entry("dhal")

    result = repository.view_existing_food()
    assert len(result) == 3
    assert "dhal" not in [food.name for food in result]

"""
When FoodEntryRepository generate_reports is called,
a report of food items expiring soon is returned.
"""
def test_generate_reports(db_connection):
    db_connection.seed("seeds/food_tracker.sql")
    repository = FoodEntryRepository(db_connection)

    report = repository.generate_reports(7, 1)

    assert "Food Items Expiring Soon:" in report
