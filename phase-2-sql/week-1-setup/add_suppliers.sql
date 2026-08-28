CREATE TABLE suppliers (
    id INT PRIMARY KEY,
    name TEXT NOT NULL,
    country TEXT
);

ALTER TABLE products
    ADD COLUMN supplier_id INT REFERENCES suppliers(id);