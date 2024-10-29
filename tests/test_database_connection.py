# This is an example of how to use the DatabaseConnection class for the food waste tracker project

import os
from lib.database_connection import DatabaseConnection

def test_database_connection():
    # Use DATABASE_URL from environment or local fallback to ensure tests can run locally if not
    db_url = os.getenv("DATABASE_URL", "postgresql://localhost/food_tracker")
    db_connection = DatabaseConnection()
    db_connection.connect()  # Now uses DATABASE_URL by default
    
    # Seed the food_entries table with some test data
    db_connection.seed("seeds/food_tracker.sql")

    # Insert a new record
    db_connection.execute("INSERT INTO food_entries (name, quantity, expiration_period_weeks, expiration_period_months) VALUES (%s, %s, %s, %s)",
                        ["fifth_food", 5, 4, 1])

    # Retrieve all records
    result = db_connection.execute("SELECT * FROM food_entries")

    # Assert that the results are what we expect
    assert result == [
        {"id": 1, "name": "dhal", "quantity": 1, "expiration_period_weeks": 1, "expiration_period_months": 0},
        {"id": 2, "name": "sandwiches", "quantity": 5, "expiration_period_weeks": 1, "expiration_period_months": 0},
        {"id": 3, "name": "onions", "quantity": 10, "expiration_period_weeks": 8, "expiration_period_months": 2},
        {"id": 4, "name": "yogurt", "quantity": 6, "expiration_period_weeks": 12, "expiration_period_months": 3},
        {"id": 5, "name": "fifth_food", "quantity": 5, "expiration_period_weeks": 4, "expiration_period_months": 1}
    ]
