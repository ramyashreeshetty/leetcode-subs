-- Write your PostgreSQL query statement below
with cte as(
select *
from (
    select
        product_id,
        new_price,
        change_date,
        row_number() over(partition by product_id order by change_date desc) rn
    from products
    where change_date <= '2019-08-16'
)
where rn=1
)
select
    distinct p.product_id,
    case when c.new_price is null then 10
    else c.new_price end as price
from products p
left join cte c
on p.product_id = c.product_id