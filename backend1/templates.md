# Flask and Jinja2 template engine

If we are not doing something like React where we only fetch data from API endpoints, an other way to display data rather than just returning html blocks is using a so-called template engine.
Jinja is such a tool, and is coming bundled with Flask, but we need to import it from there:

```python
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

if __name__ == '__main__':
    app.run()
```
## Templates

In it's most simple form, it looks like the snippet below. We tell it to render a specific html file.

> All the `.html` files can be found in the `templates/` folder.

Create an `index.html` file at `templates/index.html`:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>My title</title>
    </head>
    <body>
        <h1 class='myclass'>Helloo world!</h1>
        <p>Hello hello</p>
        <div>
            <ul>
                <li>List item 1</li>
                <li>List item 2</li>
            </ul>
        </div>
    </body>
</html>
```

And add a route to the flask application.

```python
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
```

Templates can also take template parametres:

```python
@app.route('/templateparams')
def templateparams():
    return render_template('templateparams.html', name='John Doe', age=20)
```

Parametres, which we can use in the template file like this:

```html
    <h1>Hello {{name}}</h1>
    <p>Your age is {{age}}</p>
```

A few other types, and conditionals:

```python
@app.route('/options')
def options():
    name = "John Doe"
    isWelcome = True
    age = 66
    return render_template('options.html', name=name, isWelcome=isWelcome, age=age)
```

And in the template:

```html
{% if isWelcome %}
<h1>Hello {{name}}</h1>
{% else %}
<h1>Bye {{name}}</h1>
{% endif %}

{% if age > 18 %}
<p>You are an adult</p>
{% endif %}
```

In this project as well, we have an array, called `foods` defined in `foods.py`, that we have to import to use first.

```python
from foods import foods
```

Pass it to the template engine.

```python
@app.route('/foods', methods=['GET'])
def foods():
    return render_template('foods.html', foods=foods)
```

And in the template file, we can loop through it with for (or while), getting the properties of the individual objects with the dot notation.

```html
{% for food in foods %}
<li>
    <h1>{{food.name}}</h1>
    <p>
        {{food.description}}
    </p>
    <p>
        {{food.price}}
    </p>
</li>
{% endfor %}
```

## Template hierarchies

Templates can also extend each other. 
A "parent" template defines blocks (which can have default content) but which are otherwise filled by child templates extending the parent.
Create a base template that we can extend upon:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>{% block title %}{% endblock %}</title>
    </head>
    <body>
        <h1>Base Template</h1>
        <nav>
            <a href="#">Home</a>
            <a href="#">Foods</a>
            <a href="#">Options</a>
        </nav>
        {% block content %}
            <h2>This is in the base template!</h2>
        {% endblock %}
    </body>
</html>
```

Now we only need to leaave the body content in foods, index and options.html.
In those files, we should define that the current template extends the base, as well as define the title and content blocks.
The snippet belows shows how the foods file should look like after.

```html
{% extends 'base.html' %}

{% block title %}Foods{% endblock %}

{% block content %}
<h1>Food List</h1>
<ul>
    {% for food in foods %}
    <li>
        <h1>{{food.name}}</h1>
        <p>
            {{food.description}}
        </p>
        <p>
            {{food.price}}
        </p>
    </li>
    {% endfor %}
</ul>
{% endblock %}
```

If we don't supply one of these blocks, we can specify default blocks in the base template like we did above, and they will be automatically used instead.
We can also manually invoke them on demand by calling `super()` in the html template's respective block.

```html
{{ super() }}
```

## Static files, links

Let's also add an image to foods just below the ul, but still inside the content block. The image is also included in the project in the static/images folder. Below you can see how we can import it using the `url_for` function.

```html
<img src="{{url_for('static', filename='images/pizza.png')}}" alt="food">
```

Links are done similarly with `url_for`. As of now, regular links would work as well, however with `url_for` we are referring to function names that are serving the actual routes, so through `url_for`, 
we don't have to fix all the links when one of the route's name changes for example. We can use `url_for` programatically from the python files as well.

```html
<a href="{{url_for('index')}}">Home</a>
<a href="{{url_for('get_foods')}}">Foods</a>
<a href="{{url_for('options')}}">Options</a>
```

## Forms

To see forms through an example, we need to import a few more functions from Flask as below.

```python
from flask import Flask, jsonify, request, render_template, redirect, url_for
```

In this example, the `/theform` route listens to both GET and POST request. In case of a GET request, it displays the form defined in the `form.html`. If we submit that form, it POSTs to the same route, triggering the POSt logic defined conditionally in the function.

```python
@app.route('/theform', methods=['GET','POST'])
def theform():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        name = request.form['name']
        location = request.form['location']
        return 'Hello {}. You are from {}. You have submitted the form successfully!'.format(name, location)
        #return redirect(url_for('index'))
```

The accompanying form.html looks as follow:

```html
{% extends 'base.html' %}

{% block title %}Form{% endblock %}

{% block content %}
    <h1>Please fill out the form</h1>
    <form action="/theform" method="POST">
        <input type="text" name="name">
        <input type="text" name="location">
        <input type="submit" value="Submit">
    </form>
{% endblock %}
```