from playwright.sync_api import Page, expect

# Test the '/food' route to add a new food entry
def test_add_food(page, test_web_address, db_connection):
    # Seed the database with necessary data if required
    db_connection.seed("seeds/food_tracker.sql")

    # Navigate to the '/food' route
    page.goto(f"http://{test_web_address}/food", wait_until="domcontentloaded")

    # Fill in form data and submit it
    page.fill('input[name="name"]', "mango")
    page.fill('input[name="quantity"]', "10")
    page.fill('input[name="expiration_weeks"]', "2")
    page.fill('input[name="expiration_months"]', "0")
    page.click('button[type="submit"]')

    # Assert that the response contains the success message
    expect(page).to_have_text("Food entry added successfully")

# Test the '/food' route to get all food entries
def test_get_food(page, test_web_address, db_connection):
    # Seed the database with the required data
    db_connection.seed("seeds/food_tracker.sql")

    # Navigate to the '/food' route
    page.goto(f"http://{test_web_address}/food", wait_until="domcontentloaded")

    # Assert that the response contains the expected food entries
    expect(page).to_have_text("Food Entries")
    expect(page).to_have_text("dhal")
    expect(page).to_have_text("mango")
    # Add more assertions as needed for other food entries

# Test the '/food/<name>/quantity' route to update food quantities
def test_update_food_quantity(page, test_web_address, db_connection):
    # Seed the database with necessary data if required
    db_connection.seed("seeds/food_tracker.sql")

    # Navigate to the '/food' route to get food entries
    page.goto(f"http://{test_web_address}/food", wait_until="domcontentloaded")

    # Click on the link to update quantity for a specific food item (e.g., dhal)
    page.click(f'text="Update Quantity"')

    # Fill in the form data to update quantity
    page.fill('input[name="quantity"]', "15")
    page.click('button[type="submit"]')

    # Assert that the response contains the success message
    expect(page).to_have_text("Food quantity updated successfully")

# Test the '/food/<name>/expiration' route to update expiration dates
def test_update_expiration_dates(page, test_web_address, db_connection):
    # Seed the database with necessary data if required
    db_connection.seed("seeds/food_tracker.sql")

    # Navigate to the '/food' route to get food entries
    page.goto(f"http://{test_web_address}/food", wait_until="domcontentloaded")

    # Click on the link to update expiration dates for a specific food item (e.g., mango)
    page.click(f'text="Update Expiration"')

    # Fill in the form data to update expiration dates
    page.fill('input[name="expiration_weeks"]', "3")
    page.fill('input[name="expiration_months"]', "0")
    page.click('button[type="submit"]')

    # Assert that the response contains the success message
    expect(page).to_have_text("Expiration dates updated successfully")

# Test the '/food/<name>' route to delete a food entry
def test_delete_food_entry(page, test_web_address, db_connection):
    # Seed the database with necessary data if required
    db_connection.seed("seeds/food_tracker.sql")

    # Navigate to the '/food' route to get food entries
    page.goto(f"http://{test_web_address}/food", wait_until="domcontentloaded")

    # Click on the link to delete a specific food item (e.g., onions)
    page.click(f'text="Delete"')

    # Assert that the response contains the success message
    expect(page).to_have_text("Food entry deleted successfully")

# Test the '/reports' route to generate reports
def test_generate_reports(page, test_web_address, db_connection):
    # Seed the database with necessary data if required
    db_connection.seed("seeds/food_tracker.sql")

    # Navigate to the '/reports' route
    page.goto(f"http://{test_web_address}/reports", wait_until="domcontentloaded")

    # Assert that the response contains the expected content
    expect(page).to_have_text("Report Title")
    expect(page).to_have_text("Total Quantity")
    expect(page).to_have_text("Expiring Soon")
    

