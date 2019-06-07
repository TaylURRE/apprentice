USE m6;
#LOAD address data
LOAD DATA LOCAL INFILE './tmp/customers_fill.csv'
INTO TABLE address_book
FIELDS TERMINATED BY ','
LINES TERMINATED BY ';'
(customer_id, address, city, state, zip_code, primary_address)  SET created_time=CURRENT_TIMESTAMP, mod_time=CURRENT_TIMESTAMP;
