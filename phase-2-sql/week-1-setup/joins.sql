SELECT p.name AS product, s.name AS supplier, s.country
FROM products p
INNER JOIN suppliers s ON p.supplier_id = s.id;


SELECT s.country, COUNT(*) AS product_count
FROM products p
INNER JOIN suppliers s ON p.supplier_id = s.id
GROUP BY s.country;


SELECT p.name AS product, s.name AS supplier, s.country
FROM products p
LEFT JOIN suppliers s ON p.supplier_id = s.id;