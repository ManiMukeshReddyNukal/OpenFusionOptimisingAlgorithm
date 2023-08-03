# Write your MySQL query statement below

#select SUM(amount), COUNT(*) from Transactions where state='approved' group by MONTH(trans_date);

select DATE_FORMAT(trans_date, '%Y-%m') AS month, country,COUNT(*) as trans_count, SUM(IF(state='approved',1,0)) as approved_count, SUM(amount) as trans_total_amount, SUM(IF(state='approved',amount,0)) as approved_total_amount from Transactions group by DATE_FORMAT(trans_date, '%Y-%m'),country;



