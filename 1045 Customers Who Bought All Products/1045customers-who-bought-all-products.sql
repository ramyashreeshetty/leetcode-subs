-- Write your PostgreSQL query statement below
select distinct c.customer_id
from customer c
join product p
on c.product_key = p.product_key
group by 1
having count(distinct p.product_key) = (select count(product_key) from product)
