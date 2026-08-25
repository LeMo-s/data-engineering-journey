SELECT * FROM products WHERE category = 'vegetable' ORDER BY price DESC;

SELECT category, COUNT(*) AS product_count FROM products GROUP BY category;

SELECT category, ROUND(AVG(price), 2) AS average_price FROM products GROUP BY category ORDER BY average_price DESC;