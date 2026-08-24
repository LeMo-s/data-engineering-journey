   CREATE TABLE products (
       id INT PRIMARY KEY,
       name TEXT NOT NULL,
       category TEXT,
       price NUMERIC(10,2)
   );

   INSERT INTO products (id, name, category, price) VALUES
       (1, 'apple', 'fruit', 0.50),
       (2, 'pear', 'fruit', 0.75),
       (3, 'carrot', 'vegetable', 0.30);

   SELECT * FROM products;