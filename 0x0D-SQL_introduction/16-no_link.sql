-- List all records of a table of a database in MySQL server.

SELECT score, name
  FROM second_table
  WHERE name IS NOT Null
  ORDER BY score DESC;
