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

#### Forms and states

What we did in the App component is a simple button that adds a new element with hard-coded data. Let's improve upon that
by making a new component that is able to add a new element dynamically, through a form where we can type in the properties
of the new food item that we want to add.

Make a new component called `NewFood.js` and another called `FoodForm.js`:

```jsx
import FoodForm from "./FoodForm";
import styles from './NewFood.module.css';

function NewFood() {
   return(
           <div className={styles.newfood}>
              <h2>Add a new Food!</h2>
              <FoodForm/>
           </div>
   );
}

export default NewFood;
```

```jsx

function FoodForm() {

   return (
           <form>
              <label htmlFor="foodform_name">Name</label>
              <input type="text" id="foodform_name" onChange={nameChangedHandler}/>
              <label htmlFor="foodform_imageurl">Image URL</label>
              <input type="text" id="foodform_imageurl"/>
              <label htmlFor="foodform_description">Description</label>
              <textarea id="foodform_description"/>
              <label htmlFor="foodform_price">Price</label>
              <input type='number' step="1" id="foodform_price"/>
              <button type="submit">Add</button>
           </form>
   );
}

export default FoodForm;
```

> Notice the use of `htmlFor`, instead of just `for` as in vanilla JavaScript. Same situation as with `class` and `className`.

The `NewFood.module.css` is as below:

```css
.newfood {
   max-width: 500px;
   margin: auto;
}

.newfood form {
   display: flex;
   align-items: center;
   align-content: stretch;
   flex-direction: column;
}


.newfood form * {
   width: 100%;
   box-sizing: border-box;
}

.newfood button {
   margin: 10px;
   padding: 5px;
}
```

And make an instance of this in the `App` component once. Maybe between the `<h1>` and a `<button>` below it. Don't forget to import it!
We can even wrap it in a `<Card>` to make it even nicer.

```jsx
    <Card>
        <FoodForm/>
    </Card>
```

Next, regarding the form. What we want to have is to listen to every single keystroke, getting the value the user entered
and store it somewhere.
The `onChange` event listener can be used for that for example. `onInput` also works, but `onChange` is more universal, and works with all
input fields.

For example, add the `onChange` event listener on the name field: `onChange={nameChangedHandler}` and of course, also declare
the handler function above in the component:

```jsx
 const nameChangedHandler = () => {
     console.log("name changed");
 }
```

This is not that useful for now. This event handler function however, similarly to vanilla JavaScript, can take a parameter (representing the event),
through which we will have access to various properties among which is the `target.value` which basically represents the
text that is currently in the input field.

```jsx
const nameChangedHandler = (event) => {
    console.log(event.target.value);
}
```

Combining what we know so far, one way we can handle gathering the values of the input fields is creating one or more state for them,
promptly assigning them in the event handler functions.

```jsx
 const [name, setName] = useState('');

 const nameChangedHandler = (event) => {
     setName(event.target.value);
 }
```

> Once again don't forget to import `useState`: `import { useState } from "react";`!

Similarly, we can employ the same way to deal with the rest of the input fields. Just below, here is how the component would look like:

```jsx
import { useState } from "react";

function FoodForm() {

    const [name, setName] = useState('');
    const [imageUrl, setImageUrl] = useState('');
    const [description, setDescription] = useState('');
    const [price, setpPrice] = useState('');

    const nameChangedHandler = (event) => {
        setName(event.target.value);
    }

    const imageUrlChangedHandler = (event) => {
        setImageUrl(event.target.value);
    }

    const descriptionChangedHandler = (event) => {
        setDescription(event.target.value);
    }

    const priceChangedHandler = (event) => {
        setPrice(event.target.value);
    }

    return (
        <form>
            <label htmlFor="foodform_name">
                Name
            </label>
            <input 
                type="text" 
                id="foodform_name" 
                onChange={nameChangedHandler}/>
            <label htmlFor="foodform_imageurl">Image URL</label>
            <input 
                type="text" 
                id="foodform_imageurl" 
                onChange={imageUrlChangedHandler}/>
            <label htmlFor="foodform_description">Description</label>
            <textarea 
                id="foodform_description" 
                onChange={descriptionChangedHandler}/>
            <label htmlFor="foodform_price">Price</label>
            <input 
                type="number" 
                step="1" 
                id="foodform_price" 
                onChange={priceChangedHandler}/>
            <button type="submit">Add</button>
        </form>
    );
}

export default FoodForm;
```

Managing all these individually is one (totally fine) option. There is also an alternative. Instead of having multiple small "sub states" or
"state slices", just managing one big composite state.
Just as a state can represent a number, a string or a boolean, it can also be an object.

```jsx
 const [userInput, setUserInput] = useState({
   name: '',
   imageUrl: '',
   description: '',
   price: ''
});
```

One big difference would be, that in this new case, if we were to update one "piece" of the state, we have to update all of them.
The easy way to handle updating the state in this case would be to use the spread operator, then overwrite the property that
needs to be changed.

For example in the `nameChangedHandler`:
```jsx
 const nameChangedHandler = (event) => {
   setUserInput({
      ...userInput,
      name: event.target.value
   });
}
```

And in all of them:

```jsx
 const nameChangedHandler = (event) => {
     setUserInput({
         ...userInput,
         name: event.target.value
     });
 }

 const imageUrlChangedHandler = (event) => {
     setUserInput({
         ...userInput,
         imageUrl: event.target.value
     });
 }

 const descriptionChangedHandler = (event) => {
     setUserInput({
         ...userInput,
         description: event.target.value
     });
 }

 const priceChangedHandler = (event) => {
     setUserInput({
         ...userInput,
         price: event.target.value
     });
 }
```

> In all of the cases above, we "depend on" the "previous state" to properly set the new (current) state. This is mostly fine,
and also will mostly work find in most, but a few niche cases. React schedules state updates, it does not perform them immediately.
> In rare cases it can potentially happen, that by the time React schedules the next update, the state have been already changed
> by other methods or logic.

When we update state however, while also depending on the previous state, an alternative form of this is recommended to use.
Pass a function that receives the previous state at the exact time when it has to be updated, as well as which then updates the state based on that.

```jsx
    const nameChangedHandler = (event) => {
        setUserInput((prevState)=>{
            return {...prevState, name: event.target.value};
        });
        console.log(userInput);
    }

    const imageUrlChangedHandler = (event) => {
        setUserInput((prevState)=>{
            return {...prevState, imageUrl: event.target.value};
        });
    }

    const descriptionChangedHandler = (event) => {
        setUserInput((prevState)=>{
            return {...prevState, description: event.target.value};
        });
    }

    const priceChangedHandler = (event) => {
        setUserInput((prevState)=>{
            return {...prevState, price: event.target.value};
        });
    }
```

**Anyway, for now, let's go back to the initial version of the individual states.**

```jsx
    const [name, setName] = useState('');
    const [imageUrl, setImageUrl] = useState('');
    const [description, setDescription] = useState('');
    const [price, setPrice] = useState('');

    const nameChangedHandler = (event) => {
        setName(event.target.value);
    }

    const imageUrlChangedHandler = (event) => {
        setImageUrl(event.target.value);
    }

    const descriptionChangedHandler = (event) => {
        setDescription(event.target.value);
    }

    const priceChangedHandler = (event) => {
        setPrice(event.target.value);
    }
```

Now we know how to listen to changes in the form, but so far we did not know anything exciting with that data. Next, we should
look into how we can submit forms.

We can either listen to the `onClick` event of the button, but there is a more sophisticated way to achieve the same functionality.
Remember, that by default, a `<button>` with the `type="submit"` property will automatically submit a form. Therefore, a better way
is to listen to the `onSubmit` event of the form itself.

```jsx
    // ...

    const submitHandler = () => {}

    return (
        <form onSubmit={submitHandler}>
           {/* ... */}
```

Beware another default functionality here. The submit button by trying to submit the form will trigger a page reload event.
This is something we should prevent here, as we want to handle the form submission through React.
Thus, the automatic submission should be prevented. Modify the handler function to that end:

```jsx
    const submitHandler = (event) => {
        event.preventDefault();
    }
```

Inside this event handler function now, we can gather up all the state values into a single object. Finally, we can `console.log` out the fresh
object.

```jsx
const submitHandler = (event) => {
   event.preventDefault();
   
   const newFood = {
      name: name,
      imageurl: imageUrl,
      description: description,
      price: price
   };
   
   console.log(newFood);
}
```

> Notice the syntax. The keys are the properties of the new object we are creating, while the values (with the same name)
> now refer to the name of the states we are using in this component.

#### Two-way binding

Coming next up, pretend that by logging out the new food, we submitted it into a server for processing. What is the next step?
Clearing the input forms.

First, if we clear a state by setting it to an empty string or such, it will not remove the entered strings from the form controls.
Second, grabbing the JSX elements individually and then setting their value properties to empty strings is also tiresome.

Good news is, that (unknowingly) we already did set up one direction of the two-way binding. We already listen to changes in
the form elements. The other direction is simply "feeding" the data back to the elements through setting the `value`property to
the states. That means that when we change a state, basically we also change the input, and the other way around of course.

```jsx
        <form onSubmit={submitHandler}>
            <label htmlFor="foodform_name">
                Name
            </label>
            <input 
                type="text" 
                id="foodform_name"
                value={name}
                onChange={nameChangedHandler}/>
            <label htmlFor="foodform_imageurl">Image URL</label>
            <input 
                type="text" 
                id="foodform_imageurl"
                value={imageUrl}
                onChange={imageUrlChangedHandler}/>
            <label htmlFor="foodform_description">Description</label>
            <textarea 
                id="foodform_description" 
                value={description}
                onChange={descriptionChangedHandler}/>
            <label htmlFor="foodform_price">Price</label>
            <input 
                type="number" 
                step="1" 
                id="foodform_price" 
                value={price}
                onChange={priceChangedHandler}/>
            <button type="submit">Add</button>
        </form>
```

Making this change would not result anything noticeable at the first look. However, now if we "null out" the states in the `submitHandler` method,
the input fields will be similarly reset to empty values.

Put the following code to the end of the `submitHandler`, right below the `console.log` call:

```jsx
setName('');
setImageUrl('');
setDescription('');
setPrice('');
```

#### useRef

If we don't really plan on changing the values of the states, another option React gives is the `useRef` hook.
References provide the (same) two-way binding out of the box, with less boilerplate code needed.

Delete all, but the `submitHandler` method with a list of references as follows. Don't forget to import `useRef` the very same way we
imported `useState`.

```jsx
 const nameRef = useRef();
 const imageUrlRef = useRef();
 const descriptionRef = useRef();
 const priceRef = useRef();
```

In the JSX part, replace all the `value` and `onChange` properties with the `ref` property.

```jsx
     <form onSubmit={submitHandler}>
         <label htmlFor="foodform_name">
             Name
         </label>
         <input 
             type="text" 
             id="foodform_name"
             ref={nameRef}/>
         <label htmlFor="foodform_imageurl">Image URL</label>
         <input 
             type="text" 
             id="foodform_imageurl"
             ref={imageUrlRef}/>
         <label htmlFor="foodform_description">Description</label>
         <textarea 
             id="foodform_description" 
             ref={descriptionRef}/>
         <label htmlFor="foodform_price">Price</label>
         <input 
             type="number" 
             step="1" 
             id="foodform_price" 
             ref={priceRef}/>
         <button type="submit">Add</button>
     </form>
```

Finally, we can access values in the submitHandler function by using the `current.value` property of the references.

```jsx
 const submitHandler = (event) => {
     event.preventDefault();

     const newFood = {
         name: nameRef.current.value,
         imageurl: imageUrlRef.current.value,
         description: descriptionRef.current.value,
         price: priceRef.current.value
      };
      
     console.log(newFood);

     nameRef.current.value = '';
     imageUrlRef.current.value = '';
     descriptionRef.current.value = '';
     priceRef.current.value = '';
 }
```

> Usually it is not a good idea to directly manipulate the value of the input elements like this in React, but in this
> trivial form submission case, it is probably fine!
