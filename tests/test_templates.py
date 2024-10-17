import pytest
from app import app  # Adjust the import if your app is named differently

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_food_entries_template(client):
    """Test that the food entries template renders correctly."""
    # Simulate the response from your interact_repository
    food_entries = [
        {
            'name': 'Apples',
            'quantity': 10,
            'expiration_period_weeks': 2,
            'expiration_period_months': 1
        },
        {
            'name': 'Bananas',
            'quantity': 5,
            'expiration_period_weeks': 1,
            'expiration_period_months': 0
        }
    ]

    # You can use a mock library to stimulate a resposne.
    # For this example, we will directly call the route
    response = client.get('/food')

    # Assert that the response is 200 OK
    assert response.status_code == 200
    # Assert that the response data contains the food entries
    assert b'Food Entries' in response.data
    assert b'Apples' in response.data
    assert b'10' in response.data
    assert b'2' in response.data
    assert b'1' in response.data
    assert b'Bananas' in response.data
    assert b'5' in response.data
    assert b'1' in response.data
    assert b'0' in response.data

def test_empty_food_entries_template(client):
    """Test that the template renders correctly when there are no food entries."""
    # Here you would mock the response when there are no food entries
    response = client.get('/food')

    # Assert that the response is 200 OK
    assert response.status_code == 200
    # Assert that the template indicates no food entries found
    assert b'No food entries found.' in response.data
