#### Event listeners

With HTML and JavaScript, one can attach event listeners to various events such as click, change, submit, etc.
Adding these to default elements or custom components is fairly trivial as well.

Let's start experimenting with this in the `<App/>` component.

Add a button in the JSX block and then promptly create the handler function as well.

```jsx
<button onClick={handleButtonClick}>Click me!</button>
```

```js
const handleButtonClick = () => {
    alert('You clicked me. ');
}
```

Listening to an event is as simple as this.

What if we want to listen on a custom component?
All the same. Put the click listener on `<Welcome>` and it will work out of the box.

```js
<Welcome borderWeight={3} onClick={handleButtonClick}>
    Food list is <span>working</span>
</Welcome>
```

If we need to pass a parameter to a function, it can be done, however that process is a little more involved.

To the handler function, the only change is the added parameter, and potentially doing something with it.
```js
const handleButtonClick = (param) => {
    alert('You clicked me. ' + param);
}
```

To update the binding, the naïve idea would be to do it like this: `<button onClick={handleButtonClick("Hello")}>Click me!</button>`

> This would not work as expected, as putting the parentheses behind the function name in the JSX block
> would execute the function every time it is displayed, and we do not want that.


For binding a function with parameters, we have two options:

1. Pass it with a lambda function. Basically wrapping it in a function that executes when it is needed.
```<button onClick={() => handleButtonClick("Hello")}>Click me!</button>```

2. Pass it through parameter binding. ```<button onClick={handleClick.bind(null, 'Hello')}>Click me</button>```

#### States, useState

To continue this event listener example as well as move forward, let's create a new `<h1>` in App, right around the `<Welcome>`
component. Feel free to comment out or delete `<Welcome>` for now.

It can look something like this:

```jsx
<h1 style={{textAlign:"center"}}>Food!</h1>
```

We can go even further, and declare the text above the JSX block as a simple variable and use that instead.

```js
let title = "Food!";
```

```jsx
<h1 style={{textAlign:"center"}}>{title}</h1>
```

Visually, nothing should change as expected.

Let's add another button and another handler function changing that title somehow.

```jsx
<button onClick={handleChangeTitle}>Change title</button>
```

```js
const handleChangeTitle = () => {
    this.title = "Order food!";
}
```

What we would expect is that the title would be changed, but it did not. Or did it?
Add some console logs around the assignment to find out the truth!

```js
const handleChangeTitle = () => {
    console.log(title);
    title = "Order food!";
    console.log(title);
}
```

The variable `title` has indeed changed, but the DOM does not reflect this change. _Why?_
Because React is not built that way. To understand it, first we have to understand how React parses and renders the JSX blocks in the code,
how it evaluates a Component from start to finish.
Components are basically fancy functions. They are evaluated from the top all the way down to the bottom where the return block
returns some JSX code (the components of which are also functions...). Kind of like a recursive data structure. Functions in functions, function
calls in function calls, components in components, starting all the way from `index.js` where we call the `ReactDOM.createRoot(...` function...

When we change the `title` variable, the class has already been evaluated and returned its pre-set title. Changing a variable
in a component after this point has no effect on anything that has already been displayed.
_Then what? How we can force React to change its contents?_
With a different mechanism. We have to let React know that something has changed. We want React to re-evaluate this component
after we change the title somewhere, somehow. It can be done through a concept called State.
States are what React cares about this context, meanwhile it ignores "simple" variables like our `title`.

What we need is a function called `useState`. We need the following named import to make it available:

```js
import React, { useState } from 'react';
```

> `useState` can ONLY be used inside React components.

What the documentation tells about this function is as follows: _"Returns a stateful value, and a function to update it."_
This special function returns two things. A value and a function. As an easy way to handle it, we will use
a concept called [Object Destructuring / Destructuring assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment).

With `useState` we are basically creating a very special kind of variable where changes will cause the component to be reevaluated.
The named of the destructured variable and function can be anything, but by convention, they are usually called "x" and "setX",
in our case `title` and `setTitle`. Replacing the original `let title = "Food!"` assignment, what we should have is this `useState` call:

```js
const [title, setTitle] = useState("Food!");
```

`title` is for retrieving and using the value stored in the State, while `setState` should be the only function
that can change its value.

Using `title` is exactly like we used it before, while now our assignment in the `handleChangeTitle` function
is illegal, as we cannot assign new values to constant variables. The `handleChangeTitle` function should correctly be modified as such
to use the `setTitle` method.

```js
const handleChangeTitle = () => {
    setTitle("Order food!");
}
```

States can of course hold much bigger and larger things as well, not just small variables like a string or a number.
Still staying in the `<App>` component, make a new State from the `mockData` array as well.
Just as we used an inlined string in the previous example, we can use variables to initialize a state too.

```js
  const [foods, setFoods] = useState(mockFoods);
```

Also, remember to change the `<FoodList>` parameter to the new state as well.

```jsx
<FoodList foods={foods}/>
```

Let's also add a third button:

```jsx
<button onClick={addFoodHandler}>Add food</button>
```

With the respective function above which it requires:

```js
const addFoodHandler = () => {
    // todo
}
```

Now this will be a little tricky, but nothing that we cannot manage.
Remember that we cannot directly edit the state and add new elements to it. We have to use the setFoods function
to create a new foods state from the previous state and the newly added element.

1. Create a new food:
   ```js
   const newFood = {
   name: "Pizza",
       url: "https://www.mindmegette.hu/images/388/Social/lead_Social_pizza-alap-recept.jpg",
       description: "Pizza is a dish of Italian origin consisting of a usually round, flat base of leavened wheat-based dough.",
       price: 8
   };
   ```

2. Create a new array from the `foods` state and the newly created element.
   ```js
      const newFoods = [...foods, newFood];
   ```
   > Notice the [spread operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax).

3. Set that new array as the new state.
   ```js
     setFoods(newFoods);
   ```

In summary:

```js
  const addFoodHandler = () => {
    const newFood = {
        name: "Pizza",
        url: "https://www.mindmegette.hu/images/388/Social/lead_Social_pizza-alap-recept.jpg",
        description: "Pizza is a dish of Italian origin consisting of a usually round, flat base of leavened wheat-based dough.",
        price: 8
    };
    const newFoods = [...foods, newFood];
    setFoods(newFoods);
  }
```

It is nice to store data / variables into state objects using the `useState` hook. 
Let's store the food data in the `Food` component this way as well.

> To make our lives easier, add some CSS centering the content to the `App` component.
> To that end, replace the fragments with a `div` with the `container` `className` attached to it.
> From this: `<>...</>` to this: `<div className='container'>...</div>`.
> In `index.css`, add the container class, and add the max-width and margin properties over to there as follows:
> `.container {
> max-width: 900px;
> margin: 15px auto;
> }`

