# Databases

Databases are organized collections of data, describing a subset of the real world, typically stored electronically in a computer system. 
They are designed to efficiently manage, store, retrieve, and update large volumes of data. Databases are fundamental to many aspects of modern computing, from business applications to scientific research and beyond.

A database management system (DBMS) is the hardware-software system that allows high-level access or modification of this data for one or more users. DBMS characteristics include handling large amounts of data, complex structures, and long lifecycles. Data in DBMS are primarily stored on hard disk drives (HDDs), with increasing use of solid-state drives (SSDs). The rich structure of databases allows for various logical relationships between stored records, facilitating specific database operations. The high level of data management means users can interact with the DBMS without detailed knowledge of its algorithms or data storage principles.

The usage of classical DBMS involves two main phases: defining the logical structure of data storage, known as creating the database schema (Phase 1), followed by data manipulation and querying (Phase 2).

Phase 1 involves defining the schema using a data definition language (DDL), which is then interpreted and translated by the schema compiler. 

Phase 2 involves querying the database using a data manipulation language (DML). 

The central component of a DBMS is the database manager, responsible for handling user queries based on the translated schema and ensuring security, synchronization, and integrity. 
The file manager provides access to the physical database and interacts closely with the operating system. Ultimately, data must be persistently stored to mitigate the risk of data loss.


## Ancillary tasks

**Privacy:** Not all users can access all data stored in the database. Access permissions vary, and sensitive data like personal information may have restricted access, often requiring passwords or other security measures.

**Security:** Certain databases hold valuable data, necessitating measures to prevent their destruction or partial loss even in extreme circumstances. This includes logging, regular backups, redundant data files, and distributed operation.

**Integrity:** It's crucial to ensure the correctness and consistency of database data, especially during operations like insertion, deletion, or modification. DBMS ideally prevents actions that violate integrity, but sometimes application-level checks are required.

**Synchronization:** Modern DBMSs are often multi-user and distributed, requiring mechanisms to handle concurrent operations without undesired effects on each other's activities or the database content. Transaction processing methods, such as locks, ensure synchronization.

## Database management system structure

Today's database management systems (DBMS) are complex hardware-software systems comparable in complexity to operating systems, sometimes even more so. Designing, implementing, and maintaining such systems is a challenging task, requiring sophisticated methods. 

Layered architecture, similar to the OSI model for computer networks, is commonly used in DBMS design. This model divides the system into layers, with each layer building upon the one below it, minimizing interaction between layers. 
The three-layer model is a common approach, consisting of the physical database layer, the conceptual database layer, and the view layer. 


* Physical database layer deals with storing data on physical storage devices.
* The conceptual database layer represents a model of the real world and is closely related to how data is interpreted. 
* Views represent different perspectives of the database accessible to users. 

A well-designed system based on layering allows for independent modification and replacement of layers as long as the interfaces between layers remain unchanged, a concept known as data independence. Two types of data independence exist: 
* physical data independence, where changes at the physical level don't affect the logical database
* logical data independence, where changes to the logical database don't impact user views.

## Main types of databases

**Relational Databases:** Relational databases store data in tables, with each table consisting of rows (records) and columns (fields). They use structured query language (SQL) for querying and managing data. Examples include MySQL, PostgreSQL, Oracle, and SQL Server.

**NoSQL Databases:** NoSQL databases diverge from the traditional relational model, offering more flexibility in handling unstructured and semi-structured data. They are well-suited for large-scale distributed data storage and real-time applications. Examples include MongoDB, Cassandra, Couchbase, and Redis.

**Object-Oriented Databases:** Object-oriented databases store data as objects, which encapsulate both data and behavior. They are ideal for applications with complex data structures and relationships, such as object-oriented programming languages like Java and C++. Examples include db4o and ObjectDB.


Relational databases follow a tabular data model, while NoSQL databases can adopt various models such as document-oriented, key-value, wide-column, or graph-based. Object-oriented databases store data as objects with attributes and methods.

NoSQL databases are often more scalable and can handle large volumes of data across distributed systems more effectively than relational databases.

NoSQL databases offer greater flexibility in schema design and data modeling, allowing for easier adaptation to changing data requirements compared to rigidly structured relational databases. However at the same time SQL databases are better for protecting data validity - dealing with highly structured data.