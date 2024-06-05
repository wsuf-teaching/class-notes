from flask import Flask, jsonify, abort, request, make_response
from foods import foods

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello world!</h1><input type='text'>abc"

@app.route("/about")
def about():
    return "This is the about page"

@app.route("/login")
def login():
    return "Log in here!"

@app.route("/api")
def api():
    return {'hello':'world'}

@app.route("/api2")
def api2():
    mylist = [1,2,3,4,5]
    return jsonify(mylist)

@app.route("/foods")
def foodsroute():
    return jsonify(foods)

@app.route('/foods/<int:id>')
def get_food(id):
    for food in foods:
        if food['id'] == id:
            return jsonify(food)
    return abort(404, "Food not found")

def returnname(name):
    return '<h1>Hello {}!</h1>'.format(name)

@app.route('/<name>')
def name(name):
    return returnname(name)

@app.route('/echo/<string:name>/<int:age>')
def nameecho(name, age):
    age = age + 1
    name = name.upper()
    return '<h1>Hello {}! You are almost {} years old.</h1>'.format(name,age)

# @app.route('/echo/<string:surname>/<string:lastname>')
# def nameecho2(surname, lastname):
#     return '{} {}'.format(surname, lastname)

@app.route('/echo2/<name>', methods=['POST','GET'])
@app.route('/echo2/', methods=['POST','GET'], defaults={'name':'John'})
def echo2(name):
    return 'Hello {}!'.format(name)

@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    age = request.args.get('age')
    return '<h1>Hi {}. You are from {}. Your age is {}. You are on the query page.'.format(name, location, age)

@app.route('/requestform', methods=['POST'])
def requestform():
    name = request.form['name']
    location = request.form['location']
    return 'Hello {}. You are from {}. You have submitted the form successfully!'.format(name, location)

@app.route('/submitformpage')
def submitformpage():
    return '''
        <form action="/requestform" method="POST">
            <input id="name" name="name" type="text"/>
            <input id="location" name="location" type="text"/>
            <button>Submit</button>
        </form>'''

@app.route('/addfood', methods=['PUT'])
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

@app.route('/setcookie')
def setcookie():
    response = make_response('Cookie ha sbeen set!')
    response.set_cookie('mycookie','mycookievalue12345')
    return response

@app.route('/getcookie')
def getcookie():
    cookie = request.cookies.get('mycookie')
    cookies = request.cookies
    print(cookies)
    if cookie:
        return f"The value of mycookie is {cookie}"
    else:
        return "Mycookie not found"

if __name__ == '__main__':
    app.run(debug=True, port=80)