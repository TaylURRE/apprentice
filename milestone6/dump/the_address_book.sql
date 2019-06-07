CREATE TABLE address_book (
	id INT AUTO_INCREMENT ,
	customer_id INT,
	created_time DATETIME(6),
	mod_time DATETIME(6),
	address  VARCHAR(255),
	city VARCHAR(255),
	state VARCHAR(255),
	zip_code VARCHAR(255),
	primary_address BOOLEAN DEFAULT 0,
	PRIMARY KEY(id),
	UNIQUE KEY unique_address(customer_id, address, city, state, zip_code)
);