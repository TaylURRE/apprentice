USE m6;
## LOAD customer data
LOAD DATA LOCAL INFILE './tmp/address_fill.csv'
INTO TABLE customers
FIELDS TERMINATED BY ','
LINES TERMINATED BY ';'
(first_name, last_name, email, sr_member)  SET created_time=CURRENT_TIMESTAMP, mod_time=CURRENT_TIMESTAMP;

## Set foreign key
ALTER TABLE address_book
	ADD FOREIGN KEY(customer_id) REFERENCES customers(id);