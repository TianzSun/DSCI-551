use sakila;


SELECT DISTINCT film_actor.actor_id
FROM film_actor
LEFT JOIN film
ON film_actor.film_id=film.film_id
WHERE film.length<48
ORDER BY film_actor.actor_id;
