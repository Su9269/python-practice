---Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).
---Return the result table in any order.
---The result format is in the following example.
with copy as(
    select id,
        recordDate,
        temperature,
        date_sub(recordDate, interval 1 day) as yesterday
    from Weather
)
select c.id as Id
from copy as c
    left join weather as w on c.yesterday = w.recordDate
where c.temperature > w.temperature ---Input: 
    ---Weather table:
    ---+----+------------+-------------+
    ---| id | recordDate | temperature |
    ---+----+------------+-------------+
    ---| 1  | 2015-01-01 | 10          |
    ---| 2  | 2015-01-02 | 25          |
    ---| 3  | 2015-01-03 | 20          |
    ---| 4  | 2015-01-04 | 30          |
    ---+----+------------+-------------+
    ---Output: 
    ---+----+
    ---| id |
    ---+----+
    ---| 2  |
    ---| 4  |
    ---+----+
    ---Explanation: 
    ---In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
    ---In 2015-01-04, the temperature was higher than the previous day (20 -> 30).