-- Write your PostgreSQL query statement below
select 
    sell_date, 
    count(distinct product) as num_sold, 
    STRING_AGG(DISTINCT product, ',' ORDER BY product) as products
from Activities 
group by 1
order by 1