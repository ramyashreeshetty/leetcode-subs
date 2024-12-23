-- Write your PostgreSQL query statement below
with first_order as (
select 
customer_id,
order_date,
row_number() over (partition by customer_id order by order_date) rn,
customer_pref_delivery_date
from delivery
)
select 
round((((count(case when order_date = customer_pref_delivery_date then 1 end)*1.0)/count(*)) * 100), 2) as immediate_percentage 
from first_order
where rn = 1
-- and order_date = customer_pref_delivery_date