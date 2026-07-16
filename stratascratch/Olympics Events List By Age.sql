---Find the lowest, average, and the highest ages of athletes across all Olympics. 
---HINT: If athlete participated in more than one discipline at one Olympic games, consider it as a separate athlete, no need to remove such edge cases.
select min(age) as lowest_age,
    avg(age) as mean_age,
    max(age) as higest_age
from olympics_athletes_events;