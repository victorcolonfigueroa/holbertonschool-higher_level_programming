-- this script lists all the cities contained in the database hbtn_0b_usa
SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states ON states.id = cities.state_id
ORDER BY cities.id;