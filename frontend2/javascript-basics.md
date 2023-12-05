# JavaScript

JavaScript as of today is nearing 20 years old. Originally intended as a script-like "extension" for Java to make interactive
websites. Note, that it has no relation to Java whatsoever, even though their names suggesting otherwise.

Over the years, it had some sub-variants, most notably ActionScript and TypeScript - out of which only TypeScript is in use now.

HTML is responsible for the textual content, as well as the base structure of the page, and CSS's domain is to make
that content look nice and presentable. Meanwhile, JavaScript is handling the logic, the interactivity with a website.

## Location of JavaScript in a page

* Anywhere in an HTML file between opening and closing `<script>` tags. In the `<body>` or even in the `<head>`.
* In a separate script file linked through the `<script src="mylittlescript.js"></script>` notation.
* On some element's own event handler properties, like `<button onclick="javascriptfunctionhere()">`.

> If we plan on manipulating the DOM and/or using event listeners on certain DOM elements, it is good practice to either
put the `script` tags at the very end of the `<body>` section or use the `defer` property on them and then place them anywhere we like.

## Types

### Primitives

JavaScript has a few primitive data types. Primitives are variables with a single, immutable value.
They don't have any properties or methods, and immutable in this context means that their values cannot be changed.

The primitive types are as follows:

* string: Represents a sequence of characters, e.g., "hello".
* number: Represents numeric values, e.g., 42 or 3.14.
* boolean: Represents either true or false.
* undefined: Represents a variable that has been declared but not assigned a value.
* null: Represents the intentional absence of any object value.
* symbol: Introduced in ECMAScript 6 (ES6), represents a unique identifier.

We can assign these to variables (storing a value) as you would expect:

```javascript
var text = "Hello world!";
var num = 42;
var isTrue = true;
var undefined;
var nullValue = null;
var symbolValue = Symbol("uniqueSymbol");
```

> If we leave out the `var` keyword, the variable will still be created, but in the global namespace. More about both of these later. :)

Of course, we can grab a variable and assign it a different value.

```javascript
var text = "Hello world!";
text = "Goodbye world!";
```

This seemingly contradicts primitives being immutable, but it does not. When we manipulate primitive values,
we work with the actual value stored in the variable, and any operation on a primitive value returns a new value without
modifying the original. So in this case "Hello world!" is not modified to be "Goodbye world!", but rather the contents of the 
`text` variable are replaced with the new one.

> Everything else in JavaScript that is not a primitive data type (introduced just above) is treated as an object.


## Variables

We have seen above how we can create a variable with the `var` keyword, and also by simply assigning a value to a "name".
There are two more types, so let's see all of them together.

* `var` has a function scoping (only working in the function they are declared in)
* "assignment without keyword" has a global scoping, being available anywhere in the script.
* `const` which stands for "constant". The values of constants cannot be changed later (hence their name). They will give as an error if we try to do so and they also require a value to be provided when creating them.
* `let` is a simple and mutable block-scoped (in a class, in a function or in a foor loop or if-else construct, etc.) variable.

```javascript
name = "John";
age = 25;

var city = "Budapest";
var population = 1700000;
var size;

let product;
product = "TV";
let price = 300;
price = 300;

const something;        // this would give as an error
const pi = 3.14;
pi = 3.1415;            // this again would give an error
```

### Basic arithmetic operators

* `+` for addition `let sum = 5+3`
* `-` for subtraction `let diff = 7-2`
* `*` for multiplication `let prod = 4*6`
* `/` for division `let quotient = 10/2`
* `%` for modulus calculation (returns the remainder of the left operand divided by the right operand) `let remainder = 15%4` (3).
* `**` for exponentiation (raises the left operand to the power of the right operand) `let result = 2 **3` (8)

## Type system

JavaScript is what is considered a weakly typed language. This means that a variable can be dynamically assigned a value of any
data type during runtime. For example a variable that initially held a string can later contain a number instead and operators might
behave differently in different types.

> We can check the (current) type of a variable with the `typeof` keyword.

### Dynamic types

```javascript
let a = 2;
let b = 4;
alert(a + b);           // 6 (Number)

a = "John ";
b = "Doe";
alert(a + b);           // John Doe (String)
```

### Implicit type conversion (coercion)

JavaScript performs automatic type conversion when operators or functions expect a certain type. This can lead to unexpected behavior if not understood carefully.

```javascript
let a = 5;
let b = "10";
let result = a + b;     // JavaScript converts 'a' to a string and performs string concatenation
alert(result);          // 510

let year = 2023;
let month = "January";
alert(year + month);    // "2023January"
alert(year + month + 1);// "2023January1"
alert(year + 1 + month);// "2024January"
```
### Equalities, inequalities

In JavaScript, both `==` and `===` are comparison operators used to compare values. However, they differ in terms of their behaviour and the type of comparison they perform.

#### Equality (==)

The equality operator only compares values. To that end, it performs type coercion trying to convert the operands to the same type before
making the comparison. After the coercion, it checks whether the values are equal. This type of equality can thus lead
to unexpected returns.

```javascript
5 == "5"                // true, as number 5 is coerced into string "5"
true == 1               // true, as boolean is coerced into number 1
```

```javascript
let year = 2023;
alert(year == "2023");    // true, as number 2023 is coerced into string "2023"
```

#### Strict equality (===)

The strict equality operator does not perform type coercion. It simply checks if the values are equal and
of the same type. In this case if the operands are of different types, the operator returns false without trying to convert them.

```javascript
let year = 2023;
alert(year === "2023");    // false, as they are different types
```

#### Inequalities (!= and !==)

Work in very much the same (but opposite) way to their equality counterparts with `!=` performing coercion while `!==` does not.

```javascript
5 != "5"                // false
true != 1               // false

5 !== "5"               // true
true !== 1              // true
```

### Undefined

If a variable is not assigned a value, both it's type, and it's value will be `undefined`.

```javascript
let myvar;
alert(myvar);           // undefined
alert(typeof myvar);    // undefined
```

> Surprisingly enough, the type of `null` is not `null` but `object`. More about objects later.

### Conversion to boolean, truthy and falsey values

We know that booleans can be either `true` or `false`. However, in JavaScript, everything can be checked as if it were a boolean.
We call these "truthy" or "falsey" values based on whether they would be evaluated as the former or the latter.

Truthy values are `true`, any non-empty strings, any non-null numbers, empty or non-empty arrays or objects.
Falsey values are `false`, the number 0, empty strings, `null` and `undefined`.

#### Negation

Any booleans can be negated with the negation `!` operator put just before the value or variable.

```javascript
!true;                  // false
let myboolean = false;
!myboolean;             // true
```

#### Double negation and boolean conversion

Furthermore, anything in javascript can be converted to boolean by the use of double negation `!!`.
Let's think of it this way: The first negation performs a type conversion (then negates its value), and then
the second negation turns its value back to its "original" truthy or falsey value.

```javascript
let mytext = "Some text";
alert(typeof !!mytext);     // boolean
alert(!mytext);             // false
alert(!!mytext);            // true
```

#### Equality revisited

'0' as a string is truthy, but 0 as a string is falsey. What happens when we compare them??

```javascript
alert('0' == 0);            // true, as == only compares their values
alert('0' === 0);           // false, as it checks their types first which are different in this example
```


Equality checks might even behave differently if done through `==` signs, or through implicit type conversion for example in an `if` statement.

[Look at this website](https://dorey.github.io/JavaScript-Equality-Table/) to see an exhaustive table for some funky type coercions.

<b>Moral of the story: Always use 3 equals unless you have a good reason to use 2. </b>

[//]: # (todo conditionals, default values, existence check and quick evaluation, ~p23 or so)

## Conditionals

conditionals are used to make decisions in your code based on certain conditions. 
The primary conditional statements are `if`, `else` and the `switch`-`case` construct.
In addition, there are a couple of shorthand notations for conditionals as well which we will see later in this section.

### If-else

The `if` statement is used to execute a block of code if a specified condition is true (truthy!).
Meanwhile, the `else` statement is used in conjunction with `if` to execute a block of code if the specified condition is false (falsey!).

```javascript
if (condition) {
    // code to be executed if the condition is true
} else {
    // code to be executed if the condition is false
}
```

Lastly, the `else if` statement is used when you have multiple conditions to check. It allows you to check for additional conditions if the previous ones are false.

> We can chain as many if-else statements as we want.

```javascript
if (condition1) {
    // code to be executed if condition1 is true
} else if (condition2) {
    // code to be executed if condition2 is true
} else {
    // code to be executed if all conditions are false
}
```

For example:

```javascript
let num = 5;

if (num > 0) {
    console.log("Positive number");
} else if (num < 0) {
    console.log("Negative number");
} else {
    console.log("Zero");
}
```

### Switch-case

The `switch` statement is used to perform different actions based on different conditions. It is an alternative to using multiple `if` and `else if` statements.

```javascript
switch (expression) {
    case value1:
        // code to be executed if expression === value1
        break;
    case value2:
        // code to be executed if expression === value2
        break;
    // more cases as needed
    default:
        // code to be executed if none of the cases match
}
```

As a concrete example:

```javascript
let num = 5;
switch (num) {
    case 1:
        console.log("One");
        break;
    case 2:
        console.log("Two");
        break;
    default:
        console.log("Other");
}
```

### Logical AND (&&)

The logical `&&` operator returns `true` if both operands are `true` and `false` otherwise.

```javascript
let x = true;
let y = false;
console.log(x && y);            // false
console.log(x && true);         // true
console.log(false && true);     // false
```

### Logical OR (||)

The logical `||` operator returns `true` if at least one of the operands is `true` and `false` otherwise.

```javascript
let a = false;
let b = true;

console.log(a || b);            // true
console.log(true || false);     // true
console.log(false || false);    // false
```

### Short circuit evaluation

Related to the two logical operators above, one important behaviour to note is short-circuit evaluation.

In logical AND (`&&`) if the left operand is `false`, the right operand is not evaluated because the overall result will be `false` regardless.
In logical OR (`||`) if the left operand is `true`, the right operand is not evaluated because the overall result will be `true` regardless.

These operators are commonly used in conditional statements, such as if statements, to make decisions based on certain conditions in your JavaScript code.

Let's see a real-life example for both of these operators:

```javascript
let name;                           //  do some logic to ask for the user's name here
let userName = name || "Guest";     // if the name is empty (therefore falsey), set "Guest" as the userName
```

```javascript
user.isAuthenticated && doSomeLogicHere();  // the "doSomeLogicHere" function is only executed if "user.isAuthenticated" is truthy
```

## Loops

Loops are used to repeatedly execute a block of code as long as some specific statement or condition holds true (truthy).

### for loop

The basic syntax of the `for` loops is as follows:

```javascript
for (initialization; condition; iteration) {
    // code to be executed in each iteration
}
```

As a concrete example:

```javascript
for (let i = 0; i < 5; i++) {
    console.log(i);
}
```

The snippet above executes five times, and writes out the current loop number to the console.

> Good to know, that all three of these parametres are optional!
> For example we can right the following statement to have an infinite loop executing forever
> (or until the program is killed) `for(;;)`.

