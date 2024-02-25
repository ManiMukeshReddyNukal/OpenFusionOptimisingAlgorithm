# Write your MySQL query statement below
(select "Low Salary" as category,COUNT(*) as accounts_count
from accounts 
where income<20000)
UNION
(select "Average Salary" as category,COUNT(*) as accounts_count
from accounts 
where income>=20000 and income <=50000)
UNION
(select "High Salary" as category,COUNT(*) as accounts_count
from accounts 
where income>50000)
;
