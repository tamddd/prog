select max(e.salary) as "SecondHighestSalary" from Employee as e
where e.salary < (
    select max(salary) from Employee
)
