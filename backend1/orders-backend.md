## Migrations

Remember the initial migration that we have created. Now modify one of the tables we have, add for example a new column to the food table, and of course also update the functions accordingly:


private fields:
```python
    in_stock = db.Column(db.Boolean, default=True, nullable=True)
```
\_\_init\_\_():
```python
    def __init__(self, name, description, price, image_url, in_stock=True):
            # ...
            self.in_stock = in_stock
```
json():
```python
            'in_stock': self.in_stock
```

If we run `flask db migrate` now, we will see that flask detected the new column added nd generated a new migration based on it.
We can execute this migration with `flask db upgrade`. Why migrations are useful, is that we don't have to manually change the SQL structure with the alter table commands, as well as giving us a very easy and straightforward way to
apply or rollback database schema changes. Just as we can apply the modification with `upgrade`, we can remove them with `downgrade`.

```sh
flask db migrate
flask db upgrade
```

## Orders

As last part of this exercise, we are creating more data structures and tables. Orders (`order.py`), which links a user to an actual order having its own id. Notice the `foreignKey` relations in SQLAlchemy syntax:

```python
from flask_sqlalchemy import SQLAlchemy
from db import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    order_foods = db.relationship('OrderFood', backref='order', lazy=True)

    def __init__(self, user_id):
        self.user_id = user_id

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, order_id):
        return cls.query.get(order_id)

    @classmethod
    def get_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()   

    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'order_foods': [order_food.json() for order_food in self.order_foods]
        }

    def __repr__(self):
        return f"Order('Order#{self.id} belonging to User#{self.user_id}')"
```

And OrderFoods (`orderfood.py`), which link an Order (by its id) to food items it contains.

```python
from flask_sqlalchemy import SQLAlchemy
from db import db

class OrderFood(db.Model):
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True)
    food_id = db.Column(db.Integer, db.ForeignKey('food.id'), primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    food = db.relationship('Food', backref='order_foods')

    def __init__(self, order_id, food_id, amount):
        self.order_id = order_id
        self.food_id = food_id
        self.amount = amount

    def json(self):
        return {
            'order_id': self.order_id,
            'food_id': self.food_id,
            'amount': self.amount,
            'food': self.food.json()
        }
    
    def __repr__(self):
        return f"OrderFood('{self.order_id}', '{self.food_id}', '{self.amount}')"
```


These are many-to-many relationships. A user can can have zero or more orders, and an order can have zero or more order items (foods).
        
The user file should also be modified with a field representing the relationship.

```python
    orders = db.relationship('Order', backref='user', lazy=True)
```

We can make a test route to list out all orders in the system in `app.py`:

```python
from models.order import Order
from models.orderfood import OrderFood

# ...

@app.route('/orders')
def get_orders():
    orders = Order.get_all()
    return jsonify([order.json() for order in orders])
```

Let's also add some test data through `flask shell`:

```python
from app import app, db, Food, Order, OrderFood, User
user1 = User.query.get(1)
user2 = User.query.get(2)
order1 = Order(user_id=user1.id)
order2 = Order(user_id=user2.id)
food1 = Food.query.get(1)
food2 = Food.query.get(2)
food3 = Food.query.get(3)
food4 = Food.query.get(4)
food5 = Food.query.get(5)
db.session.add_all([order1, order2])
db.session.commit()

order_food1 = OrderFood(order_id=order1.id, food_id=food1.id, amount=2)
order_food2 = OrderFood(order_id=order1.id, food_id=food2.id, amount=3)
order_food3 = OrderFood(order_id=order2.id, food_id=food3.id, amount=1)
order_food4 = OrderFood(order_id=order2.id, food_id=food4.id, amount=2)
order_food5 = OrderFood(order_id=order2.id, food_id=food5.id, amount=2)
db.session.add_all([order_food1, order_food2, order_food3, order_food4, order_food5])
db.session.commit()
```

Let's also make another endpoint that retrieves the currently logged in user's orders in the system:

```python
@app.route('/myorders')
@flask_praetorian.auth_required
def get_my_orders():
    userid = flask_praetorian.current_user_id()
    orders = Order.get_by_user_id(userid)
    return jsonify([order.json() for order in orders])
```

We also need to have an `Address` (`address.py`) object and model to implement everything we planned.

```python
from db import db

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    zip = db.Column(db.String(20), nullable=False)
    orders = db.relationship('Order', backref='address', lazy=True)

    def json(self):
        return {
            'id': self.id,
            'street': self.street,
            'city': self.city,
            'zip': self.zip
        }
```

And then change `order.py` as such to add the connection between them:

```python
from flask_sqlalchemy import SQLAlchemy
from db import db
from models.address import Address

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    order_foods = db.relationship('OrderFood', backref='order', lazy=True)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id', name='fk_order_address'), nullable=True)

    def __init__(self, user_id, address_id):
        self.user_id = user_id
        self.address_id = address_id

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, order_id):
        return cls.query.get(order_id)
    
    @classmethod
    def get_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()   

    def json(self):
        address = Address.query.get(self.address_id)
        return {
            'id': self.id,
            'user_id': self.user_id,
            'address': address.json() if address else None,
            'order_foods': [order_food.json() for order_food in self.order_foods]
        }

    def __repr__(self):
        return f"Order('Order#{self.id} belonging to User#{self.user_id}')"
```

> Address should not be nullable, but to make our lives easier by not having to edit data already in the DB, we opt to leave it nullable.

Migrate again cause we edited the orders table:

```sh
flask db migrate
flask db upgrade
```

Finally, we make the endpoint that can receive a new order and stores it nicely.

> Be sure to have all the correct impots in `app.py`:
> ```python
> from models.food import Food
> from models.user import User
> from models.order import Order
> from models.orderfood import OrderFood
> from models.address import Address
> ```

The route:

```python
@app.route('/order', methods=['POST'])
@flask_praetorian.auth_required
def new_order():
    req = request.get_json(force=True)

    street = req.get('street')
    city = req.get('city')
    zip_code = req.get('zip')

    items = req.get('items', [])
    if not items:
        return jsonify({"error": "No items in order"}), 400
    
    food_ids = [item['id'] for item in items]
    existing_foods = Food.query.filter(Food.id.in_(food_ids)).all()
    existing_food_ids = {food.id for food in existing_foods}

    for item in items:
        if item['id'] not in existing_food_ids:
            return jsonify({"error": f"Food id {item['id']} does not exist"}), 400

    new_address = Address(street=street, city=city, zip=zip_code)
    db.session.add(new_address)
    db.session.commit() 

    user = flask_praetorian.current_user()
    new_order = Order(user_id=user.id, address_id=new_address.id)  
    db.session.add(new_order)
    db.session.commit()

    for item in items:
        order_food = OrderFood(order_id=new_order.id, food_id=item['id'], amount=item['amount'])
        db.session.add(order_food)

    db.session.commit()
    
    return jsonify({"message": "Order created successfully"}), 201
```