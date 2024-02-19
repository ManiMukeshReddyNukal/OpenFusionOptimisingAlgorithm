# Write your MySQL query statement below
select V.customer_id, COUNT(*) as count_no_trans
from Visits V LEFT JOIN
Transactions T ON
V.visit_id = T.visit_id 
WHERE T.transaction_id is Null
group by V.customer_id
