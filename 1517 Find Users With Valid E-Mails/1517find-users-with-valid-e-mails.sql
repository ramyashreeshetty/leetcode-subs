-- Write your PostgreSQL query statement below
select *
from users
where mail ~ '^[a-zA-Z][a-zA-Z0-9._-]*@leetcode[.]com$'