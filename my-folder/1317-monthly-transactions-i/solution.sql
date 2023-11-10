# Write your MySQL query statement below

#select SUM(amount), COUNT(*) from Transactions where state='approved' group by MONTH(trans_date);
SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month, country, count(*) as trans_count,
sum(state = 'approved') as approved_count, sum(amount) as trans_total_amount,
sum(case when state = 'approved' then amount else 0 end) as approved_total_amount
from Transactions
GROUP BY month, country;






