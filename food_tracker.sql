-- Table created for food entries
CREATE TABLE food_entries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    quantity INTEGER NOT NULL,
    expiration_weeks INTEGER NOT NULL,
    expiration_months INTEGER NOT NULL
);

-- Example records for tests to run 
INSERT INTO food_entries (name, quantity, expiration_weeks, expiration_months) VALUES ('dhal', 1, 1, 0);
INSERT INTO food_entries (name, quantity, expiration_weeks, expiration_months) VALUES ('sandwiches', 5, 1, 0);
INSERT INTO food_entries (name, quantity, expiration_weeks, expiration_months) VALUES ('onions', 10, 8, 0);
INSERT INTO food_entries (name, quantity, expiration_weeks, expiration_months) VALUES ('yogurt', 6, 12, 3);
