-- Script for show list with contain the cities of California in the database
SELECT id, name FROM cities WHERE state_id =
        (SELECT id FROM states WHERE name = 'California') ORDER BY id DESC;
