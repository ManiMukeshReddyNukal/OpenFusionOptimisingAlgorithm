# Write your MySQL query statement below

select "Low Salary" as category , SUM(IF(income<20000,1,0)) as accounts_count from Accounts UNION 
select "Average Salary" as category , SUM(IF(20000<=income &&income <=50000,1,0)) as accounts_count from Accounts UNION
select "High Salary" as category , SUM(IF(50000<income,1,0)) as accounts_count from Accounts ;


