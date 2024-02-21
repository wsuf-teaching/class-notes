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


#### Validation

Before going further, here is a great chance to also introduce validation in React. Even though the final validation would be
done on the server, as we cannot trust validation in the browser - it is still a good idea to implement a client-side
validation as well, as it can provide feedback to the users much more readily.

In a trivial example, we can just stop the code execution in case we encounter an incorrect value. The following block should go
inside the `submitHandler`, between the `preventDefault` and the `const newFood` lines:

```jsx
if(nameRef.current.value.trim() == '') {
   return;
}
```

An improvement to this can also show some feedback to the user regarding the nature of the failed validation.
To this end, we will utilize one more state. A state that will tell us about whether a field or fields are valid or not.
We want to start with `true`, so that the name initially is valid. Then set it to `false` if the name turns out to be invalid after all.

```jsx
const [nameIsValid, setNameIsValid] = useState(false);
```

In the conditional block shown above, if the name is invalid, we set this state to `false` and return out of the function.
Otherwise, we set it to `true`, continuing on with the rest of the instructions.

```jsx
 const submitHandler = (event) => {
     event.preventDefault();

     if(nameRef.current.value.trim() == '') {
         setNameIsValid(false);
         return;
     }

     setNameIsValid(true);
     
     // ...
```

Lastly, we can display some feedback text conditionally, based on the state of the `nameIsValid` property the following way.
Put it below the `<input>` of the name.

```jsx
{!nameIsValid && <span style={{color:"red"}}>Name cannot be empty!</span>}
```

#### Child-to-parent communication

Now, we have all the data gathered and validated. It is also in a single object. But technically, we have no use for this
data here in the `FoodForm` component. We made this component so it better separates the adding/validation logic from the
rest of the application - from displaying the data. What we want is to add this new object to the list of foods in the `App` component.
Notice, that between the two of them: `App` and `FoodForm` we also have one additional component, `NewFood`.

Let's start in the intermediary component (`NewFood`).
Add a new function that "handles" a new food when added. For now, let's just log out the data it receives as a parameter.

```jsx
const addNewFoodHandler = (newFood) => {
    console.log(newFood);
}
```

This function should be passed as a "custom listener" function to the `FoodForm` component in the JSX block. Even though we write it
as `onSomething`, it is still just a prop, and a prop can take functions as well, not just primitive values or objects.

```jsx
<FoodForm onAddNewFood={addNewFoodHandler}/>
```

Inside `FoodForm`, simply call the new method passed as a prop inside the `submitHandler` function.
Don't forget to pass the props as well.

```jsx
function FoodForm(props) {
```

```jsx
props.onAddNewFood(newFood);
```

And now let's do the same process one more level.

Inside `App`:

```jsx
const addNewFoodHandler = (newFood) => {
    setFoods([...foods,newFood]);
}
```

```jsx
<NewFood onAddNewFood={addNewFoodHandler}/>
```

Then finally replace the `console.log` inside the `addNewFoodHandler` in the `NewFood` component with the passed prop function call.

```jsx
function NewFood(props) {

    const addNewFoodHandler = (newFood) => {
        props.onAddNewFood(newFood);
    }
    
    // ...
```

#### useEffect, getting remote data

Continuing forward, notice how we have all the initial food data hardcoded inside the "mockdata" folder. For testing purposes,
it is mostly fine, however in the end we want to get all our data from a remote server.

To "simulate" that, attached you can find a `server.py` in the resources folder.
To use it, you should have [Python](https://www.python.org/downloads/), pip installed.
With pip, also install `flask` and `flask-cors`.
[Here](/frontend1/test_server_setup.md#2-installing-python), you can find detailed instructions on how to install them all and run the server.
The endpoint that should be queried is `/foods`, making the full URL needed by default `http://127.0.0.1:5000/foods`.

When sent a GET request, or visited from the browser, you should see all the foods listed as JSON data.

![foods](https://i.imgur.com/kaQneVI.png)

That is what we will need and use in this section.

We already learned how to make web calls in JavaScript as part of frontend2. One of the functions JavaScript provides us out of the box
is `fetch` [fetch description here](/frontend2/javascript-async-promise-fetch.md#fetch).
There are alternative methods and libraries like [axios](https://www.npmjs.com/package/axios) but fetch can also be used in React just fine.

So how to use fetch to fetch all the needed data to set up the initial states?
Let's just try putting the fetch call inside the `App` component, somewhere, just before the return block.

> First, also make the foods state empty as a starting point, we no longer need the `mockFoods` array.
> `const [foods, setFoods] = useState();`

> Also, as this would crash our application right now, as inside the `FoodList` component, we cannot
> map over an empty object, add a null check in the return block changing this line:
> `{ props.foods && props.foods.map((food,i) => `

First, just fetch it and log both (either) the received data and the error.

```jsx
fetch('http://127.0.0.1:5000/foods')
 .then(response => response.json())
 .then(data => console.log(data))
 .catch(error => console.log(error));
```

With a successful call, we should see something like this in our browser console:
![succfetch](https://i.imgur.com/uEVrFMq.png)
And with an unsuccessful one, something along the lines of these:
![failfetch1](https://i.imgur.com/AV61E2k.png)
![failfetch2](https://i.imgur.com/9RmK54m.png)

Now we are ready to use this JSON data in the application in earnest.

```jsx
fetch('http://127.0.0.1:5000/foods')
 .then(response => response.json())
 .then(data => setFoods(data))
 .catch(error => console.log(error));
```

What we will see when running this code is not what we would first expect. It kinda works, but if we add a new food manually,
it almost immediately disappears, replaced with the original list.
Why? Because we set state! And when we set a state, and the component where the state is will be reloaded.
After the component is reloaded, fetch is called again, where we set the state... You can see where this goes.
An infinite reload loop is triggered, and the only reason we even see some elements being displayed is due
to the time the asynchronous fetch call takes. If it were instantaneous, we would see nothing, as the component
would be reloaded before even reaching the return block.

The main task of a React application is to render the UI elements and to react to various user inputs, even to manipulate
the DOM accordingly. Everything else is basically a "side effect" or "effect" in short. Sending HTTP requests,
storing data in browser, managing timers, etc. These are all terribly useful stuff, that we need, but they are not
the "core" of React. They are not something that we can only do due to React, they are not something that React cares about.
They are "side effects". Therefore, these must happen outside the normal component evaluation circle of React.
(Remember how a component reloads when a state has changed!)

In situations like this, where for example we want to execute some code when the component first loads, only once,
or depending upon some state, the `useEffect` hook is our friend.

`useEffect` is imported similarly to the `useState` hook: `import { useEffect } from 'react';`.
The rest of its usage is a little bit different though.
It kind of looks like this:

```jsx
useEffect( () => {}, [dependencies]);
```

Here, the first argument is a method that we want to call, that should be executed after every component evaluation if the 
specified dependencies have changed and also on the very first run of the component (as the dependencies loading for
the first time is considered as them being changed). Inside this function should code snippets with side effects be executed.
Then, the second argument is an array of dependencies - if any one of these change, the method in the first parameter will run.

> Leaving the dependencies array empty (`[]`) will mean that the `useEffect` will only run once - as nothing cannot change. :)

Import useEffect, and write the required hook setting the state accordingly, only running once:

```jsx
import React, { useState, useEffect } from 'react';
```

```jsx
  useEffect(()=>{
   fetch('http://127.0.0.1:5000/foods')
           .then(response => response.json())
           .then(data => setFoods(data))
           .catch(error => console.log(error));
},[])
```

Another example where we can use `useEffect`, now with dependencies is in form submissions.
We can make form submission functions leaner, separating concerns a little bit by using `useEffect`.

To practice a little bit of both forms and effects, make a new component called `Login` and call it inside the `App` component:

Making the `Login` component:

```jsx
import { useState, useEffect } from 'react';
import styles from './Login.module.css';

function Login() {

   const [email, setEmail] = useState('');
   const [password, setPassword] = useState('');

   const emailChangedHandler = (event) => {
      setEmail(event.target.value);
   }

   const passwordChangedHandler = (event) => {
      setPassword(event.target.value);
   }

   const submitHandler = (event) => {
      event.preventDefault();
      console.log(email);
      console.log(password);
   }

   return (
           <form className={styles.login} onSubmit={submitHandler}>
              <h2>Log in!</h2>
              <label htmlFor="login_email">E-mail</label>
              <input
                      type="text"
                      id="login_email"
                      value={email}
                      onChange={emailChangedHandler}
              />
              <label htmlFor="login_password">Password</label>
              <input
                      type="password"
                      id="login_password"
                      value={password}
                      onChange={passwordChangedHandler}
              />
              <button type="submit">Login</button>
           </form>
   );
}

export default Login;
```

The related `Login.module.css`:

```css
.login {
    max-width: 500px;
    margin: auto;
    display: flex;
    align-items: center;
    align-content: stretch;
    flex-direction: column;
}

.login * {
    width: 100%;
    box-sizing: border-box;
}

.login button {
    margin: 10px;
    padding: 5px;
}
```

In the top of `App`:

```jsx
import Login from './components/Login';
```

Maybe between the `<h1>` and the another `<Card>`:

```jsx
<Card>
  <Login/>
</Card>
```

The effect logic should be as follows:

```jsx
 const [formIsValid, setFormIsValid] = useState(false);

useEffect(()=>{
   setFormIsValid(
           email.includes('@') && password.trim().length > 6
   );
},[email, password])
```

And modify the submit button based on the value of this new `formIsValid` state either enabling or disabling it

```jsx
<button type="submit" disabled={!formIsValid}>Login</button>
```

Basically, what we did was move out (part) of the validation logic to a single place instead of listening
to each little individual events on their own handler functions trying to juggle many smaller states accordingly.
We can still do that, with individual state feedbacks, but now the `useEffect` hook here
manages a "global" validity variable, listening to all the input field state changes.

#### Adding a loading text

A little thing that can always make an application nicer is to show "Loading" texts or a spinning icon while content is loading.
Content is loading, while for example we make our fetch call and waiting for the server to respond.

With React, doing this is trivially easy due to its declarative nature.

> To simulate slow network, comment in `import time` at the top of the server script, as well as the call to
> `time.sleep(1)` (remove the "#" signs) then restart the python server.

Remember, when a state is changed, React will trigger a full component reload. This is the reason why at first the food list
shows up as empty, then after we receive the data, they will all pop in to the DOM.
Instead of displaying nothing, we can make the component display a "Loading" text instead while waiting for the data, so while
the data is "null", then display the `FoodList` accordingly after React reloads the component.

We can use just a null check for this just fine.
Wrap the `FoodList` component in `App` with the following snippet:

```jsx
{foods && <FoodList foods={foods}/>}
{!foods && <h4>Loading...</h4>}
```

Or in a little shorter way:

```jsx
{foods ? <FoodList foods={foods}/> : <h4>Loading...</h4>}
```

An alternative way could be using an additional state that knows whether the list is loading or not.