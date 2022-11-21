use sakila;


SELECT actor.first_name, actor.last_name
FROM actor
WHERE actor.actor_id IN
      (SELECT actor_id
       FROM (SELECT film_actor.actor_id
             FROM film_actor
             GROUP BY film_actor.actor_id
             ORDER BY count(*) DESC LIMIT 30
            )
       AS actor_id
      )
ORDER BY actor.first_name, actor.last_name;