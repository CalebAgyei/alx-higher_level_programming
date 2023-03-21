-- Create a new database and a new table in MySQL server.

--
-- Create database 'hbtn_0d_usa'
--
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

--
-- Switch to the new databse 'hbtn_0d_usa'
--
USE hbtn_0d_usa;

--
-- Create table 'cities' in 'hbtn_0d_usa'
--
CREATE TABLE cities (
  `id` INT NOT NULL AUTO_INCREMENT,
  `state_id` INT NOT NULL,
  `name` VARCHAR(256) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`state_id`) REFERENCES states (`id`)
);
