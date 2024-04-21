-- Objective: list the titles and release years of all Harry Potter movies, in chronological order

-- The percent sign % represents zero, one, or multiple characters. 
-- In this case, it represents the remainder of the Harry Potter movie titles
SELECT title, year FROM movies
WHERE title LIKE 'Harry Potter%'
ORDER by year;