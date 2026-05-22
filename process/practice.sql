SELECT *
FROM employee
WHERE performance > (
        SELECT AVG(performance)
        FROM employee
    )
ORDER BY salary DESC