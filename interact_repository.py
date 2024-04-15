class FoodEntryRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_new_food(self, food_entry):
        self._connection.execute('INSERT INTO food_entries (name, quantity, expiration_period_weeks, expiration_period_months) VALUES (%s, %s, %s, %s)',
            [food_entry.name, food_entry.quantity, food_entry.expiration_period_weeks, food_entry.expiration_period_months])
        return None

    def view_existing_food(self):
        rows = self._connection.execute('SELECT * FROM food_entries')
        food_entries = []
        for row in rows:
            entry = FoodEntry(row["name"], row["quantity"], row["expiration_period_weeks"], row["expiration_period_months"])
            food_entries.append(entry)
        return food_entries

    def update_food_quantities(self, name, new_quantity):
        self._connection.execute('UPDATE food_entries SET quantity = %s WHERE name = %s',
            [new_quantity, name])
        return None

    def update_expiration_dates(self, name, new_expiration_period_weeks, new_expiration_period_months):
        self._connection.execute('UPDATE food_entries SET expiration_period_weeks = %s, expiration_period_months = %s WHERE name = %s',
            [new_expiration_period_weeks, new_expiration_period_months, name])
        return None
    
    def delete_food_entry(self, name):
        confirm_delete = input(f"Are you sure you want to delete the food entry '{name}'? (yes/no): ")
        if confirm_delete.lower() == "yes":
            self._connection.execute('DELETE FROM food_entries WHERE name = %s', [name])
            print(f"Food entry '{name}' has been successfully deleted.")
        elif confirm_delete.lower() == "no":
            print(f"No deletion of food entry '{name}'.")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
        return None

    def generate_reports(self, soon_to_expire_weeks, soon_to_expire_months):
        # Retrieve data from the database
        rows = self._connection.execute('SELECT * FROM food_entries')

        # Calculate total quantity
        total_quantity = sum(row["quantity"] for row in rows)

        # Filter items that are expiring soon
        expiring_soon = [entry for entry in rows if entry["expiration_period_weeks"] <= soon_to_expire_weeks or entry["expiration_period_months"] <= soon_to_expire_months]

        # Format reports
        report = f"Total Quantity of Food Items: {total_quantity}\n"
        report += "Food Items Expiring Soon:\n"
        for entry in expiring_soon:
            report += f"Name: {entry['name']}, Expiration Period (weeks): {entry['expiration_period_weeks']}, Expiration Period (months): {entry['expiration_period_months']}\n"

        return report
