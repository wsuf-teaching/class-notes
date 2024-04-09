## Entity-relation model

### Entities

In the context of database management, the entity-relationship (ER) model is not considered a data model in the strict sense because it does not define data operations. Instead, it focuses on the elements of the ER model, which include entity types, attribute types, and relationship types.

Entities represent real-world objects with distinct identities, either logically or physically. These entities are grouped into sets based on common characteristics. For example, entities could be cars, people, contracts, etc. Each entity type has its own set of instances or occurrences.

Attributes characterize entities and help distinguish them from one another. Attributes can be properties or characteristics of entities. The definition of attributes for entities is a modeling decision, and it determines how entities are uniquely identified and differentiated. For example, attributes for a person entity could include name, date of birth, mother's name, eye color, etc.

An entity set is a collection of entities that share the same attribute types. It represents a grouping of entities with similar characteristics. Entity sets are usually denoted with the name of the entity type, followed by a list of common attribute types enclosed in parentheses. For example:

```
ACCOUNT(name, password, email)
FOOD(name, description, price)
```

![a](.//examples/erdiagram.png)

### Relations

In reality, entities rarely exist in isolation; they typically have relationships with each other, such as foods, user accounts, and orders making relations between the two. A relationship is some form of connection between entities. Relationships vary widely, and it's important to consider factors like the number of entity sets involved and the minimum or maximum number of related entities per instance. 

```
ORDERS: ACCOUNT, ORDER
```


In a one-to-one relationship, each instance of one entity set can be associated with at most one instance of another entity set. This implies a strict cardinality of one-to-one correspondence between the entities involved.

```
PRIME_MINISTER: PERSON, COUNTRY
HAVE: NETWORK_INTERFACE, MAC_ADDRESS
```

> Defining proper cardinalities is a very important modelling question, and the answer is often "it depends". In Hungary, MARRIAGE would define a one-to-one relationships, but it may be defined as a one-to-many in other countries. Similarly, with countries allowing for more than one full-time jobs, or multiple active passports at a time..



In a many-to-one relationship, instances of one entity set can be associated with at most one instance of another entity set, but instances of the second entity set can be associated with any number of instances of the first entity set. This implies a cardinality where multiple instances of one entity map to a single instance of another entity.

```
ORDERS: CUSTOMER, ORDER
DELIVERS: DRIVER, FOODS
STUDIES: STUDENT, CLASS
```

In a many-to-many relationship, instances of one entity set can be associated with any number of instances of another entity set, and vice versa. This implies a cardinality where multiple instances of one entity can be related to multiple instances of another entity.

```
ORDERS2: CUSTOMER, FOOD
TEACHES: STUDENT, TEACHER
```

![a](.//examples/cardinality.png)

Relationships can also have properties.

```
WORKS: PERSON, COMPANY; date
```

The date property here cannot be individually connected to either a person or a company, it only makes sense in context of the relationship. For example the starting date of a work contract.

![a](.//examples/relationprop.png)


### Keys

Keys are what makes an entity an entity, uniquely identifying it.

For example passport or id card number for a person, order number for a food order, or an auto-generated or uuid for a specific food.

<example of a food drawing in ER diagram form>

### IsA

A popular extension of the default ER syntax is the "IsA". 
It is common, when each element of an entity set has attributes from another, more general entity set, but also additional attributes beyond that.

![a](.//examples/isa.png)

### Weak entity

A weak entity is an entity that does not have its own unique, identifiable key. Instead, it relies on a related entity (known as the "owner entity") for its identification. In other words, a weak entity is in a one-to-many relationship with its owner entity, and its existence depends on the existence of the owner entity. If the owner entity is deleted, the weak entity is also deleted or its state is altered. Weak entities are often used in situations where an entity cannot identify itself independently and is closely associated with another entity.

For example, consider a scenario of a university database

Entity: Student
Weak Entity: Course Enrollment

![a](.//examples/weakentity.png)