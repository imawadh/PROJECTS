CREATE DATABASE olympics_db;

USE olympics_db;

-- Question --> 1
SELECT * FROM olymypics;

-- Question --> 2
select name,medal
from olymypics;

-- Question --> 3
SELECT COUNT(name) AS total_number_of_athletes FROM olympics;

-- Question --> 4
SELECT * FROM olympics WHERE medal='Gold';

-- Question --> 5
SELECT name,year FROM olympics WHERE medal='silver';

-- Question --> 6
SELECT 
    team,
    SUM(CASE WHEN medal = 'Gold' THEN 1 ELSE 0 END) AS Gold,
    SUM(CASE WHEN medal = 'Silver' THEN 1 ELSE 0 END) AS Silver,
    SUM(CASE WHEN medal = 'Bronze' THEN 1 ELSE 0 END) AS Bronze
FROM 
    olympics
WHERE 
    medal IN ('Gold', 'Silver', 'Bronze')
GROUP BY 
    team;

-- Question --> 7
SELECT team 
FROM olympics 
WHERE medal LIKE 'Gold'
GROUP BY team
HAVING count(medal='Gold')>50;

-- Question --> 8
SELECT name FROM olympics GROUP BY name  ORDER BY COUNT(medal) DESC LIMIT 1;

-- Question --> 9
SELECT event FROM olympics WHERE event LIKE '%Freestyle%';

-- Question --> 10
SELECT name,count(medal) AS total_numbers_of_medals FROM olympics GROUP BY name  ORDER BY COUNT(medal) DESC LIMIT 3;

-- Question --> 11
SELECT distinct name, COUNT(*) AS total_medals
FROM olympics
GROUP BY name
HAVING COUNT(*) > 1;

-- Question --> 12
SELECT DISTINCT team 
FROM olympics
WHERE medal='Gold' AND (season='Summer' OR season='Winter');

-- Question --> 13
SELECT team, MAX(year) - MIN(year) AS year_difference
FROM olympics
GROUP BY team;

-- Question --> 14
SELECT team, COUNT(medal) / COUNT(DISTINCT name) AS avg_medals_per_athlete
FROM olympics
GROUP BY team;

-- Question --> 15
SELECT team
FROM (
    SELECT team, sport, medal
    FROM olympics
    GROUP BY team, sport, medal
) AS medal_counts
GROUP BY team
HAVING COUNT(DISTINCT sport) > 10;