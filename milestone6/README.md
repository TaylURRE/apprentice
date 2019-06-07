Apprentice Database Skills Evaluation
-------------------------------------
**Goal**: Determine that an Apprentice has basic SQL and database knowledge that could give them an E1 job at any reputable organization.

milestone 6 project README
--------------------------
This application uses Docker start the server locally, Start the Database and Load the data for this activity.
The crud functionality is located in the milestone6/crud.sql file

**Start Docker Application for Use with DB**
1. Build the image from Dockerfile / 
    Start the Docker container in the background

    ```
    docker-compose up -d

    ```
    
2. Connect via dbeaver
    ```
    Server host: localhost
    Port: 3306
    database: mysql
    Username: root
    password: mypassword
    ```
**Start Docker Application for use with command line**
1. Build the image from docker file/
    Start the container in the background
    
    ```
    docker-compose up -d

    ```
2. Enter Container
    ```
    docker exec -it m6_db /bin/bash;
    ```
3. Sign into mysql in command line
    ```
    mysql -u root -p$MYSQL_ROOT_PASSWORD;
    
    ```
4. Select m6 database
    ``` 
        USE m6;
    ```
5. Can now run crud sql commands on the mysql command line
    ```
        #example:
        SHOW tables;
        SELECT * FROM CUSTOMERS;
    ```
    
**Stop Docker Application**
1. Stop and remove
    ```
        docker stop m6_db
        docker rm m6_db
    ```

-------------
Capabilities
------------
**Query basics**
* How to write a query to retrieve from a database :
```'*.sql'
SELECT *
FROM m6.address_book
LIMIT 2;

```
* How to write an query that can do aggregation
```'*.sql'
SELECT count(*), city
FROM m6.address_book
GROUP BY city;

```
* How to write a query that can do an aggregation like count or sum
```'*.sql'
SELECT count(*)
FROM m6.address_book;

```
* How to write a Join query. Understand difference between LEFT and RIGHT joins and INNER and OUTER joins.
**Joins:** tables joined at a point where a primary key(key in the initial table) matches 
the foreign key(key in external table)
    * **Left JOIN**  displays the data on the primary table where the primary key exists on the foreign table with
data that exist only exists the primary table.
    * **Right JOIN** displays the data from the foreign table where the foreign key exists in the primary table and data that
only exists on the foreign table.
    * **INNER JOIN** return data from connected table where primary and foreign key connect excludes null values for these keys

```'*.sql'
###Inner Join
SELECT *
FROM m6.address_book a 
JOIN m6.customers c  ON a.customer_id = c.id;


```

```'*.sql'
##Left Join
SELECT *
FROM m6.address_book a 
LEFT JOIN m6.customers c  ON a.customer_id = c.id;

```
```'*.sql'
##RightJoin
SELECT *
FROM m6.address_book a 
RIGHT JOIN m6.customers c  ON a.customer_id = c.id;

```
* How to use GROUP BY and SORT BY
```'*.sql'
##GROUP BY

SELECT count(*), sr_member
FROM m6.customers
GROUP BY sr_member;

```
```'*.sql'
##SORT BY
SELECT *
FROM m6.customers
SORT BY last_name ASC;

##ASC can be exchanged for DESC
```
* How to use EXPLAIN to debug a query:
EXPLAIN gives the optimal plan for executing a query.  The output can be used to modify keys used or increase optimization
by understanding current query performance.
**The output includes:**  
    * id: identifies each select (useful when running subqueries)
    * select_type: type of the select used
    * table: table referred to by row 
    * type: how mysql joins table (ALL, worst scenario scans the entire table)
    * possible_keys: shows possible keys that can be used 
    * key: shows the actual key used
    * key_len: length of the index query optimizer chose to use
    * ref: shows column referenced
    * rows: lists the number of rows examined
    * filtered: rows that where filtered through the query.
    * extra: additional information about how a query was resolved ie 'Using Where'
additional debugging: I read the output to determine what kind of error that occurred. I like to place each statement on
 a new line so the output is  cleaner to understand. It will tell you where things went wrong.

Data modeling basics
--------------------
* Understand what ACID means
Database properties that guarantee data exists regardless of external factors ie power failures, errors
    * Atomicity : If one portion of a transaction fails the whole thing fails. ie insert row if all but one of the columns
    succeeds the transaction will fail.
    * Consistency : Any data must be valid according to the rules. ie You won't find a string in an int column
    * Isolation : One transaction has to be complete before moving on to the next transaction. 
    i.e. Insert customer row and address_book row. If customer row insert first then address_book row added.
    * Durability: What's done is done, if they row is inserted or deleted that state is maintained even in the event of
    power failure
* When to use primary keys, foreign keys, and indexes
    * primary key: a key that is native to that table, one per table, unique, not null
    * foreign key: a key used to reference a primary key in another table, enforces referential integrity
    * indexes: used to find rows in a particular column quickly, good for WHERE clauses, retrieve rows during joins
* Unique constraint | Primary Key constraint: Ensures each item in a give column are unique to that column. No duplicates
* Normalization vs Denormalization:
    * Normalization: process used to organize tables and columns. Essentially each table has a purpose to reduce
    anomalies that can occur on a denormalized table ie
        * Insertion Anomaly- Inserts data incorrectly into table
        * Update Anomaly- With duplicates when updating some may be missed
        * Deletion Anomaly - Deleting a row removing information that is needed elsewhere
    * Denormalization: Undoing all that was done with Normalization
* Design a multiple table database for use from a transactional web service: WIP
* Describe NoSQL and how it differs from traditional relational databases and when to use:
    * NoSQL is a database that you are unable to query using SQL. The advantages of using a NoSQL database include
quicker access to data, ability to create a REST API, ability to scale and access to data in different format(JSON).
The disadvantages are loss of ACID properties, the inability to query takes away the immediate ability to analyze data.

**Data warehousing basics (bonus)**
* OLTP vs OLAP
    * OLTP- High transactions-Online Transaction Processing- Operations Business Process -(INSERT, UPDATE, DELETE)
    * OLAP- low transactions-Online Analytical Processing Information Process -Business Data warehouse 
* Star Schema basics- multi-dimensional Schema- denormalized- simpler queries- business reporting-fast aggregation OLAP- Example: snowflake match rate
* Cluster Keys - Subset of columns or expressions on a tables that are explicitly defined when creating a table. id and date example want to look at a particular day, daily feed
* Data extraction via ETL, ELT, etc- Extract Transform Load, Extract Load Transform

**Big Data basics (bonus)**
* MapReduce- programming model for big data, figure out what goes where, shuffle and reduce to smaller subsets

**Data Collection basics (bonus)**
* Demonstrate when to collect data to a database (transactions) vs when to collect data via a log (analytics)
    no restricted to structured data structures

**Data Security basics (bonus)**
* PII- Personally Identifiable Information | Info to identify, contact or location of a person
* PCI- Payment Card Industry Data Security is a set of security standards designed to ensure that ALL companies that accept, process, store or transmit credit card information maintain a secure environment.
* Understand Encrypted columns- Pass through different encryption functions
* Understand database permissions ROLE SCHEMA SECURITY
