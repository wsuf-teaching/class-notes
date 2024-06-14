# Advanced Flask concepts

Here, we are going to see of the more advanced features of Flask, like database connectivity using SQLAlchemy and AAA (Authorization, Authentication and Accounting).
First, let's install the prerequisite packages with PIP.

```sh
pip install flask flask_migrate flask_bcrypt flask_login flask_sqlalchemy
```

> Once again, all the files are included in this folder on github.

> We assume that we have sqlite3 installed and added to the environmental variables.


```python
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    return app

app = create_app()

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```

First we setup the project similarly as before. Noteable changes that will happen are the database uri configuration value, the migration object and moving all of this logic over to a separate function.
Just to see whether it works, a simple hello world route is created too.


## Database setup, models and data

To create the db, run the command `sqlite3 data.db`, `data.db ""` or `data.db " "`. Command lines on Windows prefer the last format.

Let's also create a db file, that is pretty simple, but if we want to import models in the man file, it helps avoid circular dependencies with imports.

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

Also configure the database in the app.py, getting us to this state:

```python
from flask import Flask, jsonify
from db import db

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///C://sqlproject//data.db" # enter the actual path for your project
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["DEBUG"] = True
    db.init_app(app)
    return app

app = create_app()

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```


Now we can create the food file (in the `models` folder), that will host and represent both the model in memory, the table in the database and class and object functions related to them.
First we define the table columns, that will be interpreted by SQL, but we define them in sqlalchemy python syntax. Then the constructor to create new items.
This is followed by the `get_all` and `get_one` methods retrieving either all or a single element from the database.
Lastly we also create the `json` and `__repr__` functions. The former we will use when returning one element through the API, and the latter mainly 
for debugging purposes, so we can see more meaningful messages when printing out a variable.

```python
from db import db

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

    def __init__(self, name, description, price, image_url):
        self.name = name
        self.description = description
        self.price = price
        self.image_url = image_url

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, food_id):
        return cls.query.get(food_id)

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'image_url': self.image_url
        }

    def __repr__(self):
        return f"Food('{self.name}', '{self.description}', '{self.price}', '{self.image_url}')"
```

As we now have a proper model class, we have to set up "migrations". Migration is the process of setting up, modifying or moving data between databases.

```python
from flask import Flask, jsonify
from flask_migrate import Migrate
from db import db
from models.food import Food

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///I://aaa//data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["DEBUG"] = True
    db.init_app(app)
    return app

app = create_app()
migrate = Migrate(app, db)
with app.app_context():
    print("Tables loaded and initialised")
    #db.drop_all()
    db.create_all()

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```


Create the initial migrations now as well, so we can respond to db schema changes more easily later. In the command line, run:

```sh
flask db init
flask db migrate
```

To the code, add a function that populates the database, the "seed" function:

```python
def seed():
    food1 = Food(name='Pizza', description='Dish of Italian origin', price=10.99, image_url='image1.jpg')
    food2 = Food(name='Hamburger', description='Meat and vegetables in a bun', price=15.99, image_url='image2.jpg')
    food3 = Food(name='Sushi', description='Raw fish in rice', price=12.99, image_url='image3.jpg')
    food4 = Food(name='Pasta', description='Italian dish of noodles', price=11.99, image_url='image4.jpg')
    food5 = Food(name='Steak', description='Roasted meat', price=20.99, image_url='image5.jpg')
    food6 = Food(name='Pho', description='Vietnamese noodle soup', price=9.99, image_url='image6.jpg')
    food7 = Food(name='Tacos', description='Mexican dish of tortilla and meat', price=8.99, image_url='image7.jpg')
    food8 = Food(name='Ramen', description='Japanese noodle soup', price=11.99, image_url='image8.jpg')
    food9 = Food(name='Curry', description='Indian dish of meat and vegetables', price=12.99, image_url='image9.jpg')
    food10 = Food(name='Donuts', description='American dessert', price=5.99, image_url='image12.jpg')

    db.session.add_all([food1, food2, food3, food4, food5, food6, food7, food8, food9, food10])
    
    db.session.commit()
    return 'Seeded'
```

If we want to run this "seeder" function from the console, enter `flask shell`, and therein run the following snippet:

```python
from app import app, db, Food, User, seed
seed()
```


## SQLAlchemy queries

Now we can fiddle around a little bit with the database data.
We can create instances of these model classes just as we would with any normal class as we have the constructor set up with the `__init__`.
Adding an in-memory object to the database is also trivial, similarly to git, we need to use the add and commit functions (of the session object in this case).

Below we add a new food element:

```python
newfood = Food(name="Goulash",description="Hungarian soup thingie with meat, potatoes, carrots and paprika",price="11.99",image_url="goulash.gif")
db.session.add(newfood)
db.session.commit()
```

These objects than can be freely modified too just by modifying the object in python. If we commit it once again, all the changes would be added to the database as well.

```python
newfood.image_url='goulash.jpg'
db.session.commit()
```

Getting a single item by it's id:

```python
Food.query.get(1)
```

Getting all the items:
```
Food.query.all()
```