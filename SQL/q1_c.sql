use sakila;


SELECT  film_actor.actor_id, actor.first_name, actor.last_name, film.film_id, film.title
FROM film_actor
LEFT JOIN actor
ON film_actor.actor_id=actor.actor_id
RIGHT JOIN film
ON film_actor.film_id=film.film_id
WHERE film_actor.actor_id= 1;