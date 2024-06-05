### Introduction to Flask

Flask is a lightweight web framework for Python, designed to make it easy to get a web application up and running with minimal overhead. It provides the essential tools needed to build web applications and APIs, making it an excellent choice for simpler projects or as a starting point for more complex ones. Flask emphasizes simplicity and flexibility, allowing developers to choose their tools and libraries as needed.

### Improved Code Descriptions

#### Backend v1

In simpler web applications or APIs, most of the user-facing parts revolve around defining routes and the functions that handle those routes. The default return value for a route, when accessed by a browser, is interpreted as HTML.

#### Setting Things Up

First, let's set up a basic Flask application. Here is a simple example:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```

To run this application, save it in a file (e.g., `app.py`) and execute it with the command `python app.py`. To enable automatic reloading of the server when code changes, add the `debug=True` parameter to the `app.run()` function:

```python
app.run(debug=True)
```

#### Basic Routes

Routes in Flask are defined using the `@app.route` decorator. Here is an example of a basic route that returns a plain text message:

```python
@app.route('/')
def index():
    return 'Hello, World!'
```

To return JSON data, you can either return a dictionary directly or use Flask's `jsonify` function. Note that `jsonify` needs to be imported from Flask.

```python
from flask import jsonify

@app.route('/api')
def api():
    return {
        'hello': 'world'
    }

@app.route('/jsonify')
def json():
    mylist = [1, 2, 3, 4, 5]
    return jsonify(mylist)
```

You can also return HTML directly from a route:

```python
@app.route('/html')
def html():
    return '<h1>Hello, World!</h1>'
```


Routes can take parameters, however this will only work with names not already defined above as routes, and will "eat" requests to other named routes defined below it.

```python
@app.route('/<name>')
def name(name):
    return '<h1>Hello {}!</h1>'.format(name)

@app.route('/echo/<name>')
def nameecho(name):
    return '<h1>Hello {}!</h1>'.format(name)
```

The type for the URL parametres can be defined as well.

```python
@app.route('/echo/<string:name>')
def nameecho(name):
    return '<h1>Hello {}!</h1>'.format(name)
```

And we can have multiple parameters too.

```python
@app.route('/echo/<string:name>/<int:age>')
def nameecho(name):
    return '<h1>Hello {}! You are {} years old.</h1>'.format(name,age)
```

Of course, aside from echoing it back, we can do anything, run any logic on the data that we have. Here we convert the name to UPPER CASE, and add one to the age.

```python
@app.route('/echo/<string:name>/<int:age>')
def nameecho(name, age):
    age = age + 1
    name = name.upper()
    return '<h1>Hello {}! You are almost {} years old.</h1>'.format(name,age)
```

Let's also see an example of an endpoint that the food order app would use. In the folder, we have a file called foods.py, that simply defined a list of foods with properties like id, name, description and so.

```python
from foods import foods

@app.route('/foods')
def get_foods():
    return jsonify(foods)
```

We can also retrieve a single food by its id. If it is not found, we return an error in a JSONified form.

```python
@app.route('/foods/<int:id>')
def get_food(id):
    for food in foods:
        if food['id'] == id:
            return jsonify(food)
    return jsonify({'error': 'Food not found'})
```

## POST requests

Everything we have seen so far was a GET request, let's see a few examples of POSTs. In the route decorator of a function, we have to declare what type of method it should listen to.

```python
@app.route('/echo2/<name>', methods=['POST'])
def process(name):
    return 'Hello {}!'.format(name)
```

The same route can also serve multiple request types as well. We can either define it with the same name below with the GET method, or add GET to the methods array.

```python
@app.route('/echo2/<name>', methods=['POST, GET'])
def echo2(name):
    return 'Hello {}!'.format(name)
```

Routes cantake default values, automatically injected by flask if none is given to the request.

```python
@app.route('/echo2/', methods=['POST','GET'], defaults={'name':'John'})
@app.route('/echo2/<name>', methods=['POST', 'GET'])
def process(name):
    return 'Hello {}!'.format(name)
```

## Passing more data

Query parametres can be used the way defined below. However we need the request import from flask for them to work. Here we are listening to two parameters, name and location. In the URL they are in the following format: `http://baseurl/query?name=XXX&location=YYY`.

```python
# add requests to the import ad the top
from flask import Flask, jsonify, request

@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    age = request.args.get('age')
    return '<h1>Hi {}. You are from {}. Your age is {}. You are on the query page.'.format(name, location, age)
```

Another option to pass data to the server is using a request with form parametres.
If we don't have a form at hand, we can send the request from Postman by setting the key-value pairs up at it's body > formdata section.

```python
@app.route('/requestform', methods=['POST'])
def requestform():
    name = request.form['name']
    location = request.form['location']
    return 'Hello {}. You are from {}. You have submitted the form successfully!'.format(name, location)
```

With this tiny route we can display a small html page capable of submitting a form that the route above can listen to.

```python
@app.route('/submitformpage')
def submitformpage():
    return '''
        <form action="/requestform" method="POST">
            <input id="name" name="name" type="text"/>
            <input id="location" name="location" type="text"/>
            <button>Submit</button>
        </form>'''
```

For more complex data structures, json body can be used.
In postman, set the them under body > raw > json.

```json
{
    "name":"Ice cream",
    "price":"19",
    "description":"A cold, sweet dessert made with milk, cream, and various flavorings."
}
```

And the route receiving them. The snippet below shows an example of an endpoint receiving json data, and adding the received data to the foods array.

```python
@app.route('/addfood', methods=['POST'])
def add_food():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')
    food = {
        'id': len(foods) + 1,
        'name': name,
        'price': price,
        'description': description
    }
    foods.append(food)
    return jsonify(foods)
```

## Cookies

Last, let's see some operations regarding writing and reading cookies.
On the getcookie route, (well, always) the cookies relevant to the page are automatically sent to the server with the requests where we can check them out through the `request.cookies` object.

Creating a cookie:

```python
# add make_response to the import ad the top
from flask import Flask, jsonify, abort, request, make_response

@app.route('/setcookie')
def setcookie():
    response = make_response('Cookie has been set!')
    response.set_cookie('mycookie', 'cookievalue')
    return response
```

Reading a cookie:

```python
@app.route('/getcookie')
def getcookie():
    cookie = request.cookies.get('mycookie')
    
    if cookie:
        return f'The value of mycookie is: {cookie}'
    else:
        return 'mycookie not found'
```
