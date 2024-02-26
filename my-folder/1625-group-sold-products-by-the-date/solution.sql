# Write your MySQL query statement below
select sell_date, 
count(DISTINCT(product)) as num_sold,
 GROUP_CONCAT(DISTINCT(product) 
 ORDER BY product SEPARATOR ',') as products
  from activities group by sell_date;
