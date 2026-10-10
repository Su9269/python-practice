--Write a solution to find the daily active user count for a period of 30 days ending 2019-07-27 inclusively. 
--A user was active on someday if they made at least one activity on that day.
--Return the result table in any order.
--The result format is in the following example.
--Note: Any activity from ('open_session', 'end_session', 'scroll_down', 'send_message') will be considered valid activity for a user to be considered active on a day.
select activity_date as day,
    count(distinct user_id) as active_users
from Activity
where activity_type in(
        'open_session',
        'end_session',
        'scroll_down',
        'send_message'
    )
    and activity_date between "2019-06-28" and "2019-07-27"
group by activity_date --Example 1:
    --Input: 
    --Activity table:
    --+---------+------------+---------------+---------------+
    --| user_id | session_id | activity_date | activity_type |
    --+---------+------------+---------------+---------------+
    --| 1       | 1          | 2019-07-20    | open_session  |
    --| 1       | 1          | 2019-07-20    | scroll_down   |
    --| 1       | 1          | 2019-07-20    | end_session   |
    --| 2       | 4          | 2019-07-20    | open_session  |
    --| 2       | 4          | 2019-07-21    | send_message  |
    --| 2       | 4          | 2019-07-21    | end_session   |
    --| 3       | 2          | 2019-07-21    | open_session  |
    --| 3       | 2          | 2019-07-21    | send_message  |
    --| 3       | 2          | 2019-07-21    | end_session   |
    --| 4       | 3          | 2019-06-25    | open_session  |
    --| 4       | 3          | 2019-06-25    | end_session   |
    --+---------+------------+---------------+---------------+
    --Output: 
    --+------------+--------------+ 
    --| day        | active_users |
    --+------------+--------------+ 
    --| 2019-07-20 | 2            |
    --| 2019-07-21 | 2            |
    --+------------+--------------+ 
    --Explanation: Note that we do not care about days with zero active users.