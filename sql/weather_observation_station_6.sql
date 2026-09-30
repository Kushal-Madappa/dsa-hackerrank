-- HackerRank: Weather Observation Station 6
-- https://www.hackerrank.com/challenges/weather-observation-station-6/problem
SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '^[aeiouAEIOU]';
