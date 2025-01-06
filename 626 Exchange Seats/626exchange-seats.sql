-- Write your PostgreSQL query statement below
SELECT id, 
       CASE WHEN id % 2 = 0
       then LAG(student, 1, student) OVER (ORDER BY id) 
       else LEAD(student, 1, student) OVER (ORDER BY id) 
       end as student
FROM seat;