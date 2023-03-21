-- Create a database and a table
-- `id` INT unique, auto generated, can't be null and is primary key

-- Create a database 'hbtn_0d_usa'
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to new database
USE hbtn_0d_usa;

-- Create a table 'states' in database 'hbtn_0d_usa'
CREATE TABLE states (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(256) NOT NULL,
  PRIMARY KEY (`id`)
  -- UNIQUE (id) // Primary key is also UNIQUE
);
