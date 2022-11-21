use sakila;


SELECT film.title, film.release_year
FROM film
WHERE film.film_id = ANY
      (SELECT film_actor.film_id
       FROM film_actor
       WHERE film_actor.actor_id = 1
      )
ORDER BY film.title;