
WITH min_year_table AS (
SELECT product_id, min(year) min_year
FROM sales
GROUP BY product_id)

SELECT s.product_id, s.year first_year, quantity, price
FROM sales s
JOIN min_year_table m ON s.product_id = m.product_id and s.year = m.min_year
