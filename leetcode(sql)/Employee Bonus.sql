--Write a solution to report the name and bonus amount of each employee who satisfies either of the following:
--The employee has a bonus less than 1000.
--The employee did not get any bonus.
--Return the result table in any order.
--The result format is in the following example.
select e.name,
    b.bonus
from Employee as e
    left join Bonus as b on e.empId = b.EmpId
where b.bonus is null
    or b.bonus < 1000 --Input: 
    --Employee table:
    --+-------+--------+------------+--------+
    --| empId | name   | supervisor | salary |
    --+-------+--------+------------+--------+
    --| 3     | Brad   | null       | 4000   |
    --| 1     | John   | 3          | 1000   |
    --| 2     | Dan    | 3          | 2000   |
    --| 4     | Thomas | 3          | 4000   |
    --+-------+--------+------------+--------+
    --Bonus table:
    --+-------+-------+
    --| empId | bonus |
    --+-------+-------+
    --| 2     | 500   |
    --| 4     | 2000  |
    --+-------+-------+
    --Output: 
    --+------+-------+
    --| name | bonus |
    --+------+-------+
    --| Brad | null  |
    --| John | null  |
    --| Dan  | 500   |
    --+------+-------+