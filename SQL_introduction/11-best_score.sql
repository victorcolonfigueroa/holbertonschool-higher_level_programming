-- creates the lists of all records with a score of >= 10 ib the second_table
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER by score DESC