-- Table created for food entries
CREATE TABLE food_entries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    quantity INTEGER NOT NULL,
    expiration_days INTEGER NOT NULL,
    category_id INTEGER NOT NULL
);

-- Example records for tests to run 
INSERT INTO food_entries (name, quantity, expiration_days, category_id) VALUES ('dhal', 1, 1, 0);
INSERT INTO food_entries (name, quantity, expiration_days, category_id) VALUES ('sandwiches', 5, 1, 0);
INSERT INTO food_entries (name, quantity, expiration_days, category_id) VALUES ('onions', 10, 8, 2);
INSERT INTO food_entries (name, quantity, expiration_days, category_id) VALUES ('yogurt', 6, 12, 3);
