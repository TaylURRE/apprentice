USE m6;

CREATE TABLE customers (
	id INT AUTO_INCREMENT ,
	created_time DATETIME(6),
	mod_time DATETIME(6),
	first_name  VARCHAR(255),
	last_name VARCHAR(255),
	email VARCHAR(255),
	sr_member BOOLEAN DEFAULT 0,
	PRIMARY KEY(id),
	UNIQUE KEY unique_customer(first_name, last_name, email)
);


