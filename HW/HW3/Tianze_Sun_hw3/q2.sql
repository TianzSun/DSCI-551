use sakila;
DROP VIEW IF EXISTS Comedy_film;


CREATE VIEW Comedy_film AS
SELECT film_category.film_id
FROM film_category
WHERE film_category.category_id IN
(SELECT category.category_id
    FROM category
    WHERE category.name='Comedy'
    );

SELECT DISTINCT actor.actor_id, actor.first_name, actor.last_name
FROM actor
WHERE actor.actor_id IN
(SELECT film_actor.actor_id
FROM film_actor
    WHERE film_actor.film_id IN (SELECT Comedy_film.film_id FROM Comedy_film)
    )
ORDER BY actor.actor_id DESC;
