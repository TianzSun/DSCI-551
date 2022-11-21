use sakila;


SELECT COUNT(DISTINCT category_id) AS number_of_categories FROM
(SELECT film_category.film_id, film_category.category_id
 FROM film_category
 WHERE film_category.film_id IN
     (SELECT film_actor.film_id
      FROM film_actor
      WHERE film_actor.actor_id IN
            (SELECT actor.actor_id
             FROM actor
             WHERE actor.first_name='Ed'
             AND actor.last_name='Chase'
            )
     )
) AS t;