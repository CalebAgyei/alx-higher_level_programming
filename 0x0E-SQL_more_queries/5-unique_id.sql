-- Create a table `unique_id` on MySQL server.
-- `id` INT with default value 1 and must be unique

CREATE TABLE IF NOT EXISTS unique_id (
  `id` INT DEFAULT 1,
  `name` VARCHAR(256),
  UNIQUE (id)
);
