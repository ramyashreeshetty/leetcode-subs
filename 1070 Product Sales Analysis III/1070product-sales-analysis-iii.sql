-- Write your PostgreSQL query statement below

select product_id, year as first_year, quantity, price
from (
select s.product_id, year, quantity, price, rank() over(partition by s.product_id order by year) as rn
from sales s
join product p
on s.product_id = p.product_id
)
where rn = 1


-- select s.product_id, year, quantity, price, rank() over(partition by s.product_id order by year) as rn
-- from sales s
-- join product p
-- on s.product_id = p.product_id
