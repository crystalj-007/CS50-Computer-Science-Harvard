-- Objective: determine the average rating of all movies released in 2012


-- Join both tables by matching movie id in movies to movie id in the ratings table
-- AVG determines average
SELECT AVG(rating) FROM movies
JOIN ratings ON movies.id= ratings.movie_id
WHERE year =2012;