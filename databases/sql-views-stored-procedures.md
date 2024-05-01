## Views

Views are virtual tables created by a query. They allow us to simplify complex queries and joins by providing a level of abstraction by presenting data in a format that is easier to understand or work with than the underlying tables. They can combine data from multiple tables into a single virtual table, that would later be reuseable by other queries.

Views can also work as a securit mechanism restricting access to certain columns or rows of a table, providing a security mechanism to control what data users can see or manipulate. This is particularly useful for enforcing data access policies and protecting sensitive information.

For example we can create a table that combines the name of the user who placed an order with the order's id, simplifying later queries that use these informations, while still storeing the actual data parts separate and storeing them in a non redundant way:

```sql
CREATE VIEW order_details AS
SELECT orders.id AS order_id, 
	   orders.order_date AS order_date, 
       users.id AS user_id, 
       users.first_name AS first_name, 
       users.last_name AS last_name
FROM orders
JOIN users ON orders.user_id = users.id;
select * from order_details;
```

Let's see the data:

```sql
SELECT * FROM order_details;
```

Views can be dropped just like tables or databases, deleting them:

```sql
DROP VIEW order_details;
```

With using this view, we no longer have to join multiple tables to for example tell which user (showing its name) placed the most orders:

```sql
SELECT user_id, first_name, last_name, COUNT(order_id) AS total_orders
FROM order_details
GROUP BY user_id
ORDER BY total_orders DESC
LIMIT 1;
```

## Indexes

Indexes are data structures that improve the speed of data retrieval operations on tables by providing quick access to rows based on the values of certain columns. They work similarly to the index of a book, allowing the database to quickly locate rows that match a specific condition without having to scan the entire table.

Advantages:
* Improved join, sorting, grouping, and overall query performances.

Disadvantages / considerations:
* Indexes present an additional overhead, consuming additional disk space and may impact the performance of write operations (inserts, updates, and deletes).
* Indexes need to be maintained as data is inserted, updated, or deleted from the table, which can impact database performance.
* The "selectivity" of an index refers to the percentage of rows in the table that match a particular value. Highly selective indexes are more efficient. Indexes are most effective for columns frequently used in search conditions, joins, and sorting operations and with highly unique values.

```sql
CREATE INDEX idx_user_id ON orders (user_id);
```

```sql
CREATE INDEX idx_order_date_user_id ON orders (order_date, user_id);
```

## Stored procedures

Stored procedures are precompiled SQL code blocks stored in the database. They work very similarly to "functions" in an imperative programming language like Java or JavaScript. They can accept input parameters, perform operations on the database, and return results. They can contain SQL statements, control-of-flow statements (like IF-ELSE and LOOP), variables, and error handling logic.
Stored procedures are compiled and optimized by the database server, which can lead to improved performance compared to executing ad-hoc SQL statements.

```sql
-- Create the stored procedure, the "delimiter //" trick is needed so we can write ";" inside it
DELIMITER //

CREATE PROCEDURE GetOrderCountByUser(
    IN userId INT,
    OUT orderCount INT
)
BEGIN
    SELECT COUNT(*) INTO orderCount
    FROM orders
    WHERE user_id = userId;
END//

DELIMITER ;

-- Declare variables to hold the input and output parameters
SET @userId = 1;
SET @orderCount = 0;

-- Call the stored procedure
CALL GetOrderCountByUser(@userId, @orderCount);

-- Output the result
SELECT @orderCount AS OrderCount;
```


