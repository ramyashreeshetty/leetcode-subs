-- -- Write your PostgreSQL query statement below
-- with trans as (
-- select 
--     substring(trans_date::varchar, 1, 7) as month, 
--     country, 
--     count(*) as trans_count,
--     sum(amount) as trans_total_amount 
-- from Transactions
-- group by substring(trans_date::varchar, 1, 7), country
-- ),
-- approv as (
-- select 
--     substring(trans_date::varchar, 1, 7) as month, 
--     country, 
--     count(*) as approved_count,
--     sum(amount) as approved_total_amount 
-- from Transactions
-- where state = 'approved'
-- group by substring(trans_date::varchar, 1, 7), country
-- )
-- select
-- t.month,
-- t.country,
-- t.trans_count,
-- coalesce(a.approved_count, 0) as approved_count,
-- t.trans_total_amount,
-- coalesce(a.approved_total_amount, 0) as approved_total_amount
-- from trans t
-- left join approv a
-- on t.month = a.month and t.country = a.country;


select 
    substring(trans_date::varchar, 1, 7) as month, 
    country, 
    count(*) as trans_count,
    count(case when state='approved' then 1 end) as approved_count,
    sum(amount) as trans_total_amount,
    sum(case when state='approved' then amount else 0 end) as approved_total_amount 
from Transactions
group by substring(trans_date::varchar, 1, 7), country