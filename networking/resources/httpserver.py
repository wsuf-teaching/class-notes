from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth

app = Flask(__name__)



app.config['BASIC_AUTH_USERNAME'] = 'username'
app.config['BASIC_AUTH_PASSWORD'] = 'password'


basic_auth = BasicAuth(app)


foods = [
    {"id": 1, "name": "Pizza", "price": 10.99, "description": "Delicious pizza with various toppings"},
    {"id": 2, "name": "Burger", "price": 8.99, "description": "Classic beef burger with cheese and lettuce"},
    {"id": 3, "name": "Sushi", "price": 15.99, "description": "Assorted sushi rolls with fresh fish"}
]

# helper function
def get_food_by_id(food_id):
    for food in foods:
        if food["id"] == food_id:
            return food
    return None

# GET route to get all foods
@app.route('/foods', methods=['GET'])
def get_foods():
    return jsonify(foods)

# GET Route to get a specific food by ID
@app.route('/foods/<int:food_id>', methods=['GET'])
def get_food(food_id):
    food = get_food_by_id(food_id)
    if food is None:
        abort(404)
    return jsonify(food)

# GET route to get food by ID using query parameters
@app.route('/foods/query', methods=['GET'])
def get_food_by_query():
    food_id = request.args.get('id')
    if food_id is None:
        abort(400)
    food = get_food_by_id(int(food_id))
    if food is None:
        abort(404)

    return jsonify(food)

# GET route to get food by ID using JSON body
@app.route('/foods/json', methods=['POST'])
def get_food_by_json():
    if not request.json:
        abort(400)

    food_id = request.json.get('id')
    if food_id is None:
        abort(400)
    food = get_food_by_id(int(food_id))
    if food is None:
        abort(404)

    return jsonify(food)



# POST route to add a new food
@app.route('/foods', methods=['POST'])
def create_food():
    if not request.json or not 'name' in request.json or not 'price' in request.json:
        abort(400)
    food = {
        'id': foods[-1]['id'] + 1 if len(foods) > 0 else 1,
        'name': request.json['name'],
        'price': request.json.get('price', ""),
        'description': request.json.get('description', "")
    }
    foods.append(food)
    return jsonify(food), 201

# PUT route to create or update a food by ID
@app.route('/foods/<int:food_id>', methods=['PUT'])
def update_or_create_food(food_id):
    existing_food = get_food_by_id(food_id)
    if existing_food:
        if not request.json:
            abort(400)
        if 'name' in request.json:
            existing_food['name'] = request.json['name']
        if 'price' in request.json:
            existing_food['price'] = request.json['price']
        if 'description' in request.json:
            existing_food['description'] = request.json['description']
        return jsonify(existing_food), 200
    else:
        if not request.json or not 'name' in request.json or not 'price' in request.json:
            abort(400)
        new_food = {
            'id': food_id,
            'name': request.json['name'],
            'price': request.json['price'],
            'description': request.json.get('description', "")
        }
        foods.append(new_food)
        return jsonify(new_food), 201


# DELETE route to delete a food by ID
@app.route('/foods/<int:food_id>', methods=['DELETE'])
def delete_food(food_id):
    food = get_food_by_id(food_id)
    if food is None:
        abort(404)
    foods.remove(food)
    return jsonify({'result': True})



# error example
@app.route('/error_example', methods=['GET'])
def error_example():
    return 3/0


# any status code
@app.route('/status_codes_example', methods=['GET'])
def status_code_example():
    return "blah", 201


# Protected endpoint requiring basic authentication
@app.route('/protected')
@basic_auth.required
def protected():
    return 'You are authenticated!'

















# Simple GET request
@app.route('/get_example', methods=['GET'])
def get_example():
    return jsonify(message='This is a GET request example')




# Example using URL parameters
@app.route('/url_params/<name>/<age>', methods=['GET'])
def url_params_example(name, age):
    return f'Hello, {name}! You are {age} years old.'

# Example using query parameters
@app.route('/query_params', methods=['GET'])
def query_params_example():
    name = request.args.get('name')
    age = request.args.get('age')
    return f'Hello, {name}! You are {age} years old.'

# Example using JSON body
@app.route('/json_body', methods=['POST'])
def json_body_example():
    data = request.json
    name = data.get('name')
    age = data.get('age')
    return jsonify({'message': f'Hello, {name}! You are {age} years old.'})






# POST request with request body
@app.route('/post_example', methods=['POST'])
def post_example():
    data = request.json
    return jsonify(message='This is a POST request example', data=data)


# PUT request to update a resource
@app.route('/put_example/<resource_id>', methods=['PUT'])
def put_example(resource_id):
    data = request.json
    return jsonify(message=f'This is a PUT request example for resource {resource_id}', data=data)


# DELETE request to delete a resource
@app.route('/delete_example/<resource_id>', methods=['DELETE'])
def delete_example(resource_id):
    return jsonify(message=f'This is a DELETE request example for resource {resource_id}')








if __name__ == '__main__':
    app.run(debug=True)