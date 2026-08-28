SELECT s.country, ROUND(AVG(price), 2) AS average_price
FROM products p
INNER JOIN suppliers s ON p.supplier_id = s.id
WHERE category = 'fruit'
GROUP BY s.country
ORDER BY average_price DESC;