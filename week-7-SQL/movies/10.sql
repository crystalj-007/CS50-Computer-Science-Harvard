-- Objective: list the names of all people who have directed a movie that received a rating of at least 9.0

SELECT name FROM people
WHERE people.id IN 

-- Subquery selects person ids from directors table where movie ratings are >=9
(SELECT DISTINCT person_id FROM directors
JOIN ratings ON ratings.movie_id = directors.movie_id
WHERE rating >= 9.0);





