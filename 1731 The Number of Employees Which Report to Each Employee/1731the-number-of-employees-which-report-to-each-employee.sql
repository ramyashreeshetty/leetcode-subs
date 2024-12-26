-- Write your PostgreSQL query statement below

select distinct m.employee_id, m.name, count(m.*) as reports_count, round(avg(e.age)) as average_age
from employees e
join employees m
on e.reports_to = m.employee_id
group by 1,2
order by 1,2