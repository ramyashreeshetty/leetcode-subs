-- Write your PostgreSQL query statement below
select p.product_name, sum(unit) as unit
from orders o
join products p on o.product_id = p.product_id
where order_date::varchar like '2020-02%'
group by o.product_id, p.product_name
having sum(unit) >= 100;