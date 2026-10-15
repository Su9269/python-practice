--We define query quality as:
--The average of the ratio between query rating and its position.
--We also define poor query percentage as:
--The percentage of all queries with rating less than 3.
--Write a solution to find each query_name, the quality and poor_query_percentage.
--Both quality and poor_query_percentage should be rounded to 2 decimal places.
--Return the result table in any order.
--The result format is in the following example.
--sol 1
select query_name,
    round(sum(rating / position) / count(query_name), 2) as quality,
    round(
        (
            sum(
                case
                    when rating < 3 then 1
                    else 0
                end
            ) / count(query_name)
        ) * 100,
        2
    ) as poor_query_percentage
from Queries
group by query_name --sol 2
select query_name,
    round(avg(rating / position), 2) as quality,
    round(avg(rating < 3) * 100, 2) as poor_query_percentage
from Queries
group by query_name --Example 1:
    --Input: 
    --Queries table:
    --+------------+-------------------+----------+--------+
    --| query_name | result            | position | rating |
    --+------------+-------------------+----------+--------+
    --| Dog        | Golden Retriever  | 1        | 5      |
    --| Dog        | German Shepherd   | 2        | 5      |
    --| Dog        | Mule              | 200      | 1      |
    --| Cat        | Shirazi           | 5        | 2      |
    --| Cat        | Siamese           | 3        | 3      |
    --| Cat        | Sphynx            | 7        | 4      |
    --+------------+-------------------+----------+--------+
    --Output: 
    --+------------+---------+-----------------------+
    --| query_name | quality | poor_query_percentage |
    --+------------+---------+-----------------------+
    --| Dog        | 2.50    | 33.33                 |
    --| Cat        | 0.66    | 33.33                 |
    --+------------+---------+-----------------------+
    --Explanation: 
    --Dog queries quality is ((5 / 1) + (5 / 2) + (1 / 200)) / 3 = 2.50
    --Dog queries poor_ query_percentage is (1 / 3) * 100 = 33.33
    --Cat queries quality equals ((2 / 5) + (3 / 3) + (4 / 7)) / 3 = 0.66
    --Cat queries poor_ query_percentage is (1 / 3) * 100 = 33.33