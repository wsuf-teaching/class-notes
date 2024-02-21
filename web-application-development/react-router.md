### React Router

With React, we build single page applications (SPAs), but we can freely modify the content that gets displayed in the 
browser.
Even though we can modify the whole DOM, and for example conditionally display a "page" with only the "login" form, or
the "new food" form, it would still be the very same page. How can we send a link pointing to either of these features
to our friends?

Currently, no matter "where" in this app we would be, we would still see the same URL in the browser, therefore
we could only share a link to the starting page of a React application.

What we actually want is to have different URLs in our browser and "navigating" or "browsing" between them.
In traditional websites, each of these URL would point to a different html file. However once again, in React, we only
have one single page, one single index.html, and everything else is done in JavaScript side.

Luckily, we can still achieve this with a library called [React Router](https://reactrouter.com/en/main).
It provides a way to create an application in React with multiple views or pages, 
allowing users to navigate between them without a full page reload - and also to share links 
pointing to certain parts of it.

Still, we will only have a single actual HTML page. Instead of creating multiple HTML pages, we will create multiple
components corresponding to a "page", associate URLs to them and make React router seamlessly navigate between them.


Let's install it by running `npm i react-router-dom`.

#### Router, Routes, Route

Go to the `App.js` and import `Route` from react-router-dom.

```jsx
import { Route } from "react-router-dom";
```

This `Route` is actually a component too, which will have some special usage.
It should have a property called "path" - whatever we set to the path will be what React will listen to in the URL. 
Its other property should be "element" that will refer to the component that we want to display when visiting that specified URL.

For example the following snippet will display a big "Hello world!" text when we visit "http://localhost:3000/hello":

```jsx
<Route path="/hello" element={<h1>Hello!</h1>}/>
```

Of course this won't work yet, as a `Route` cannot be by itself, somewhere in the DOM structure, it needs to be wrapped with a `Routes`
component inside a `Router` component like `BrowserRouter`.

So the part in `App` should look like this:

```jsx
<Routes>
  <Route path="/hello" element={<h1>Hello!</h1>}/>
</Routes>
```

> There is also a `HashRouter` that uses hash links at the end of the URL (like http://localhost:3000#hello), but for "normal" website in browser purposes
> `BrowserRouter` works better with regular URL path segments.

And the part in `index.js` for example needs the following parts:

```jsx
import { BrowserRouter } from 'react-router-dom';
```

And the call in the render block:

```jsx
<BrowserRouter>
  <App/>
</BrowserRouter>
```

Now if we just visit our home page, we will see nothing, but then if we go to the "/hello" route, we will now see the "Hello world!" text,
but everything else as well. Why? Because React router controls the display of whatever is put into routes. Currently, if it matches
the "/hello" route, it will display the `<h1>` plugged in there. Pretty similar to what we are doing with checking whether the `foods` array
is empty or not and displaying different components accordingly.

To truly control what gets displayed, all content should be plugged into routes one way or another.
Let's create a folder called `pages` - the name is only for us, they are still just regular components that we know all too well.

Create `Hello.js`:

```jsx
function Hello() {
    return (
        <h1>Hello</h1>
    );
}

export default Hello;
```

Now in the `App`, we need to import this

```jsx
import Hello from './pages/Hello';
```

before using inside the routes block:

```jsx
<Routes>
  <Route path="/hello" element={<Hello/>}/>
</Routes>
```

Now let's continue with the `Login` component.
Move `Login.js` and `Login.module.css` over to the `pages` folder.

> Don't forget to fix the imports accordingly! If you drag and drop them, VS Code should offer to fix them. Accept it. Otherwise, you can always do it manually.

To make stuff a little nicer, move the `Card` wrapping the `Login` inside the `Login` component wrapping all its contents.

It should look similar to this:

```jsx
    return (
        <Card>
            <form className={styles....
            {/* ... */ }
            </form>
        </Card>
    );
}
```

And finally create a new `Route` for it:

```jsx
<Routes>
  <Route path="/hello" element={<Hello/>}/>
  <Route path="/login" element={<Login/>}/>
</Routes>
```

Finally, let's just wrap the rest of the `App` component in one final page component called `Home`.
Create `Home.js` in the pages folder that will contain most logic that `App` has currently:

```jsx
import React, { useState, useEffect } from 'react';
import FoodList from '../components/FoodList';
import NewFood from '../components/NewFood';
import Card from '../components/Card';

function Home() {
  const [title, setTitle] = useState("Food!");
  const [foods, setFoods] = useState();

  const handleButtonClick = (param) => {
    alert("You clicked me. " + param);
  };

  const handleChangeTitle = () => {
    setTitle("Order food!");
  };

  const addFoodHandler = () => {
    const newFood = {
      name: "Pizza",
      url: "https://www.mindmegette.hu/images/388/Social/lead_Social_pizza-alap-recept.jpg",
      description:
        "Pizza is a dish of Italian origin consisting of a usually round, flat base of leavened wheat-based dough.",
      price: 8,
    };
    const newFoods = [...foods, newFood];
    setFoods(newFoods);
  };

  const addNewFoodHandler = (newFood) => {
    setFoods([...foods, newFood]);
  };

  useEffect(() => {
    fetch("http://127.0.0.1:5000/foods")
      .then((response) => response.json())
      .then((data) => setFoods(data))
      .catch((error) => console.log(error));
  }, []);


  return (
    <>
      {/* <Welcome borderWeight={3}>
        Food list is <span>working</span>
        </Welcome> */}
      <h1 style={{ textAlign: "center" }}>{title}</h1>

      <Card>
        <NewFood onAddNewFood={addNewFoodHandler} />
      </Card>
      <button onClick={handleButtonClick.bind(null, "Hello")}>Click me</button>
      <button onClick={handleChangeTitle}>Change title</button>
      <button onClick={addFoodHandler}>Add food</button>
      {foods ? <FoodList foods={foods} /> : <h4>Loading...</h4>}
    </>
  );
}

export default Home;
```

Create a new route for this as well. But not a "regular" route, but the "home" route, that is indicated by just one slash that
the application and the router will default to: "/". Alternative is to use the `index` keyword.

Doing all these changes and moving out the `Home` contents, now `App.js` will look a lot leaner:

```jsx
import { Route, Routes } from "react-router-dom";
import Login from './pages/Login';
import Hello from './pages/Hello';
import Home from './pages/Home';

function App() {

  return (
    <div className='container'>
      <Routes>
        <Route index element={<Home/>}/>
        <Route path="/hello" element={<Hello/>}/>
        <Route path="/login" element={<Login/>}/>
      </Routes>
    </div>
  );

}

export default App;
```

#### Catch all route

React Router can also listen to "any other" requests by specifying a path pointing to "*". Anything entered to the URL path that was not 
caught by another route before it will be handled by this route.

```jsx
<Route path="*" element={<h1>404 Page not found</h1>} />
```

#### Links

Of course, typing something in the URL should not be the only way to navigate between pages.
If we type a new URL then press enter, the whole React application will reload, losing our states we might have set up already.
Similar situation happens when we try to make an "anchor" link to a route we have defined. For example add these into the `App` component, directly
above and outside the `Routes`:

```jsx
<ul>
    <li><a href="./hello">Hello</a></li>
    <li><a href="./login">Login</a></li>
    <li><a href="./">Home</a></li>
</ul>
```

The way to do this instead is to use `<Link>`s.
They of course have to be imported from `react-router-dom`, making the import in `App` look like as follows:

```jsx
import { Link, Route, Routes } from "react-router-dom";
```

Finally, instead of "`a href`", we will use "`Link to`". Using `Link`s this way will preserve the navigation functionality, but 
also will prevent the browser from navigating to new pages. Instead, React will manipulate the content accordingly to simulate
navigating to a different pages accordingly.

```jsx
<ul>
    <li><Link to="/hello">Hello</Link></li>
    <li><Link to="/login">Login</Link></li>
    <li><Link to="/">Home</Link></li>
</ul>
```

#### Layout components

> Currently we have the links available to all pages. Including for example the 404 error page.
> We cannot easily "remove" them, as the links are now outside of the `Routes` block, so they will be present at every page no matter what.
> If we don't want to make the navigation menu available there, one option we can take is to create a "Navigation" or "Layout" component
> that will wrap every other element/page, aside from where we don't want the menu to be present.

Create a new component called `Layout`:

```jsx
import {Link} from "react-router-dom";

function Layout(props) {
    return (
        <>
            <ul>
                <li><Link to="/hello">Hello</Link></li>
                <li><Link to="/mylogin">Login</Link></li>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/second">Second page</Link></li>
            </ul>
            {props.children}
        </>
    )
}

export default Layout;
```

Then wrap all other pages with it.
For example:
```jsx
        <Route path="/second" element={<Layout><h1>This is the second part!</h1></Layout>}></Route>
```

and

```jsx
import Layout from "../components/Layout";

function Hello() {
    return (
        <Layout>
            <h1>Hello</h1>
        </Layout>
    );
}

export default Hello;
```

and so on....

Remember to include that new component to prevent errors.



