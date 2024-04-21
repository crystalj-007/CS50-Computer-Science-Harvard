-- Objective: determine the number of movies with an IMDb rating of 10.0

-- "COUNT" counts the total number of rows in that column 
SELECT COUNT(movie_id) FROM ratings
WHERE rating = 10;