--

SELECT cities.id, cities.name, states.name from cities
JOIN states ON cities.state_id = state.id
ORDER BY cities.id ASC;