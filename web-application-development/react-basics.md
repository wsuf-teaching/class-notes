

## Getting started

Now that we have a working react project setup, let's look at what is created and what is actually needed for this all to work.

There are two main folders created: `public` and `src`.

### public folder

`public` is the folder where we can place static assets that we want to be publicly accessible, such as images, fonts, and other files. These then can be referred to by their absolute paths, and sent to the browser usually "as is".

Inside that, `index.html` serves as the template for the react single-page application. This HTML file is loaded when the user opens the application in a web browser.

Inside the `<body>`, we will see two elements:

`<noscript>` and a `<div>` with an id of `root`.

A React application is built entirely through javascript, so if it is disabled or otherwise unavailable, the application simply cannot function. That's when the `<noscript>` tag comes into play, and simply prints some text or HTML elements in the user's browser.

The `<div id="root">` is by convention the entry point of the React application. React grabs this point in the DOM with javascript `document.getElementById` and then populates it with content.

### src folder

The `src` folder is where we typically store the source code of the React application. It contains all the JavaScript/TypeScript files, stylesheets, and other assets.

Here, the entry point is usually an `index.js`. It typically imports the main component of the application and renders it into the root element specified in the `public/index.html` file.

> The `<React.StrictMode>` component enables some checks highlighting potential problems in an application, like usage of deprecated or legacy components, problems with component lifecycles or incorrect API usages.


`App.js` by convention is typically the "main component", the first component of a React application that renders.

### Leaning it all up

If we want to lean or application up, removing all, but the most vital components, we can do so by deleting the following files for now:

```
App.css
App.test.js
logo.svg
reportWebVitals.js
setupTests.js
```

Of course, the imports, links and functions pointing to them should also be deleted from the respective `.js` files.

> We could do the same with the `public` folder, but we don't typically touch anything there, so it can be left alone.

How it would look like after cleaning up a bit:

index.js:
```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

App.js:
```javascript
function App() {
  return (
    <div>
      Hello world!
    </div>
  );
}

export default App;
```

index.css: as you wish :)

### React root and creating elements

In `index.js` we can see that first we retrieve the root element from the DOM, then render a component inside it.

```javascript
const root = ReactDOM.createRoot(document.getElementById('root'));
```

It doesn't have to be a "component" per say.
What we render can be any "HTML element" or react component.

For example a simple `<h1>`:

```javascript
root.render(<h1>Hello world!</h1>);
```

It can be multiple "elements" inside each other just as we would do in HTML:

```javascript
root.render(
<ul>
  <li>Sun</li>
  <li>Earth</li>
  <li>Moon</li>
</ul>
);
```

Furthermore, these "elements" can even be saved to a variable first.

```javascript
const myElements = (
  <ul>
    <li>Sun</li>
    <li>Earth</li>
    <li>Moon</li>
  </ul>
);

root.render(myElements);
```

>Actually what happens in the background in all these cases is multiple `React.createElement` calls >embedded in each other.
>
>This:
>```javascript
> root.render(<h1>Hello world!</h1>);
>```
>
>is equivalent to:
>```javascript
>root.render(
>    React.createElement('h1',{},'Hello world!')
>);
>```
>
>Where the first parameter (`h1` here) is the name of the element or component that we want to >render. The second parameter is a list of "props", more about them in a little while - but we keep >them empty here. The rest of the parameter(s) are child components that we want to render inside the >component declared as the first parameter.
>
>Let's see an example with multiple levels of components:
>
>This from above:
>```javascript
>root.render(
><ul>
>  <li>Sun</li>
>  <li>Earth</li>
>  <li>Moon</li>
></ul>
>);
>```
>
>is equivalent to:
>
>```javascript
>root.render(
>  React.createElement('ul',{},
>    React.createElement('li',{},'Sun'),
>    React.createElement('li',{},'Earth'),
>    React.createElement('li',{},'Moon'),
>  )
>);
>```

### Components

So this is all working, but continuing on like this, we would pretty soon find ourselves in a similar situation to what we had with regular HTML. Everything in one place, cluttered.
If we can, we would like to avoid that. Components to the rescue!

Components in one of their most raw state look earily similar to javascript functions, hence a subset of them are called "functional components". (There are also class components, more about them later)

The `App.js` is precisely such a component. A function that returns some "html" in a return block.

Mind you, that snippet, even though looks like HTML, it is not really HTML. In React it is called "JSX". It is a syntactic extension to JavaScript that allows us to describe how the UI should look like. JSX closely resembles XML/HTML, but is embedded directly in JavaScript code. In addition, it allows embedding JavaScript expressions into it with curly braces `{}`. Before being rendered in a web browser, these JSX snippets all get converted into a chain of `React.createElement...` calls.

```javascript
function App() {
  return (
    <div>
      Hello world!
    </div>
  );
}

export default App;
```

> If the compoent resides in a separate file, it also has to be exported like in the last line of the code piece above.

After this, the component can be used in other components or `createElement` or `render` calls with using the name of the component like you would a self-closing HTML tag: `<App/>` after we import it (`import App from './App';`).

Thus, index.js should look like this: 
```jsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <App/>
);
```

#### Outputting dynamic data

A component can consist of a lot more than just a return (render) block.

Let's create a component called Food that will display some information about a food we are selling in our delivery app.

Usually what we like to do in react is to create a new folder called `components` inside `src`, and create a file called `Food.js` under it.

```jsx
function Food() {
    return (
        <div className="food">
            <h2>Spaghetti</h2>
            <img src="https://www.bowlofdelicious.com/wp-content/uploads/2023/07/one-pot-spaghetti-with-meat-sauce-square-500x375.jpg"></img>
            <p>Spaghetti is a long, thin, solid, cylindrical pasta. It is a staple food of traditional Italian cuisine.</p>
            <h4>Price: $10</h4>
        </div>
    );
}

export default Food;
```

> Notice how we used `className` instead of `class`, as the latter is a reserved keyword in React.

Here is also some example CSS we can add to `index.css` to make it look a little bit nicer:

<details>
    <summary>Food css (<i>click to expand</i>)</summary>

```css
.food {
  border: 2px solid red;
  padding: 10px; 
  display: flex;
  margin: auto; 
  max-width: 900px;
  min-height: 150px;
}

.food h2 {
  min-width: 170px;
}

.food h4 {
  min-width: 100px;
}

.food * {
  margin: 5px;
}

.food img {
  width: 100px;
  object-fit: cover;
}

.food #sale {
  background-color: salmon;
  color: white;
  align-self: center;
}
```

</details>

All we have so far is static data "hardcoded" into the JSX part of the component.
Before the return block, we can make variables, and store data inside them.

Create them:

```jsx
    const name = "Spaghetti";
    const url = "https://www.bowlofdelicious.com/wp-content/uploads/2023/07/one-pot-spaghetti-with-meat-sauce-square-500x375.jpg";
    const description = "Spaghetti is a long, thin, solid, cylindrical pasta. It is a staple food of traditional Italian cuisine.";
    const price = 10;
```

Then use the curly braces (`{}`) inside the JSX block to print them out into the DOM as follows:

```jsx
    return (
        <div className="food">
            <h2>{name}</h2>
            <img src={url}></img>
            <p>{description}</p>
            <h4>Price: ${price}</h4>
        </div>
    );
```

Between the curly braces, smaller JavaScript statements and logic can be executed as well:

```jsx
            <h2>{name.toUpperCase()}</h2>
```

#### Passing props

Props (short for properties) are a way to pass data from a parent component to a child component. They can pass variables, objects, or functions as well.
They are declared like they were custom HTML attributes.

Move the food variables to the `App` component then pass them one by one. The name of the properties can be anything:

```jsx
      <Food name={name} url={url} description={description} price={price}/>
```


On the receiving component's side, the function receives them as a single object parameter - which we have to now add, and also which we usually call "props", but can be called anything as usual.

```jsx
function Food(props) {
```

As this parameter is an object, we have to use the object notation to retrieve the various parts of data that were sent to this component:

```jsx
            <h2>{props.name.toUpperCase()}</h2>
            <img src={props.url}></img>
            <p>{props.description}</p>
            <h4>Price: ${props.price}</h4>
```

Alternatively, if the data is bundled up in a single object, then the passing syntax becomes much more concise.

Replace the previous variables with a single one in `App`:

```jsx
const spaghetti = {
  name: "Spaghetti",
  url: "https://www.bowlofdelicious.com/wp-content/uploads/2023/07/one-pot-spaghetti-with-meat-sauce-square-500x375.jpg",
  description: "Spaghetti is a long, thin, solid, cylindrical pasta. It is a staple food of traditional Italian cuisine.",
  price: 10
};
```

The component call would be just this now:

```jsx
      <Food data={spaghetti}/>
```

Lastly, as we call the whole prop as "data" now, we have to put that in their name as well as follows inside `Food`:

```jsx
            <h2>{props.data.name.toUpperCase()}</h2>
            <img src={props.data.url}></img>
            <p>{props.data.description}</p>
            <h4>Price: ${props.data.price}</h4>
```


Let's also see a dummy example where we pass a function as a prop.
Declare it once again in `App.js`:

```jsx
  const printTime = () => {
    return new Date().toDateString();
  }
```

Pass it (example is shortened, don't delete everything else).
Don't call the function here (don't use parantheses `()`), just pass it by name:

```jsx
<Food time={printTime}/>
```


Then finally invoke it in the child component either to display it in the return block, or use it for some calculation above that: 

```jsx
            {props.time}
```

> At the same time this also serves as an example that the name of the prop and the passed variable don't necessarily have to be the same!

#### Outputting multiple elements dynamically

There are various ways to create elementy dynamically, the most popular in React however is running the higher-order function `.map()` on them. [See another example of map from before here.](https://github.com/wsuf-teaching/class-notes/blob/main/frontend2/javascript-basics.md#map-the-method-not-the-data-structure)


Create a `mockdata` folder in `src`, then create a `foods.js` therein.

Add the following snippet into it:

<details>
    <summary>Food mock data (<i>click to expand</i>)</summary>

```js
const mockFoods = [
    {
        name: "Spaghetti",
        url: "https://www.bowlofdelicious.com/wp-content/uploads/2023/07/one-pot-spaghetti-with-meat-sauce-square-500x375.jpg",
        description: "Spaghetti is a long, thin, solid, cylindrical pasta. It is a staple food of traditional Italian cuisine.",
        price: 10
    },
    {
        name: "Fettuccine Alfredo",
        url: "https://www.modernhoney.com/wp-content/uploads/2018/08/Fettuccine-Alfredo-Recipe-1.jpg",
        description: "Fettuccine Alfredo is a pasta dish made from fettuccine pasta tossed with Parmesan cheese and butter.",
        price: 12
    },
    {
        name: "Penne Arrabiata",
        url: "https://www.saltandlavender.com/wp-content/uploads/2019/04/easy-pasta-arrabiata-recipe-1.jpg",
        description: "Penne Arrabiata is a spicy Italian pasta dish made with penne pasta, tomatoes, garlic, and red chili peppers.",
        price: 9
    },
];

export default mockFoods;
```

</details>


Also create a `FoodList` component inside `components`, and pass the `mockFoods` array to it from `App`. Feel free to delete the `printTime` function and any references to it from the application, we don't need that at this time.

App should look like this:

```jsx
import FoodList from "./components/FoodList";
import mockFoods from "./mockdata/foods";

function App() {

  const printTime = () => {
    return new Date().toDateString();
  }

  return (
    <div>
      Hello world!
      <FoodList foods={mockFoods}/>
    </div>
  );
}

export default App;
```

In the `FoodList` component, we are going to dynamically create `Food` elements based on the data array it receives.

Inside `FoodList` we map over the data array, and return an instance of `Food` for all of them:

```jsx
            {props.foods.map((food,i)=> 
                <Food data={food} key={i}/>
            )}
```

> Keys help React identify which items have changed, are added, or are removed. Keys should be given to the elements inside the array to give the elements a stable identity. In this example we use the map index for a key, but a better solution would be to use a uuid or element id from a database.

Finished, it should look like this:

```jsx
import Food from "./Food";

function FoodList(props) {

    return (
        <div>
            <h1>List of foods:</h1>
            {props.foods.map((food,i)=> 
                <Food data={food} key={i}/>
            )}
        </div>
    );
}

export default FoodList;
```
