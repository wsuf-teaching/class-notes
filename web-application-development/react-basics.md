

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

> Keys help React identify which items have changed, are added, or are removed. 
> Keys should be given to the elements inside the array to give the elements a stable identity. 
> In this example we use the map index for a key, but a better solution would be to use a uuid or element id from a database.
> Even though `key` looks like a prop, it is not. If we want to use that value inside the component, we have to manually
> add it as a prop (with a different name) as well.

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

Alternatively, the mapping part can also happen beforehand saving the created element into a variable.
In that case, `FoodList` will look like as follows:

```jsx
import Food from "./Food";

function FoodList(props) {

    const foodElements = props.foods.map((food,i) => 
        <Food data={food} key={i}/>
    );

    return (
        <div>
            <h1>List of foods:</h1>
            {foodElements}
        </div>
    );
}

export default FoodList;
```

#### Fragments

One thing that was quickly skipped over previously in the `App` component is having multiple "top-level" elements in a React component.
Hence the `<FoodList ...>` component was put into the div in `App` like in the example below: 

```jsx
  return (
    <div>
      Hello world!
      <FoodList foods={mockFoods}/>
    </div>
  );
```

Why is that? Couldn't we just put it below the `<div>`? Well, we cannot "just" put it there.

If we were to try this (don't try it, it will not work, promise!):

```jsx
  return (
    <div>
      Hello world!
    </div>
    <FoodList foods={mockFoods}/>
  );
```

even the IDE would scream at us, just like the browser would also throw an error stating something alone the lines of "`Adjacent JSX elements must be wrapped in an enclosing tag.`".

That's right, a React component can only have one "top-level" element.

Good news, that there are various strategies around this:

1. Using a container element. Just as we had before. Wrap the contents of the component with a single JSX element, like a `<div>`. This would work in almost all of the cases, it is not optimal as it needlessly introduces additional elements in the DOM.

2. Introduce higher-order components to wrap other components. This will use the "child" prop, more about that in a little while.

3. Wrap elements in a "React fragment" (`<React.Fragment>`, or `<>` and `</>`). This wrapps the adjacent JSX elements without introducing an extra DOM node.

```jsx
  return (
    <React.fragment>
      <div>
        Hello world!
      </div>
      <FoodList foods={mockFoods}/>
    </React.fragment>
  );
```

or

```jsx
  return (
    <>
      <div>
        Hello world!
      </div>
      <FoodList foods={mockFoods}/>
    </>
  );
```

> For the former example, you might need to import React in the .js file! (`import React from "react";`)

#### Conditional rendering

We have seen above, how we can run JavaScript code in the JSX block inbetween curly braces (`{}`). Using that, we can easily wrap parts of the JSX blocks in conditionals, thus rendering conditionally.

One of the ways to do it is usng element variables, creating a variable holding the JSX element conditionally, then adding that to the return statement.


Edit `Food.js` as such:

```jsx
function Food(props) {

    let sale;
    if( props.data.price<10 ) {
        sale = <div id="sale">SALE!</div>;
    }

    return (
        <div className="food">
            <h2>{props.data.name.toUpperCase()}</h2>
            <img src={props.data.url}></img>
            <p>{props.data.description}</p>
            {sale}
            <h4>Price: ${props.data.price}</h4>
        </div>
    );
}

export default Food;
```

First, pased on the condition we create variable holding the `<div>`, then simply use it in the JSX block.

The other method uses a shorter "inline" syntax inside the returned JSX block to achieve the same:

```jsx
    return (
        <div className="food">
            <h2>{props.data.name.toUpperCase()}</h2>
            <img src={props.data.url}></img>
            <p>{props.data.description}</p>
            {props.data.price < 10 && 
                <div id="sale">SALE!</div>
            }
            <h4>Price: ${props.data.price}</h4>
        </div>
    );
```

#### Children prop

So far, every custom component of ours were self-closing. `<FoodList foods={mockFoods}/>`, `<Food data={food}/>` and even `<App/>`.

That is not to say this is our only option. Similar to default JSX elements, like `<h2>` or `<div>`, "wrapper" components can easily be made that take "children" between their opening and closing tags.

To make the next example look a little better, remove the `border: 2px solid red; margin:auto; max-width:900px;` styles in `index.css` from the `.food` style.

Let's make a new component called `Card`.

```jsx
function Card() {
    return (
        <div className="card">
        </div>
    );
}

export default Card;
```

Also add some nice styling to this Card in `index.css`.

```css
.card {
  border: 1px solid black;
  border-radius: 15px;
  box-shadow: 0px 3px 3px 0px rgba(0,0,0,0.1);
  max-width: 900px;
  margin: 15px auto; 
}
```

Now the changes that we need to do is wrap the individual `Food` elements with the `Card` component in `FoodList`. 

> Notice, how the `key` prop got moved to the `Card` here.

```jsx
    return (
        <div>
            <h1>List of foods:</h1>
            {props.foods.map((food,i)=>
                <Card key={i}>
                    <Food data={food} />
                </Card> 
            )}
        </div>
    );
```

Finally, the `Card` component should take `props` parameter and have `{props.children}` inbetween its opening and closing `<div>` tags.

```jsx
function Card(props) {
    return (
        <div className="card">
            {props.children}
        </div>
    );
}
```

Now we have a `Card` component that can be reused not just for displaying foods in a list, but everywhere, as it can wrap-around anything.

#### Styling

Let's look at styles and CSS in React, let's see a few of the options we have to make the web application look nice.

##### 1. Inline styles
Inline styles. Once again the syntax is a little different, but not much. Inline styles have to be put between double curly braces just like other
JavaScript code in the JSX block, and then we have to use the camel case version of the style properties.
For example `<h1 style={{ textAlign: 'center' }}>Food list is working!</h1>` in the `FoodList.js` component.
For multiple styles, separate them with comma signs (`,`): `{{textAlign:'center', color:'blue'}}`

##### Setting styles properties dynamically

Styles, just like JSX elements can be added dynamically and conditionally. Consider the following example in `Food.js`:

```jsx
    <h4 style={{color: props.data.price<10 ? 'red' : 'black'}}>
```

If the price is lower than 10, the `<h4>` displaying it should be red, otherwise black. 

> The conditional (ternary) operator is the only JavaScript operator that takes three operands: 
> a condition followed by a question mark (?), 
> then an expression to execute if the condition is truthy followed by a colon (:), 
> and finally the expression to execute if the condition is falsy. 
> This operator is frequently used as an alternative to an if...else statement.
> [source: MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator)

Other small example we can do is displaying every second `Card` component in a slightly different gray-ish colour.
For that, first pass the `i` from the `map` in `FoodList` as a prop named `index`, then use it in the JSX block:

```jsx
    {/* ... */}
    <Card key={i} index={i}>
    {/* ... */}
```

```jsx
    <div className="card" style={{backgroundColor: props.index%2 ? 'white':'lightgray'}}>
```

> Consider if we have multiple of these conditional styles in an element, using classes (classNames) should be way easier 
> than adding the same condition check before each style property.

 
##### 2. Regular class names and css files

Simply using regular class names as we did it so far (a single `index.css`). While it works, it is not the most elegant solution.
It suffers from the same problem as any prior application throughout the semester of us having to keep track of all the CSS ids and class names
in the global scope.
> Remember, instead of `class`, they keyword `className` should be used in React.

Of course one option is to create numerous smaller CSS files.
Let's for example create a `Food.css` and put it right next to `Food.js` then grab all the relevant CSS from `index.css` and put it in there.
Link it by simply importing it as such: `import './Food.css';`.
However, while this may split the CSS into smaller and more manageable pieces, in the end all of the individual styles are still applied
globally to all elements; so if we were to have a different component with the class `food` on it, these styles would take
effect on that as well - and anything else applicable in the application globally.

##### Setting CSS classes dynamically

Combining the previous two approaches leads to slightly better results. We make CSS classes in our `.css` files and apply those dynamically
instead of applying inlined CSS styles.

Add the two background-colors as their own CSS classes, maybe into a newly created `Card.css` which of course needs to also be imported now:

```js
import './Card.css';
```

```css
.whiteBg {
  background-color: white;
}

.grayBg {
  background-color: lightgray;
}
```

Now, the className syntax becomes a little weird, but logically it is simply a javascript block inside JSX with string interpolation inside.

```jsx
        <div className={`card ${props.index%2 ? 'whiteBg' : 'grayBg'}`}>
```

It can maybe be further simplified by moving the expression out of the return block and only needing the gray background
if it is an odd element making the component look like as such:

```jsx
import './Card.css';

function Card(props) {

    const everySecond = props.index%2;

    return (
        <div className={`card ${everySecond ? 'grayBg' : 'whiteBg'}`}>
            {props.children}
        </div>
    );
}

export default Card;
```

##### 3. Styled components

Styled Components is a popular library for React that allows us to write CSS directly within 
the JavaScript code using tagged template literals. Basically components with certain styles attached to them from the start, and of course
those styles only affecting that specific component they were attached to.

To get started, the package has to be installed first:

```
npm install --save styled-components
```

For this example, look at `FoodList`. The `<h1>` inside it has some inline styles. Let's make that a styled component instead.
Maybe name the new file and component `Welcome.js`, as that explains what it does pretty well.

First just create a regular component from it, then it will be converted into a styled component step by step.
Cut it from FoodList, replacing it with `<Welcome>Food list is working</Welcome>`. Also add the required import (`import Welcome from './Welcome';`) and it is done.

```jsx

function Welcome() {
    return (
        <h1 style={{textAlign:'center', color:'blue'}}>Food list is working!</h1>
    );
}

export default Welcome;
```

After confirming that it works, comment the function out right away.
First import styled components (`import styled from 'styled-component';`), then let's get started.

```js
const Welcome  = styled.h1`
`;
```

> Now this is a super weird syntax, yes. It is called `tagged string literal` 
> and you can read more about them [for example here](https://wesbos.com/tagged-template-literals).

> Basically what this tagged string literal feature does is allowing us to process template literals with a function, known
> as the "tag" function. This "tag" function takes an array containing the string literals from the template, as well as
> an array containing the evaluated expressions. Then it can manipulate these parts as needed and return a modified or completely new string.

> In case a styled component we only have to care about the syntax, but below in the dropdown you can find a quick example
> of how these can work in practice otherwise:

<details>
    <summary>(<i>click to expand</i>)</summary>

```js
    function myTagFunction(strings, ...values) {
    // strings: an array of string literals
    // values: an array of evaluated expressions
    
    // Use map to apply custom logic to each evaluated expression
    const modifiedValues = values.map(value => {
    // If the value is a number, square it; otherwise, leave it unchanged
    return typeof value === 'number' ? value * value : value;
    });
    
    // Combine the modified values with the original string literals
    const result = strings.reduce((acc, str, index) => {
    // Append the modified value and the corresponding string literal
    return acc + str + (index < values.length ? modifiedValues[index] : '');
    }, '');
    
    return result;
    }
    
    const variable = 5;
    const result = myTagFunction`The square of ${variable} is ${variable * variable}.`;
    
    console.log(result);
```
</details>

So summing it up and applying it in our case: `styled.h1` is just a method, into which we pass
some parameters in a special syntax/way between the backticks (&#96;).
In the end, it will return a `h1`, with the styles we provide as parameters included.

Inside the backticks, we add the styles. Any styles added there will directly affect the component it is added to.

Classes, pseudo-classes or nested classes can be added onto an element by prefixing them by the and sign (`&`)
instead of using a class name, tag name or an id.

For example, the new styled component can look like as follows:

```js
const Welcome  = styled.h1`
    text-align: center;
    color: blue;

    &:hover {
        background-color: lightblue;
    }
`;
```

> Styled components automatically forward all children props!

Styled components are especially useful in creating small bits of the web application with certain non-clashing styles.
They cannot however "directly" take logic like regular React components, making them ideal for "dumb" display
components or for creating layouts.
At best what they take are default event listeners like `onClick` and such.
Custom props can also be sent to it making the styled component dynamically configurable. For example:

```jsx
const Welcome  = styled.h1`
    text-align: center;
    color: blue;
    border: ${props => props.borderWeight}px solid blue;

    &:hover {
        background-color: yellow;
    }
`;
```

and passing it as usual:

```jsx
<Welcome borderWeight={3}>Food list is working</Welcome>
```

Configuring child elements with styles can be done like the following snippets.
Notice the `<span>` put inside it!

```jsx
    <Welcome borderWeight={3}>
        Food list is <span>working</span>
    </Welcome>
```

With the required CSS inside the styled tagged template literal:

```
    /* ...... */
    & span {
        background-color: red;
    }
```

Media queries can also be added in styled components with the usual syntax:

```
    @media (max-width: 600px) {
        background-color: aqua;
    }
```

> Inspect the created element in the browser. What you should see is something like this: `<h1 borderweight="3" class="sc-beySPh crzoKt">Food list is <span>working</span></h1>`
> Notice the gibberish text in the class list. These are automatically generated classes ensuring no style applied on a styled component spams the global namespace.


#### 4. CSS modules

One another very popular method to prevent global styling conflicts and providing a way to locally scope styles are CSS modules.
Using them involves just a few steps.

To have a better example, let's first convert all the styles in `Food.css` and `Food.js` to use their own classes.

It should look like this, replacing them with very common names (that would otherwise almost surely cause global styling conflicts):

```css
.food {
  padding: 10px; 
  display: flex;
  min-height: 150px;
}
  
.name {
  min-width: 170px;
}
  
.price {
  min-width: 100px;
}

.food * {
  margin: 5px;
}

.image {
  width: 100px;
  object-fit: cover;
}

.sale {
  background-color: salmon;
  color: white;
  align-self: center;
}
```

At the same time, make the js file use them:

```jsx
    let sale;
    if( props.data.price<10 ) {
        sale = <div className="sale">SALE!</div>;
    }
    
    return (
        <div className="food">
            <h2 className="name">{props.data.name.toUpperCase()}</h2>
            <img className="image" src={props.data.url}></img>
            <p>{props.data.description}</p>
            {sale}
            <h4 className="price" style={{color: props.data.price<10 ? 'red' : 'black'}}>Price: ${props.data.price}</h4>
        </div>
    );
```

With that, we should be back where we started, just using regular CSS classes.

Now, onto CSS modules.
1. Rename `Food.css` to `Food.module.css`.
2. Change the CSS import from `import './Food.css';` to `import styles from './Food.module.css';`.
3. Lastly, replace the `className="myclass"` properties with the `className={styles.myclass}` syntax.

It should look like this:

```jsx
    let sale;
    if( props.data.price<10 ) {
        sale = <div className={styles.sale}>SALE!</div>;
    }

    return (
        <div className={styles.food}>
            <h2 className={styles.name}>{props.data.name.toUpperCase()}</h2>
            <img className={styles.image} src={props.data.url}></img>
            <p>{props.data.description}</p>
            {sale}
            <h4 className={`${styles.price} ${props.data.price<10 ? styles.red : styles.black}`}>Price: ${props.data.price}</h4>
        </div>
    );
```

> Once again, notice how the final HTML will look like in the browser, with all the class names replaced with a new classname adhering to the "ComponentName-classname-uuid" format ensuring
> no global styling conflicts. All classes declared in a `*.module.css` can be safely reused in other parts of the application.
> 
> ```html 
> <div class="Food_food__iXK1m">
>   <h2 class="Food_name__CwBzd">SPAGHETTI</h2>
>   <img class="Food_image__jWq5u" src=".....">
>   <p>Spaghetti is a long, thin, solid.....</p>
>   <h4 class="Food_price__5+LR-" style="color: black;">Price: $10</h4>
> </div>
> ```

To finish up this file, also make a red and black class with the respective text colours assigned.

```css
.red {
  color: red;
}

.black {
  color: black;
}
```

And modify the bottom `<h4>`s className as follows:

```jsx
<h4 className={`${styles.price} ${props.data.price<10 ? styles.red : styles.black}`}>Price: ${props.data.price}</h4>
```

> For class names with dashes (`-`) in them, you have to use the bracket notation: `className={styles['class-name']}`

> The extra complication in this syntax (having to use emplate literals) is caused by us having to execute a JavaScript statement in the class block to determine the text color/style that should be used.
 
#### Afterword

The course continues in the [React intermediate](react-basics-p2.md) notes.

There is one small change I would like to do beforehand. Move the `<Welcome>` component from the `<FoodList>` down to `<App>`.