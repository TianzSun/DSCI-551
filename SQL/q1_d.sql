use sakila;


SELECT  address.address_id, address.address, address.city_id
FROM address
LEFT JOIN city
ON address.city_id=city.city_id
WHERE country_id=6;