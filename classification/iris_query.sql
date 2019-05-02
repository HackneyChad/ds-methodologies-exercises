-- iris query:

USE iris_db;

SELECT m.species_id
,s.species_name
,measurement_id
,petal_length
,petal_width
,sepal_length
,sepal_width
FROM measurements m
JOIN species s ON s.species_id = m.species_id
ORDER by m.species_id, m.measurement_id;


