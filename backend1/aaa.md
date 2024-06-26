# AAA

AAA stands for Authentication, Authorization, and Accounting. These are three essential components for managing and securing user access to resources in a system.

- **Authentication**: The process of verifying the identity of a user. This step ensures that the user is who they claim to be, typically through credentials like usernames and passwords, biometric data, or other verification methods.

- **Authorization**: Once authenticated, authorization determines what an authenticated user is allowed to do. This involves checking permissions and roles to grant or deny access to resources or actions within the system.

- **Accounting**: This involves tracking and recording user actions and resource usage. Accounting helps in auditing and monitoring user activities for security, compliance, and resource management purposes.

# JWT tokens

JWT (JSON Web Token) is a popular method for implementing authentication and authorization in modern web applications. JWTs are compact, URL-safe tokens that represent claims between two parties. They are commonly used to secure APIs and manage user sessions in a stateless manner.

A JWT consists of three parts: the header, the payload, and the signature. The header specifies the token type and signing algorithm. 

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

The payload contains the claims, which are statements about an entity (typically, the user) and additional data. 

```json
{
  "sub": "1234567890",
  "name": "John Doe",
  "admin": true
}
```

The signature is used to verify the token's integrity and authenticity, ensuring that the token has not been tampered with.

```json
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret
)
```

The resulting JWT looks like this:

```json
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ
```

![jwt](https://i.imgur.com/rzIbyve.png)

# In practice

## Setting up the user model

Next to `food.py`, create `user.py` which will be the user model in the databse using SQLAlchemy and also be used by the JWT token to supply identity.

```python
from db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    roles = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True, server_default='true')

    @classmethod
    def lookup(cls, username):
        return cls.query.filter_by(username=username).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)

    @property
    def identity(self):
        return self.id

    def is_valid(self):
        return self.is_active
    
    @property
    def rolenames(self):
        try:
            return self.roles.split(',')
        except Exception:
            return []
    
    def get_custom_claims(self):
        return {
            'name': self.username
        }
```

It includes several fields: `id`, which is the primary key and a unique identifier for each user; `username`, which is a unique text field; `password`, which stores the user's password; `roles`, a text field containing a comma-separated list of user roles; and `is_active`, a boolean field indicating whether the user is active, with a default value of `True`. 

The model also includes several methods. The `lookup` class method searches for a user by their username, returning a single user or `None` if no match is found. The `identify` class method retrieves a user by their ID. The `identity` property returns the user's ID. The `is_valid` method checks if the user is active by returning the value of `is_active`. The `rolenames` property splits the `roles` string into a list, handling any exceptions by returning an empty list. Finally, the `get_custom_claims` method returns a dictionary with custom claims for the JWT payload, including the user's username.

> Role names probably would ideally be stored in a separate database table, and user-role mappings would be in a third one, but we opted to put it inside the user model to make our lives a little easier coding-wise.

## Configuration setup for JWT and flask_praetorian

In this example we are using a library called `flask_praetorian` to handle AAA and JWT tokens for us. Install it first.

```sh
pip install flask_praetorian
```

For setting up the configuration, several key settings are defined. 
The `SECRET_KEY` is set to `"blahblahblah"`, which is used to sign the JWT tokens and ensure their integrity and authenticity. 

> Once again, secret keys should NEVER be put into the code going to version control systems. We will see a better way to store these later.

The `JWT_ACCESS_LIFESPAN` is set to 24 hours, meaning that access tokens will expire after a day. The `JWT_REFRESH_LIFESPAN` is set to 30 days, meaning that refresh tokens will expire after a month. An instance of `flask_praetorian.Praetorian`, named `guard`, is created to handle authentication and JWT operations. The `guard` is then initialized with the Flask app and the `User` model using `guard.init_app(app, User)`, which sets up Praetorian to manage user authentication and JWT encoding/decoding based on the `User` model.

Put the imports to the top of `app.py`:

```python
from models.user import User

import flask_praetorian
```

The config statements inside the `create_app()` method:

```python
    app.config['SECRET_KEY']="blahblahblah"
    app.config['JWT_ACCESS_LIFESPAN'] = {'hours': 24}
    app.config['JWT_REFRESH_LIFESPAN'] = {'days': 30}
    global guard
    guard = flask_praetorian.Praetorian()
    guard.init_app(app, User)
```

To add some "default" users, we can use the flask shell again:

```sh
flask shell
```

Then type the following:

```python
from app import app, db, User

user = User(username="admin@example.com",password=guard.hash_password("12345"),roles="admin")
db.session.add(user)
db.session.commit()
```

## Login route

Next, back in the code we are gonna start with the login route. It is defined to handle user login at the `/login` endpoint using the POST method. Inside the route, the JSON data from the POST request is retrieved using `request.get_json()`. The `username` and `password` are extracted from this JSON data. The `guard.authenticate(username, password)` method is used to authenticate the user with the provided credentials. If the authentication is successful, the `guard.encode_jwt_token(user)` method is used to encode a JWT token for the authenticated user. This token is then included in a JSON response under the key `"access_token"`. The response is returned with a status code of 200, indicating a successful login. This token can be used by the client to authenticate subsequent requests by including it in the request headers.

```python
@app.route('/login', methods=['POST'])
def login():
    req = request.get_json()
    username = req.get('username')
    password = req.get('password')
    user = guard.authenticate(username, password)
    jwt_token = {"access_token":guard.encode_jwt_token(user)}
    return jwt_token, 200
```

## Registration route

This route allows new users to create an account in the application. When a POST request is made to the `/register` endpoint, the route handler starts by retrieving the JSON data from the request using `request.get_json(force=True)`. This ensures that the request is parsed as JSON even if the `Content-Type` header is not set. The `username` and `password` are then extracted from this JSON data. If either the `username` or `password` is missing, the route returns a 400 status code with a message indicating that both fields are required.

Next, the `lookup` method of the `User` model is used to check if a user with the provided `username` already exists. If an existing user is found, the route returns a 400 status code with a message stating that the user already exists. If no existing user is found, a new `User` object is created with the provided `username`, the hashed `password` (using `guard.hash_password(password)`), and an empty `roles` string.

The new user is then added to the database session with `db.session.add(user)` and committed to the database using `db.session.commit()`. Finally, the route returns a 201 status code with a message indicating that the user was registered successfully.

```python
@app.route('/register', methods=['POST'])
def register():
    req = request.get_json(force=True)
    username = req.get('username', None)
    password = req.get('password', None)
    roles = ''
    if not username or not password:
        return {'message': 'Username and password are required'}, 400
    existing_user = User.lookup(username)
    if existing_user:
        return {'message': 'User already exists'}, 400
    
    user = User(username=username, password=guard.hash_password(password),roles=roles)
    db.session.add(user)
    db.session.commit()
    return {'message': 'User registered successfully'}, 201
```

## Login protected route

The protected route is a secured endpoint that requires the user to be authenticated. The `@flask_praetorian.auth_required` decorator ensures that only authenticated users can access this route. When an authenticated user makes a GET request to the `/protected` endpoint, the route returns a message indicating that the endpoint is protected and includes the username of the authenticated user. The `flask_praetorian.current_user()` function is used to get the current authenticated user, and their username is included in the response message.

```python
@app.route('/protected', methods=['GET'])
@flask_praetorian.auth_required
def protected():
    # "Authorization: Bearer <your_token>"
    return {'message': f'protected endpoint (allowed user {flask_praetorian.current_user().username})'}
```

## Admin only route

Finally, this is another secured endpoint, but it requires the user to have a specific role. The `@flask_praetorian.roles_required("admin")` decorator ensures that only users with the "admin" role can access this route. When a user with the appropriate role makes a GET request to the `/adminonly` endpoint, the route returns a message indicating that the endpoint is protected and includes the username of the current user. As with the protected route, the `flask_praetorian.current_user()` function is used to get the current user, and their username is included in the response message.

```python
@app.route('/adminonly', methods=['GET'])
@flask_praetorian.roles_required("admin")
def protected_admin_required():
    return jsonify(
        message="protected_admin_required endpoint (current user is: {})".format(
            flask_praetorian.current_user().username,
        )
    )
```