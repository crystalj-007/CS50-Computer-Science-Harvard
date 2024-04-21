-- Objective: list the titles of all movies in which both Bradley Cooper and Jennifer Lawrence starred

-- Method 1
SELECT title FROM movies
JOIN stars ON stars.movie_id=movies.id 
JOIN people ON people.id=stars.person_id
WHERE people.name='Jennifer Lawrence' 
AND title IN

(SELECT title FROM movies
JOIN stars ON stars.movie_id=movies.id 
JOIN people ON people.id=stars.person_id
WHERE people.name='Bradley Cooper' );

-- Method 2
JOIN stars ON stars.movie_id=movies.id 
JOIN people ON people.id=stars.person_id
WHERE people.name='Jennifer Lawrence' 

INTERSECT

SELECT title FROM movies
JOIN stars ON stars.movie_id=movies.id 
JOIN people ON people.id=stars.person_id
WHERE people.name='Bradley Cooper' ;


