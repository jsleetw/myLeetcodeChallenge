# Write your MySQL query statement below 
Select IFNULL(
( Select distinct Salary from Employee order by Salary desc limit 1 offset 1 ), NULL) as SecondHighestSalary
    
