---Write a solution to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. 
---In other words, you need to determine the number of players who logged in on the day immediately following their initial login, and divide it by the number of total players.
---The result format is in the following example.
with first_login as (
    select player_id,
        min(event_date) as first_date,
        date_add(min(event_date), interval 1 day) as tomorrow
    from Activity
    group by player_id
)
select round(
        count(distinct a.player_id) / count(distinct f.player_id),
        2
    ) as fraction
from first_login as f
    left join Activity as a on f.player_id = a.player_id
    and f.tomorrow = a.event_date --Example 1:
    --Input: 
    --Activity table:
    --+-----------+-----------+------------+--------------+
    --| player_id | device_id | event_date | games_played |
    --+-----------+-----------+------------+--------------+
    --| 1         | 2         | 2016-03-01 | 5            |
    --| 1         | 2         | 2016-03-02 | 6            |
    --| 2         | 3         | 2017-06-25 | 1            |
    --| 3         | 1         | 2016-03-02 | 0            |
    --| 3         | 4         | 2018-07-03 | 5            |
    --+-----------+-----------+------------+--------------+
    --Output: 
    --+-----------+
    --| fraction  |
    --+-----------+
    --| 0.33      |
    --+-----------+
    --Explanation: 
    --Only the player with id 1 logged back in after the first day he had logged in so the answer is 1/3 = 0.33