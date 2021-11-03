use sakila;


SELECT name
FROM language
WHERE language_id NOT IN
      (SELECT DISTINCT language_id
       FROM film
       WHERE language_id IS NOT NULL
      )
AND language_id NOT IN
     (SELECT DISTINCT original_language_id
      FROM film
      WHERE original_language_id IS NOT NULL
     )
ORDER BY name;
