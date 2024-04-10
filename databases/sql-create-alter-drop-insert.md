# SQL

Standing for Structured Query Language. There exists an "SQL standard", but various companies made various dialects of SQL languages, and inter-operability between them is not 100% given.

SQL is a declarative language, not a procedural one. We declare what we want to do, and not how we want to do it.
It is quite similar to natural language spoken.
Consider the following example:

```sql
SELECT name FROM food WHERE price > 5;
```

SQL operation types:

** Data Definition Language (DDL) **
Defining and creating the modal and structure of the data.

** Data Manipulation Language (DML)
Modifying or adding data into the database.

** Query Language **
Accessing (part) of the data, based on various conditions.

** Other **
Like transaction processing, etc.

## Database

In SQL, a database refers to a structured collection of data organized and managed according to a specific data model. It typically consists of one or more tables, each containing rows and columns. 

## Creating a database

> If we did not create a user at installation time, we should log in through the terminal first.
> This can be done through the `MySQL 8.0 Command Line Client` (with your appropriate version). If you supply the prompted root password correctly, you can log in.
> To create a database, issue the `CREATE DATABASE myfirstdb` command.
> Then it is also a good idea to specify a specific user to handle this database instead of the root user.
> `CREATE USER 'mydbuser'@'localhost' IDENTIFIED BY '12345';`
> And also assign it to the DB. `GRANT ALL PRIVILEGES ON myfirstdb.* TO mydbuser@localhost;`
> Afterwards, we can either use this command line client, MySQL through our favourite terminal emulator, or through a graphical user interface.
> To use it from any terminal, CD to the path of the MySQL installation. For example `C:\Program Files\MySQL\MySQL Server 8.0\bin\`. There, run `mysql.exe -u root -p nameofdatabase`, it will prompt for your password again and then you can log in.


```sql
CREATE DATABASE myfirstdb;
```

If we try to run it again, we will get an error saying it already exists. 
Listing available databases can be done by the `SHOW DATABASES` command. Deleting one is with `DROP DATABASE nameofyourdatabase`.

To start working with tables, we can to select a database to be active, we need to `use` it.

```sql
USE myfirstdb;
```

> Using a database is not mandatory, as we can prepend every table name with the name of the database schema as in the examples below. Using it however is probably more convenient.


## Table operations

### Creating tables

Tables represent entities or relationships between entities in the real world, and the rows within these tables represent individual records or instances of those entities. Columns define the attributes or properties of the entities.

There are some rules regarding naming tables:
* Must begin with a letter and must only contain [a-z, A-Z, 0-9, _, #, $] characters.
* Often must be 1-30 characters long
* Must be unique. Two tables in a database cannot have the same name.
* Must not used vendor-specific [reserved keywords](https://dev.mysql.com/doc/refman/8.0/en/keywords.html).
  For example for MySQL: ADD, AND, ASC, CHAR, DROP, FALSE, etc.

The basic syntax for creating a table is as follows:

```
CREATE TABLE [schema.]table (
    column datatype [DEFAULT value],
    [...]
)
```

`schema` is an optional parametre, the name of the database we want to create the table in.
`table` is the name of the table being created.
`column` is the name of a column of the table being created.
`datatype` specifies the data type of the column.
`[DEFAULT expr]` is another optional clause that allows us to specify a default value for the column. If a value is not explicitly provided during insertion, the default value (`expr`) will be used.
`[...]` just means that we can have (any) number of columns.

Some types that can be used:

| Data Type      | Description                                  |
|----------------|----------------------------------------------|
| INT            | Integer                                      |
| VARCHAR(size)  | Variable-length character string             |
| CHAR(size)     | Fixed-length character string                |
| TEXT           | Variable-length character string (large)     |
| DATE           | Date                                         |
| TIME           | Time                                         |
| DATETIME       | Date and time                                |
| TIMESTAMP      | Timestamp                                    |
| DECIMAL(p,s)   | Fixed-point decimal number                   |
| FLOAT(p)       | Floating-point number                        |
| DOUBLE(p)      | Double-precision floating-point number       |
| BOOLEAN        | Synonym for TINYINT(1)                       |
| ENUM(x,y,z,...)| Enumeration (list of values)                 |
| SET            | Set (multiple choices)                       |
| BLOB           | Binary large object (large binary data)      |

For example, creating a table:

```sql
CREATE TABLE IF NOT EXISTS foods(
  id INT,
  name VARCHAR(50),
  description TEXT,
  price DECIMAL(4,2),
  image VARCHAR(255)
);
```

After, the creation of a table can be confirmed with the `DESCRIBE` command.

```sql
DESCRIBE foods;
```

### Deleting, modifying tables

To delete a table, use the `DROP TABLE` command.

```sql
DROP TABLE foods;
```

Tables can be assigned new names. The first parameter between `TABLE` and `TO` is the old name of the table, and the one after the `TO` is the new name.

```sql
RENAME TABLE foods TO foods2
```

Tables can also be modified multiple ways. We can rename their columns for example:

```sql
ALTER TABLE foods
RENAME COLUMN name TO foodname;
```

Or change their data types:
```sql
ALTER TABLE foods
MODIFY COLUMN name VARCHAR(60);
```

## Constraints

Constraints are rules or conditions that enforce data integrity and consistency by restricting the type or range of values that can be stored. They enforce rules at the level of tables or columns, and are created with standard SQL statements either when the table is created or when it is altered.

A `PRIMARY KEY` constraint ensures that each row in a table is uniquely identified by a set of one or more columns. It prevents duplicate or null values in the primary key columns and enforces entity integrity. Typically, primary keys are used as unique identifiers for rows in a table.

A `FOREIGN KEY` constraint establishes a relationship between two tables by enforcing referential integrity. It ensures that the values in a column (or set of columns) in one table match the values in another table's primary key or unique key column(s). This constraint helps maintain consistency between related tables and prevents orphaned rows.

A `NOT NULL` constraint ensures that a column cannot contain null values. It requires that every row in the table must have a value for the specified column, preventing the insertion of incomplete or missing data. By default, all rows of a table would allow nulls.

A `UNIQUE` constraint ensures that the values in one or more columns of a table are unique, except for null values. It prevents duplicate entries in the specified columns and maintains data integrity. Unlike primary keys, unique constraints allow null values.

A `CHECK` constraint specifies a condition that must be satisfied for the values in a column. It allows you to define custom rules or conditions to restrict the range of values that can be inserted or updated in a column. Check constraints are useful for enforcing business rules or data validation requirements.

### Constraint operations

An example of the constraints from before, creating a new foods table now with constraints:

```sql
CREATE TABLE IF NOT EXISTS foods (
  id INT AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  description TEXT,
  price DECIMAL(4, 2) NOT NULL,
  image VARCHAR(255),
  CONSTRAINT pk_id PRIMARY KEY (id),
  CONSTRAINT uk__name UNIQUE (name),
  CONSTRAINT chk_price CHECK (price > 0)
);
```

In this example, the name of the food cannot be empty and should be unique.
The id field will be the field used to clearly identify a specific row, therefore it is a primary key, and also SQL will handle the creation of these unique ids automatically through `AUTO_INCREMENT`.
The price also has to be assigned a value greater than zero.

> `AUTO_INCREMENT` means that each new row inserted into the table will automatically be assigned a unique ID starting from 1 and incrementing by 1 for each subsequent row.

> Notice, how some constraints are put at the bottom, and some at the end of the column definitions. These are interchangeable, and up to preference or company standards.

Adding the same constraints after the table has already been created:

```sql
ALTER TABLE foods
MODIFY COLUMN id INT AUTO_INCREMENT,
MODIFY COLUMN name VARCHAR(50) NOT NULL,
MODIFY COLUMN price DECIMAL(4,2) NOT NULL,
ADD CONSTRAINT pk_id PRIMARY KEY (id),
ADD CONSTRAINT uk_name UNIQUE (name),
ADD CONSTRAINT chk_price CHECK (price > 0);
```

> In this case, a name must also be supplied to the constraints.

> We will look at the `FOREIGN KEY` constraint a little later.

Named constraints (uk_name, chk_price from above) can be easily removed.

```sql
ALTER TABLE foods
DROP CONSTRAINT chk_price;
```

## Inserting data

The `INSERT` statements adds new rows of data to a table, one at a time.

The abstract syntax looks like this: 

```sql
INSERT INTO tablename [(columnname1 [, columname2...])]
VALUES (value1 [, value2...]);
```

We need to specify the table, and the columns we want to insert values into, and finally the actual values.
In practice, we can even add more rows of data with one `INSERT` statement.

```sql
INSERT INTO foods (name, description, price, image) VALUES
('Pizza', 'Delicious pizza with pepperoni and cheese toppings', 10.99, 'pizza.jpg'),
('Burger', 'Beef burger with lettuce, tomato, and pickles', 8.49, 'burger.jpg'),
('Salad', 'Fresh garden salad with mixed greens and balsamic dressing', 6.99, 'salad.jpg');
```

This is called the "explicit" insert, as we have to manually specify which columns (and their data) and in which order they will be present.

An "implicit" insert works pretty similarly, but it assumes that the column data is supplied in the "correct" (as the table was specified) order. In this case, all values have to be supplied in order, or be passed a `NULL` value if we would like to leave it out.

```sql
INSERT INTO foods VALUES (NULL, 'Sushi', 'Assorted sushi rolls with wasabi and soy sauce', 12.99, 'sushi.jpg');
```

Once again, with the explicit insert, we can specify just a select few values to insert into the table as a new row.

In our case, the "description" and "image" columns are nullable, so we can leave them out.

```sql
INSERT INTO foods (name, price) VALUES ('Tacos', 9.99);
```

To do the same with an implicit insert, we have to supply `NULL`s in those cases.

```sql
INSERT INTO foods VALUES (NULL, 'Pasta', NULL, 12.99, NULL);
```

> Sending `NULL` into an `AUTO_INCREMENT` column will replace it with the actual automatically incremented ID.


