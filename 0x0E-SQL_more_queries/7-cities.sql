-- Script for create the database hbtn_0d_usa and the table cities

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE hbtn_0d_usa.states(id INT UNIQUE AUTO_INCREMENT, name VARCHAR(256) NOT NULL);

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE hbtn_0d_usa.cities(id INT UNIQUE AUTO_INCREMENT NOT NULL, 
       	     			PRIMARY KEY(id),
       	     			state_id INT NOT NULL,
				FOREIGN KEY (state_id) REFERENCES states(id),
				name VARCHAR(256) NOT NULL);
