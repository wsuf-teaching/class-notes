Python is a general-purpose, interpreted and easily portable language.
Can be used for many things, ranging from small automation scripts, to data analysis, machine learning, and web applications.
The syntax is very easy, dynamically and strongly typed. Supports multithreading, OOP and multiple inheritance.
It also uses garbage collector for memory management.

A big goal of the language is readability. It may be strange at first, but instead of brackets and semicolons,
it uses indentation and newline ("\n") characters for separating commands.

```python
def isEven(num):
    if num % 2 == 0:
        return True
    return False
print(isEven(3))
print(isEven(4))
```

Comments are done with the `#` character:

```python
a = 1
# b = 2
c = 3
```

While we can use an empty block in other languages, it is not applicable in Python due to how it handles block definition with
indentations. In python, we can use the `pass` keyword instead.
```java
if(condition) {
    // something
}
else {
    // something else
}
```

```python
if condition:
    pass
else
    pass
```

## Types, values and variables

Python is dynamically typed, so when we create a variable, we don't have to specify its type. It gets automatically assigned while running. However, after assigning a variable, types matter, so we cannot add 2 and "3" together.

To convert between types, we can use the `int()`, `float()`, `str()`, `list()`, `bool()` etc. functions.

We can assign multiple variables at the same time:

```python
a = b = 1
a, b = 1, 2
```

A variable have a local scope, like in a function, or in a statement block (for, if, else, etc.). By default, if we redifine a variable with a same time, it "shadows" the outer variable. If we want to use a global variable, we can use the global keyword in front of it in a function:

```python
a = 1

def myFunction():
    global a
    a = 2
```

There are four numerical types in Python. Integer, long, float and complex.

As you have seen, we can define functions with the `def` keyword.

> Variables can also be "deleted" with the `del` keyword.
> ```python
> del a
> ```

## Collections and strings

The most used collection types are list, tuple, dictionary and set.

A list is an ordered collection of elements that can be modified (mutable). Elements in a list are enclosed in square brackets [] and separated by commas.

A tuple is an ordered collection of elements that cannot be modified (immutable). Elements in a tuple are enclosed in parentheses () and separated by commas.

A dictionary is an unordered collection of key-value pairs. Each key-value pair is separated by a colon : and enclosed in curly braces {}.

A set is an unordered collection of unique elements. Elements in a set are enclosed in curly braces {} or can be created using the set() constructor.

```python
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_dict = {'name': 'John', 'age': 25, 'city': 'London'}
my_set = {1, 2, 3, 4, 5}
```

We can add one or more elements to the list with `append` and `extend` respectively.
Since tuples are immutable, we cannot directly add elements to an existing one. Instead, we should concatenate them and create a new one.
To add or modify a value in a dict, we can simply "index" them.
Lastly, to add one or more elements to the set, the `add` and `update` methods are used.

```python
my_list.append(4)
my_list.extend([5,6,7])

my_tuple = my_tuple + (6, 7)

my_dict['city'] = 'New York'
my_dict['surname'] = 'Doe'

my_set.add(6)
my_set.update([7,8,9])
```

We can index parts of a lists or strings (as they are lists of characters) using brackets `[]`. We can access a single element, or a list of elements at once, and we can also define a step size so as to retrieve every <i>n</i>th element.
The full syntax is `list[start:end:step]`, but there are also a few other things that we can do with it:


```python
# retrieve a single element
print( my_list[0] )
# retrieve the second to third element
print( my_list[1:3] )
# retrieve every second element
print( my_list[::2] )
# retrieve everything after the first two elements
print( my_list[:2] )
# retrieve the last element
print( my_list[:-1] )
# retrieve the last two elements
print( my_list[-2:])
```

Dictionary elements can be retrieved just as they were added or assigned.
We can also retrieve the list of keys or values as lists.

```python
print( my_dict['name'] )
print( my_dict.keys() )
print( my_dict.values() )
print( len(my_dict) )
```

The length of a string or collection can be retrieved with the `len` function.

## Boolean

`True` and `False` as we know, but in python, they are case sensitive!
Logical operands are `and`, `or` and `not`. Logical types can be explicitly evaluated with the `bool` function.
Python also works with implicit evaluation. Empty strings, `0` and empty lists, maps, sets are evaluated as False.

```python
# True
print( bool(7) )
# False
print( bool(0) )
# True
print( bool("string") )
# False
print( bool("") )
```


## Conditionals, operators


Most of the operators work the same as in other languages, but there is no increment or decrement operator (`++` or `--`), but there are operators
for power and integer division (`**` and `//`). Bitwise operators are the same as
we know from JavaScript (`&`, `|`, `^`, `~`, `<<`, `>>`).


All the comparators are the same as anywhere else: `<`, `>`, `==`, `!=`, `<=`, `>=`

`if` and `else` works just like how you would expect it:

```python
if condition:
    # do something
elif other_condition:
    # do something else    
else:
    # do something else too
```

> Switch-case is not present in Python, so we have to manually implement it using if-elif-else blocks.

Two more useful operators are `is` and `in`.
While `==` compares value equality, `is` compares reference equality. So it also looks whether the two variables are referencing the same object. `is` is also used for comparing with `None` values.

```Python
a is None
```

`in` is used to check containment. Whether a string or collection contains a character or an item.

```python
"i" in "string"
3 in [1, 2, 3]
```

## <a href="https://i.kym-cdn.com/photos/images/newsfeed/001/393/656/da7.jpg">Lööps</a>

`while` works just as everywhere else:

```python
i = 0
while i < 10:
    i+=1
    print("Hello world", i)
```

`for` loops are a little bit different. A `for` loops goes through an iterable object, and is not based on a counter. Kinda similar to `foreach` loops.

```python
# go through new_list, "item" can be any valid variable name
new_list = [1,2,3,4,5]
for item in new_list:
    print(item)

# go through a dict
new_dict = {'name': 'John', 'age': 25, 'city': 'London'}
for key, value in new_dict.items():
    print(key, value)

# go through a string
new_string = "Hello world!"
for character in new_string:
    print(character)
```

If we would for some reason need a loop variable or an index as well, we can get it the following way:

```python
for i, value in enumerate(new_list):
    print(i, value)
```

As a loop for counting, iterating between two numerical values, we can use the `range()` function:

```python
# iterating from 0 to 9
for i in range(10):
    print(i)

# iterating from 10 to 100 with a step size of 5
for i in range(10,100,5):
    print(i)
```

## List comprehension

List comprehensions provide a concise and readable way to create new lists based on existing lists or other iterables.
It is a bit similar to the declarative constructs of map, filter and reduce. 

The abstract syntax of the construct is as follows: `new_list = [expression for element in iterable]`, but let's see a few examples:

```python
# generating squares from numbers
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]

# filtering even numbers
numbers = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]

# flattening a nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [x for sublist in nested_list for x in sublist]
```

With the same syntax, we can generate not only lists, but sets, dictionaries or generator objects as well.

```python
list = [i ** 2 for i in range(10) if i % 2 == 0]            # list
set = {i ** 2 for i in range(10) if i % 2 == 0}             # set
dict = {str(i): i ** 2 for i in range(10) if i % 2 == 0}    # dictionary

gen_list = (i ** 2 for i in range(10) if i % 2 == 0)        # generator object
for item in gen_list:  
    print( item )  
```

## Functions

Above, we have already seen an example or two of functions. Lets see a few more useful features of python regarding functions.

A function can return a value:

```python
def add(a, b):
	c = a + b
	return c
```

Or multiple values at the same time:

```python
def multipleReturn():
    return 10, [20,30], "Hello World"
a, b, c = multipleReturn()
print(a, b, c)
```

Or none at all. In these cases the return value of the function would be `None`.

```python
def printSomething():
    print("Something")
```

With the use of "keyword arguments", we can add the function arguments in any order using their names:

```python
def printUserInfo(name, age, address):
    print(name, age, address)
printUserInfo(age=20,address="Budapest",name="Alice")

# the order can be "combined" as well
printUserInfo("Bob",address="Rome",age=30)
```

Functions can also take default argument values. In this case, passing those values is optional.

```python
def greet(name, message="Hello"):
    print(f"{message}, {name}!")
greet("Harry")
greet("General Kenobi", "Hello there")
```

The number of parametres can also be variable. By convention, unnamed parametres are put into the `*args` list, and named parametres are put into the `*kwargs` dictionary:

```python
def example_func(name, *args, **kwargs):
    print("Regular parameter:")
    print(f"Name: {name}")

    print("\nVariable-length arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

example_func("John", "apple", "banana", "cherry", country="USA", age=30)
```

## IO

We have already seen how we can output data, by printing it out to the console using the `print` function.

The opposite direction, listening to some input is done through the `input` function which can also print out some text as well before prompting the user for input.

```python
myinput = input("Please enter a string: ")
```

## File handling

To open a file, we use the `open()` function. 
It takes the filename and mode as parameters. The mode can be:
* `r`: Read mode (default). Opens the file for reading. Raises an error if the file does not exists.
* `w`: Write mode. Opens the file for writing. Creates a new file if it doesn't exist or truncates the file if it exists.
* `a`: Append mode. Opens the file for writing. Creates a new file if it doesn't exist. Writes to the end of the file if it exists.
* `r+`: Read and write mode. Opens the file for reading and writing. The handle is put at the start of the file. Overwrites contents character by character. Raises an error if the file does not exists.
* `w+`: Write and read mode. Any write operation will overwrite contens of the file. Creates the file if it does not exists.
* `a+`: Append and read mode. Read and write, creates the file if it does not exists. The handle is put to the end of the file, and any data written will be put at the end after the existing data.


```python
file = open("myfile.txt", "r")
```

We can read the entire content of a file or a specified number of characters/lines/all lines using `read()`, `readline()` and `readlines()` respectively.

```python
content = file.read() # reads the entire content

line = file.readline() # reads a single line (the next one)

for line in file: # iterating through all the lines one by one
	print(line)
	
lines = file.readlines() # reads all lines into an array

for line in lines: # iterating through all the lines again
    print(line)
	
```

We can also write to a file using the `write()` or `writelines()` methods. 
To use it, we have to make sure the file is opened in write or append mode.

```python
file.write("Hello world!")

file.writelines(["hello", "world"])
```

The `seek()` method allows us to move the cursor to a specific position in the file. While
the `tell()` method returns the current cursor position in the file.

```python
file.seek(position)

position = file.tell()
```


Finally, after performing operations on a file, it's important to close it using the `close()` method.

```python
file.close()
```

An alternative to having to manually close the file, we can also use the `with` statement that automatically closes
the file (or other, similar resources like connections and such) when done with it,
providing cleaner code and better error handling:

```python
with open("filename.txt", "r") as file:
    # Perform file operations here
```

If an exception happens in regards to the file opened, the `with` block exits,
but the file will still be properly closed.

## Exception handling

Exception handling in Python is managed using the `try`, `except`, 
`else`, and `finally` blocks. 
These blocks allow us to gracefully handle errors and exceptions that may occur 
during code execution.

The `try` block contains the code that might raise an exception.
This `except` is executed if an exception occurs in the try block. 
There, we can specify which exceptions to catch, or if you don't specify, 
it will catch all exceptions.
The `else` block is executed if no exceptions occur in the `try` block.
Finally `finally` :) block is always executed, regardless of whether an exception 
occurred or not. It's typically used for cleanup operations like closing 
files or releasing resources.

```python
# raising and catching an exception
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

```python
# the else block will run as 10/2 will not cause an exception
# the finally block will also run finally
try:
    x = 10 / 2 
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful. Result:", x)
finally:
    print("Executing finally block.")
```

We can also save the thrown exceptions into a variable, and/or catch
exceptions more generically (potentially catching any and all exceptions):

```python
# handling any error types thrown
try:
    x = 10 / 0 
except:
    print("An error occurred!")
```

```python
# handling any error types thrown saving it into a variable 
# and also printing it out
try:
    x = 10 / 0 
except Exception as e:
    print("An error occurred:", e)
```

> Exceptions can be raised (thrown) manually using the `raise` keyword:
> ```python
> raise RuntimeError("Our own exception thrown!")
> ```

## Entry point of a Python application

By default, a Python script is interpreted from top to bottom. To help us structure
the codebase, we can declare a main block that is meant to be executed when the
script is run directly. It is often placed inside a special block guarded by
a condition `if __name__ == "__main__":`. This condition checks if the script is 
being run directly by the Python interpreter. If it is, the code inside this block 
will be executed. If the script is imported as a module in another script, 
this block will not be executed.

```python
def main():
    print("this is the main block")

if __name__ == "__main__":
    main()
```

## Program arguments

### sys.argv

The out of the box solution Python has for passing arguments to the application is from the `sys` module.

```python
import sys

def main(args):
    print(f"Script name: {args[0]}")
    print("Arguments:", args[1:])

if __name__ == "__main__":
    main(sys.argv)
```

The first argument `sys.argv` takes is always the name of the script, followed by the rest one by one. It is important to note, that all arguments are treated as strings.

### argparse

The `argparse` module provides a more powerful way to handle command-line arguments allowing us to specify argument names, types, default values, and help messages.

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="Example script")
    parser.add_argument("arg1", type=str, help="The first argument")
    parser.add_argument("arg2", type=int, help="The second argument")
    parser.add_argument("--opt", type=float, default=0.0, help="An optional argument")

    args = parser.parse_args()

    print(f"arg1: {args.arg1}")
    print(f"arg2: {args.arg2}")
    print(f"opt: {args.opt}")

if __name__ == "__main__":
    main()
```

## OOP

The syntax of classes is a little bit different in Python.
Classes are declared with the `class` keyword. After the name of the class, between
parantheses we can supply the name of the parent classes (which our new class will extend).
Following that, class (static) properties are coming. Instance variables are declared
and initialized in the `init` function (constructor).

```python
class Food(object):

    order_count = 0

    def __init__(self, name, description, price, image):
        self.name = name
        self.description = description
        self.price = price
        self.image = image

    def print_info(self):
        print(self.name)
		self._Food__private_method()

    def __private_method(self):
        print("This can only be called internally")
```

Attributes are attributes of an object. They can be accessed through the dot notation,
both for getting or setting them. Therefore there is no explicit need for
making trivial setters or getters, it may still be good practice to make the code more clear.
Attributes can be declared anywhere in the code dynamically, however also as best practice,
we usually declare them in the constructor, which is the `__init__` block.

All methods take `self` as the first argument. Through that, we can access
the various properties of the object at hand.

Class attributes (declared at top level, without the `self` keyword) can be accessed
both through an object or through the class name with the dot notation (`myFood.order_count`, `Food.order_count`).

Every class has some automatically generated default attributes:
	* __dict__: Dictionary (map) representation of a class.
    * __doc__: Prints out the class documentation found in the code as comments surrounded by triple qotation marks (`"""`).
    * __name__: The name of the class.
    * __module__: The name of the module the class was defined in.
    * __bases__: Tuple of base classes.
    * And a few others...
	
By default, python does not have private or protected variables in classes. The convention is to name private variables start starting with an underscope, that are unadvised (but allowed) to be accessed from the outside. Functions can be made private with double underscores.

Methods on the other hand can sort of be set, however they are still not really private though. Python does some name mangling to make them "private". These private methods are declared as such using two underscored (`__`) before their name. Internally they
can be access through `self._Classname__methodName()` (and externally through `objectName._ClassName__methodName()` - kinda defeating
their entire purpose of being private mind you).

Instantiation of an object is done through calling the class name with the properties declared in the `__init__` method.

```python
food = Food("Sushi","Fish in rice",15,"sushi.png")

print(food.name) 	# Sushi

food.price = 16		# updating its price

food.print_info()   # accessing its public methods

food.order_count		
Food.order_count	# accessing class variables in two ways
```

Just as attributes can belong to a class (static attributes), methods can do so as well.

With the `@classmethod` decorator, a function can be defined that receives the class itself as the first parameter instead of an instance. This allows the function to access class parameters. This parameter is conventionally named cls. When calling the function, this parameter does not need to be explicitly provided.

With the `@staticmethod` decorator, a function can be defined that does not have a special first parameter. Therefore, it cannot access the attributes of the class it belongs to.

```python
class Food(object):
    # ...

    @classmethod
    def take_order(cls, order_items):
        cls.order_count += len(order_items)
        # process order
        return f"Order taken, current order count is {cls.order_count}"


    @staticmethod
    def is_valid_price(price):
        return price > 0

    # ...
```

Usage:

```python
order = [
    Food("Pizza", "Cheesy pizza with pepperoni", 8.99, "pizza.jpg"),
    Food("Salad", "Fresh garden salad", 4.99, "salad.jpg"),
    Food("Burger", "Delicious beef burger", 5.99, "burger.jpg")
]
order_summary = Food.take_order(order)


print(Food.is_valid_price(5.99))  # Output: True
print(Food.is_valid_price(-1))    # Output: False
```

Python also supports inheritance and multiple inheritance.
Let's define a parent class (Vehicle) and a child classes (Car) and (Airplane).
In the constructor, relevant parametres are passed to the parent class through the `super()` function.

```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

    def start_engine(self):
        print("Engine started")

class Car(Vehicle):
    def __init__(self, brand, model, color):
        super().__init__(brand, model)
        self.color = color

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Color: {self.color}")

    def drive(self):
        print(f"{self.color} {self.brand} {self.model} is driving")

    def stop(self):
        print(f"{self.color} {self.brand} {self.model} stopped")

class ElectricCar(Car):
    def __init__(self, brand, model, color, battery_capacity):
        super().__init__(brand, model, color)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"{self.brand} {self.model} is charging.")       

class Airplane(Vehicle):
    def __init__(self, brand, model, airline):
        super().__init__(brand, model)
        self.airline = airline

    def take_off(self):
        print(f"{self.brand} {self.model} operated by {self.airline} taking off")

    def land(self):
        print(f"{self.brand} {self.model} operated by {self.airline} landing")

    def start_engine(self, engine_number=1):
        print(f"Engine number {engine_number} started")
```

We can use the the following way:

```python
# car
my_car = Car("Toyota", "Camry", "red")
my_car.display_info()  
my_car.start_engine()  
my_car.drive()         
my_car.stop()          

# electric car
my_electric_car = ElectricCar("Tesla","Model Y","silver","80kWh")
my_electric_car.display_info()  
my_electric_car.start_engine()  
my_electric_car.drive()         
my_electric_car.stop()    
my_electric_car.charge()

# airplane
my_airplane = Airplane("Airbus","A380","Emirates")
my_airplane.display_info()  
my_airplane.start_engine()  
my_airplane.start_engine(1)  

# vehicle
my_vehicle = Vehicle("Caterpillar","Forklift")
my_vehicle.display_info()  
my_vehicle.start_engine()  
```

> It might not always make sense to allow instantiation of a base class. In those cases, in Python we can use an abstract (base) class.
> An abstract method can not be instantiated and has at least one of its methods marked as `@abstractmethod` (which have to be included > from the Python package `abc`).
> Any class extending this base class should have each of the abstract methods overridden to work.
> 
> ```python
> from abc import ABC, abstractmethod
> 
> class Vehicle(ABC):
>     def __init__(self, brand, model):
>         self.brand = brand
>         self.model = model
> 
>     @abstractmethod
>     def display_info(self):
>         pass
> 
>     def start_engine(self):
>         print("Engine started")
> 
> # ... then we need to properly override the display_info function in the child classes ...
> ```

Because the signature of the classes declared above has some common points (Vehicle), we can easily iterate over and call a specific function on each.

```python
vehicles = [my_car, my_electric_car, my_airplane, my_vehicle]
for vehicle in vehicles:
    start_engine()
```

Python also supports operator overloading in classes. We can define functions named like `__eq__` and `__le__` among others
which will translate to `=` and `<` in usage as well as make the objects created from that class sortable.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __eq__(self, other):
        return self.price == other.price

    def __ne__(self, other):
        return self.price != other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __str__(self):
        return f"{self.name}: ${self.price}"

product1 = Product("Laptop", 1000)
product2 = Product("Smartphone", 800)
product3 = Product("Tablet", 1200)

print(product1 < product2)
print(product2 <= product3)
print(product1 == product3)
print(product2 != product3)
print(product1 > product3)
print(product2 >= product1)

products = [product1, product2, product3]
cheapest_product = min(products)
print(f"Cheapest product: {cheapest_product}") 
```






