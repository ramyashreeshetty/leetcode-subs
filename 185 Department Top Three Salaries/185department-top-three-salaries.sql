-- Write your PostgreSQL query statement below

select Department, Employee, Salary
from(
    select 
        d.name as Department,
        e.name as Employee,
        e.salary as Salary,
        dense_rank() over(partition by departmentId order by salary desc) rn
    from employee e
    join department d
    on e.departmentId = d.id
)
where rn <= 3