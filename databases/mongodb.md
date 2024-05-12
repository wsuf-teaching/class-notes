# MongoDB

# Create, insert, find

MongoDB as well as MongoDB compass or MongoDB shell is required for working in a terminal environment. MongoDB Compass is recommended due to its option of visually representating the data.

At this point we refer to a db, but do not create it
```
use junkbank;
```

To add some data, we can use the `insertOne` or the `insertMany` functions. `InsertOne` as the name implies inserts a single document into our collection.

```
db.foods.insertOne({name:"Pizza",description:"Italian dish with various toppings", price: 15, image_url:"pizza.png"});

db.foods.insertOne({name:"Hamburger",description:"Meat, salad and cheese between two buns", price: 10, image_url:"hamburger.png", delicious: true});

db.foods.insertOne({name:"Fish and chips",ingredients:[{name:"Fish"},{name:"Chips"}]})
```

Notice how we did not create a collection first, rather it was created when we first added a document into the collection.
As for the data types, they are similar to SQL, like text, boolean, number, date and time... but most of the cases we do not have to specify them, and they are automatically detected and added by MongoDB. We also have a special type for ID fields, that is `ObjectId`.

From the previous commands, you can also notice how different shapes the data can take, they are not constrained to a fixed schema like in SQL. However if we really want to constraint the data to have the same form, the same 'schema', we can enforce it with inserting the necessary fields with "null" values.
For example ˙`delicious: null` in case of pizza.
Also notice, that MongoDB automatically generates ids for each of the documents, in the following format: `ObjectId("41sad5asd55fsa5d4as654d6asd")`.

We can display the first (n) documents in a collection with the `find` function. If our number of documents is small, it displays all of them, otherwise just the first few: 
```
db.foods.find()
```

We can also add arrays/collections into our documents, like the example below:
```
db.foods.insertOne({name:"Fish and chips",ingredients:[{name:"Fish"},{name:"Chips"}]})
```


`InsertMany` functions quite the same way, we can add a list of documents at once:
```
db.foods.insertMany([
  {name:"Sushi",description:"Raw seafood on rice, Japanese favourite", price: 23},
  {name:"Gyros",description:"Meat cooked on a stick, then served with pita bread and veggies", price: 15, image_url:"gyros.jpg", delicious: "very"}
  ]);
```

## Delete, update

`DeleteOne` and `deleteMany` is similar as well. We can either refer to any fields, like name, description or whatever, or use the Id, the `ObjectId`, with a little more involved syntax that will be guaranteed to uniquely identify a single document. For example:
```
db.foods.deleteOne({"_id":ObjectId("645f42337fad4d38d6839917")})
```

> Your ObjectId string will be different than in the code snippet above.

`UpdateOne` and `UpdateMany` to. They take 2 "objects". First the query that matches documents, then in the `$set` block,. we add the fields that we want to change.
```
db.foods.updateMany({delicious:"very"}, {$set: {delicious: true}});
```


Another option we have is to check weather a field exists or not with the `$exists` keyword:
```
db.foods.updateMany(
   {price: {$exists:false}},
   {$set: {price: 5}}
)
```

## Find, drop

To return only specific fields, we can set the specific field's name to 1 in the projection document as follows. If we set even one field to 1, the rest will automatically be treated as 0 and not shown (except the Ids). The Id field we can manually suppress with setting it to 0. The following snippet only returns the name fields of the documents:
```
db.foods.find({},{name:1, _id:0})
```

Of course we can combine it with selection:
```
db.foods.find({name:"Hamburger"},{name:1})
```

Deleting a collection or database works similarly to SQL:
```
db.foods.drop()
db.dropDatabase()
```

## Inserting larger data

As the shell is based on JavaScript, we can create a JS array locally, then use it with `insertMany` to insert the dataset to the database.

```
var foods = [
  {
    name: 'Sushi',
    description: 'Traditional Japanese dish with fresh raw fish and vinegared rice',
    price: 15.99,
    imageUrl: 'sushi.jpg'
  },
  {
    name: 'Pasta Carbonara',
    description: 'Classic Italian pasta dish with bacon, eggs, cheese, and black pepper',
    price: 12.99,
    imageUrl: 'carbonara.jpg'
  },
  {
    name: 'Chicken Tikka Masala',
    description: 'Creamy and flavorful Indian dish with grilled chicken in a spiced tomato-based sauce',
    price: 11.99,
    imageUrl: 'tikka_masala.jpg'
  },
  {
    name: 'Taco',
    description: 'Mexican street food with a corn or flour tortilla filled with various ingredients',
    price: 3.99,
    imageUrl: 'taco.jpg'
  },
  {
    name: 'Pad Thai',
    description: 'Thai stir-fried rice noodles with eggs, tofu, shrimp, peanuts, and tamarind sauce',
    price: 9.99,
    imageUrl: 'pad_thai.jpg'
  },
  {
    name: 'Steak',
    description: 'Juicy and tender grilled beef steak with a side of vegetables',
    price: 19.99,
    imageUrl: 'steak.jpg'
  },
  {
    name: 'Sushi Roll',
    description: 'Variety of sushi ingredients wrapped in seaweed and rice',
    price: 8.99,
    imageUrl: 'sushi_roll.jpg'
  },
  {
    name: 'Chocolate Cake',
    description: 'Rich and decadent dessert made with layers of chocolate sponge cake and chocolate frosting',
    price: 6.99,
    imageUrl: 'chocolate_cake.jpg'
  },
  {
    name: 'Pho',
    description: 'Vietnamese soup consisting of broth, rice noodles, and various herbs and meats',
    price: 10.99,
    imageUrl: 'pho.jpg'
  },
  {
    name: 'Fish and Chips',
    description: 'Classic British dish with battered and deep-fried fish served with chips (fries)',
    price: 8.99,
    imageUrl: 'fish_chips.jpg'
  }
];
```

Inserting the array:
```
db.foods.insertMany(foods)
```

## More involved queries

We can use keywords, like `$lt`, `$gt`, `$eq`, `$lte`, `$gte` to compare mainly numerical values:
```
db.foods.find({price: {$gt: 10}})
```
```
db.foods.countDocuments({price: {$gt: 10}})
```

There are also `$or`, `$and` and `$nor` operator as well to connect multiple statements through boolean logic.
At the same time, for queries involving strings, we can use regex matching:

```
db.foods.find({$or: [{imageUrl: {$regex: /\.jpg/}},{price: {$gt: 10}}]})
```
```
db.foods.find({$and: [{imageUrl: {$regex: /\.jpg/}},{price: {$gt: 10}}]})
```
```
db.foods.find({$nor: [{imageUrl: {$regex: /\.png/}},{price: {$gt: 10}}]})
```

Types can be checked with the `$type` keyword:
```
db.foods.find({price: {$type: "number"}})
```

Through JavaScript, let's add an old price field for each documents in the collection, that can randomly be higher or lower than the original price:
```
db.foods.find().forEach(function(doc) {
  var randomMultiplier = Math.random() > 0.5 ? 1 + (Math.random() * 0.2) : 1 - (Math.random() * 0.2); 
  var oldPrice = doc.price * randomMultiplier; 
  db.foods.updateOne(
    { _id: doc._id },
    { $set: { oldPrice: oldPrice } }
  );
});
```

Now we can compare the price and the oldprice fields with `$lt` as well: 
```
db.foods.find({$expr: {$lt: ["$price","$oldPrice"]}})
```


## Connections

Let's see some easy examples of document connections as well:

The snippet below is an example of one-to-many, but one-to-one works pretty much the same way, provided we don't wadd multiple addresses to a person.
In this example one user can has multiple addresses, and an address belongs to a single user only.
In a traditional SQL database, we would have two tables for this, but in MongoDB we can just add the addresses as a (sub-)collection under a user's datafields.

```
db.users.insertMany([
  {
    name: "John Doe",
    email: "john@example.com",
    addresses: [
       {
          street: "Fo utca 3",
          city: "Budapest",
          country: "Hungary"
       },
       {
          street: "Vesterbro 56",
          city: "Aalborg",
          country: "Denmark"
       }
    ],
  },
  {
    name: "Jane Smith",
    email: "jane@example.com",
    addresses: [
       {
          street: "Maple Avenue 1349",
          city: "Los Angeles",
          country: "USA"
       },
    ]
  },
  {
    name: "David Johnson",
    email: "david@example.com",
    addresses: [
       {
          street: "Higashi-Tonden-dori 66",
          city: "Tokyo",
          country: "Japan"
       },
       {
          street: "Aleksanterinkatu 1",
          city: "Helsinki",
          country: "Finland"
       },
    ]
  },
  {
    name: "Sarah Brown",
    email: "sarah@example.com",
    addresses: [
       {
          street: "Baker Street 10",
          city: "London",
          country: "Great Britain"
       },
    ]
  },
  {
    name: "Michael Davis",
    email: "michael@example.com",
    addresses: [
       {
          street: "Timarpur Road 14",
          city: "New Delhi",
          country: "India"
       },
    ]
  }
]);
```


Find users having at least one address in Hungary:
```
db.users.find({ "addresses.country": "Hungary" })
db.users.find({ "addresses.country": "Hungary" }, { name: 1, email: 1 })
```

Users having both a Hungarian and Danish address:

```
db.users.find({ "addresses.country": "Hungary", "addresses.country": "Denmark })
```


Show the addresses of Jane Smith:
```
db.users.find({ name: "Jane Smith" }, { "addresses": 1 })
```


Of course we can use mongodb like regular SQL, meaning linking different collections with ids between documents, like for example a many-to-many collection. Create a new orders collection as we did, and add rows connecting a user and a food. Fortunately we have better ways to do the same, we don't need to add new collections.
We can reference the foods as orders under a customers documents:

Let's add random number of orders with random number of foods and random number of food items under each user, dynamically!

```js
// function to generate a random number within a range
function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// find all users
var users = db.users.find();

// iterate through each user
users.forEach(function(user) {
    // get a random number of orders (between 1 and 3)
    var numOrders = getRandomInt(1, 3);
    
    var orders = [];

    // generate random orders
    for (var i = 0; i < numOrders; i++) {
        // get a random number of food items for each order (between 1 and 3)
        var numUniqueFoodItems = getRandomInt(1, 3);

        var orderFoods = [];

        // get all food items
        var allFoodItems = db.foods.find().toArray();

        // generate random order
        for (var j = 0; j < numUniqueFoodItems; j++) {
            // get a random food item
            var randomIndex = getRandomInt(0, allFoodItems.length - 1);
            var randomFood = allFoodItems[randomIndex];

            // generate a random amount for the food item (between 1 and 5)
            var amount = getRandomInt(1, 5);

            var orderFood = {
                food: randomFood._id,
                amount: amount
            };

            // push order food to orderFoods array
            orderFoods.push(orderFood);

            // remove the selected food item from the array to ensure uniqueness in each order
            allFoodItems.splice(randomIndex, 1);
        }

        // push order foods to orders array
        orders.push(orderFoods);
    }

    // update user document with orders
    db.users.updateOne(
        { _id: user._id },
        { $set: { orders: orders } }
    );
});
```

> Once again, fill the ObjectId's appropriately with your own ones.

## Aggregate queries:

Now we can do aggregate queries on them.

Counting the total number of users:

```js
db.users.aggregate([
  {
    $group: {
      _id: null,
      totalUsers: { $sum: 1 }
    }
  }
])
```

Average price of foods:

```js
db.foods.aggregate([
  {
    $group: {
      _id: null,
      averagePrice: { $avg: "$price" }
    }
  }
])
```

Number of orders a specific user made:

```js
var userId = ObjectId("663b84dc2dad0df4c7df795f");

db.users.aggregate([
  {
    $match: { _id: userId }
  },
  {
    $project: {
      numberOfOrders: { $size: "$orders" }
    }
  }
])
```

Return the names of users who have ordered a specific food.
Keep in mind, that this is a "dummy" example. With highly structured data (and queries on it) we would be better off with regular SQL. NoSQL databases shine working with less structured data.

```javascript
var foodName = "Sushi"

db.users.aggregate([
  // unwind the orders array
  { $unwind: "$orders" },
  // lookup to fetch food details for each order item
  {
    $lookup: {
      from: "foods",
      localField: "orders.food",
      foreignField: "_id",
      as: "foodDetails"
    }
  },
  // unwind the foodDetails array to denormalize it
  { $unwind: "$foodDetails" },
  // match orders containing the given food name
  {
    $match: {
      "foodDetails.name": foodName
    }
  },
  // group by user to get distinct users who ordered "Sushi"
  {
    $group: {
      _id: null,
      names: { $addToSet: "$name" }
    }
  },
  // project only the list of names
  {
    $project: {
      _id: 0,
      names: 1
    }
  }
])
```










