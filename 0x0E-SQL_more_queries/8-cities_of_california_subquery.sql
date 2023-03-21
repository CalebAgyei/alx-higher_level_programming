-- List records that can be found in a database 

--
-- List cities of California in 'hbtn_0d_usa'
--
SELECT id, name
  FROM cities
  WHERE state_id = 1
  ORDER BY id;
