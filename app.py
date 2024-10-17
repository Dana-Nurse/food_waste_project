import os
from flask import Flask, request, render_template
from lib.database_connection import DatabaseConnection  # Import the DatabaseConnection class
from lib.interact_repository import FoodEntryRepository  # Import your repository for food entries

app = Flask(__name__)

# Function to get a database connection
def get_db_connection():
    db_connection = DatabaseConnection()  # Create an instance of DatabaseConnection
    db_connection.connect()  # Connect to the database
    return db_connection

# Initialise the repository
food_repository = FoodEntryRepository(get_db_connection())  # Initialize the food entry repository

# Route to add a new food entry
@app.route('/food', methods=['POST'])
def add_food():
    data = request.form
    name = data['name']
    quantity = data['quantity']
    expiration_weeks = data['expiration_weeks']
    expiration_months = data['expiration_months']
    
    new_entry = FoodEntry(name, quantity, expiration_weeks, expiration_months)
    food_repository.add_new_food(new_entry)
    return 'Food entry added successfully', 201

# Route to get all food entries
@app.route('/food', methods=['GET'])
def get_food():
    food_entries = food_repository.view_existing_food()
    return render_template('food.html', food_entries=food_entries)

# Route to update food quantities
@app.route('/food/<name>/quantity', methods=['PUT'])
def update_food_quantity(name):
    data = request.form
    new_quantity = data['quantity']
    food_repository.update_food_quantities(name, new_quantity)
    return 'Food quantity updated successfully', 200

# Route to update expiration dates
@app.route('/food/<name>/expiration', methods=['PUT'])
def update_expiration_dates(name):
    data = request.form
    new_expiration_weeks = data['expiration_weeks']
    new_expiration_months = data['expiration_months']
    food_repository.update_expiration_dates(name, new_expiration_weeks, new_expiration_months)
    return 'Expiration dates updated successfully', 200

# Route to delete a food entry
@app.route('/food/<name>', methods=['DELETE'])
def delete_food_entry(name):
    food_repository.delete_food_entry(name)
    return 'Food entry deleted successfully', 204

# Route to generate reports
@app.route('/reports', methods=['GET'])
def generate_reports():
    soon_to_expire_weeks = request.args.get('soon_to_expire_weeks', type=int)
    soon_to_expire_months = request.args.get('soon_to_expire_months', type=int)
    report = food_repository.generate_reports(soon_to_expire_weeks, soon_to_expire_months)
    return render_template('reports.html', report=report)

if __name__ == '__main__':
    app.run(debug=True)
