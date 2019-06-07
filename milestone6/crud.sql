### SET VARIABLES
SET @first_name = 'Bar',
@last_name = 'Foo',
@mod_time = CURRENT_TIMESTAMP,
@email = 'foo@g.com',
@sr_member = 1,
@address = '736 Lighthouse',
@city = 'New York',
@state = 'NY',
@zip_code = '32242',
@primary_address = 1;

### INSERT NEW Customer/address
BEGIN;

INSERT INTO customers (
	created_time,
	mod_time,
	first_name ,
	last_name,
	email,
	sr_member
)
VALUES (
	CURRENT_TIMESTAMP,
	@mod_time,
	@first_name,
	@last_name,
	@email,
	@sr_member
);

INSERT INTO address_book (
	customer_id,
	created_time,
	mod_time,
	address,
	city,
	state,
	zip_code,
	primary_address
)

VALUES (
	last_insert_id(),
	CURRENT_TIMESTAMP,
	CURRENT_TIMESTAMP,
	@address,
	@city,
	@state,
	@zip_code,
	@primary_address
);
COMMIT;

####READ USER
SELECT id, first_name, last_name
FROM customers
WHERE id=2;

###READ ADDRESS BOOK ##WIP

SELECT c.first_name, c.last_name, sr_member, ab.address, ab.city,ab.state, ab.zip_code, ab.primary_address
FROM customers c
	JOIN address_book ab
		ON c.id = ab.customer_id
WHERE c.id=3;


###READ PRIMARY ADDRESS FOR A USER
SELECT c.first_name, c.last_name, sr_member, ab.address, ab.city,ab.state, ab.zip_code, ab.primary_address
FROM customers c
	JOIN address_book ab
		ON c.id = ab.customer_id
WHERE c.id=3 AND ab.primary_address=1;

### UPDATE USER
UPDATE customers
SET mod_time=CURRENT_TIMESTAMP,
	first_name='Her',
	last_name='Gee',
	sr_member=1
WHERE id=3;

### UPDATE AN ADDRESS
UPDATE address_book
SET mod_time=DATE(NOW()),
	address= @address,
	city= @city,
	state= @city,
	zip_code=@zip_code,
	primary_address=0
WHERE id=2 AND customer_id=3;

### UPDATE AN ADDRESS TO PRIMARY
UPDATE address_book
SET primary_address=0
WHERE customer_id=2 and primary_address=1;

UPDATE address_book
SET primary_address=1
WHERE customer_id=2 and id=2;

###DELETE AN ADDRESS
DELETE FROM address_book
WHERE id=5;

### DELETE A  USER
DELETE FROM address_book
WHERE customer_id=1;
DELETE FROM customers
WHERE id=1;
