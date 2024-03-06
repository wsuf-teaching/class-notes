# React Context

The last piece of the puzzle so far is React Context.

React Context provides a way to pass values like props between components without explicitly passing them through each level of the component tree. 
It allows us to create a global state that can be accessed by (any) component within the tree, making it particularly useful for managing state in large applications.

A Context usually consists of a context provider and a context consumer.

We can create a very simple context like this:

```jsx
const MyContext = React.createContext();
```

Then, this needs to be used in the JSX block with some specified values:

```jsx
  <MyContext.Provider value={{ /* your values here */ }}>
    {/* children components here */}
  </MyContext.Provider>
```

And also export is:

```jsx
export default MyContext;
```

After it is declared, the values would be able to be retrieved in any child component using the `useContext` hook.

```jsx
import React, { useContext } from 'react';
import MyContext from "./WHERE-YOUR-CONTEXT-IS";

// .....

const contextValue = useContext(MyContext);
```

Let's first see an example of this.

## Example 1

Declare a context called `TestContext`.
If we want to make it available to any pages, it have to be added around the Router. Either in the `App.js` wrapping the Routes block, or in the `index.js` should suffice.
Let's do the latter.

```jsx
const TestContext = React.createContext();

root.render(
  <TestContext.Provider value={{ meaningOfLife: 42 }}>
    <BrowserRouter>
        <App/>
    </BrowserRouter>
  </TestContext.Provider>
);

export default TestContext;
```

Then, if we want to retrieve its value or value - at any component or page, all we have to do is import the useContext hook, as well as the declared context.
For example inside `Hello.js`:

```jsx
import { useContext } from 'react';
import TestContext from "../index";
```

Then use it inside the component:

```jsx
function Hello() {

    const contextValue = useContext(TestContext);
    console.log(contextValue);
    console.log(contextValue.meaningOfLife);

    // ...
```

## Example 2

Now in the second example, make a little bigger context holding items we might add to a shopping cart.

First, let's set up a few things:

Make the `Food.js` component use state for handling its internal state, and add a "+" button to it as well as an event listener listening to a click to that.

```jsx
import { useState } from 'react';
import styles from './Food.module.css';

function Food(props) {   // display component

    const [food, setFood] = useState(props.data);

    let sale;
    if( food.price<10 ) {
        sale = <div className={styles.sale}>SALE!</div>;
    }

    const addToCartHandler = (event) => {
        console.log(food);
        // ... add to context here ...
    }

    return (
        <div className={styles.food}>
            <h2 className={styles.name}>{food.name.toUpperCase()}</h2>
            <img className={styles.image} src={food.url}></img>
            <p>{food.description}</p>
            {sale}
            <h4 className={`${styles.price} ${food.price<10 ? styles.red : styles.black}`}>Price: ${food.price}</h4>
            <button onClick={addToCartHandler}>+</button>
        </div>
    );
}

export default Food;
```

Then, instead of just shoving the context inside one of our tiny little components, let's make a proper place for it. 
Create a new folder called `context` in the `src` folder.
Inside that, create a new file called `cart-context.js`.

In that, just as we did before, create a new context with `React.createContext()`.
What is between the parentheses is the data we want to put into the context. Simple variables, objects, even functions.

```jsx
import React from "react";

const CartContext = React.createContext({
    cart: [{}],
    addToCart: () => {},
    clearCart: () => {},
});

export default CartContext;
```

In this example, I want to have a "cart" object holding an array of objects, as well as two functions. One to add a new element to the 
cart and one to clear it.

Afterward, we need an actual react component that will hook into it, that will provide this context to the rest of the application.
We can do that either here in place, or in a separate file:

```jsx
import { useState } from "react";
import CartContext from "./cart-context";

export const CartContextProvider = props => {
    return (
        <CartContext.Provider>
            {props.children}
        </CartContext.Provider>
    );
};

export default CartContextProvider;
```

Now the `CartContextProvider` is a real React component. And as it is a real component, we can use state,
or declare functions (interacting with each other) therein.

Put both snippets before the return JSX block:

```jsx
const [cartState, setCartState] = useState([]);

const addToCartHandler = (newElement) => {
    setCartState((cartState)=>[...cartState, newElement]);
}

const clearCartHandler = () => {
    setCartState([]);
}
```

Then, these need to be bunched up into a "context" object:

```jsx
const cartContext = {
    cart: cartState,
    addToCart: addToCartHandler,
    clearCart: clearCartHandler
};
```

And finally passed into the `CartContext.Provider` as the `value` prop.

```jsx
<CartContext.Provider value={cartContext}>
```

Then make it available globally, in `index.js` for example. Don't forget to import it.

```jsx
root.render(
  <TestContext.Provider value={{ meaningOfLife: 42 }}>
    <CartContextProvider>
      <BrowserRouter>
          <App/>
      </BrowserRouter>
    </CartContextProvider>
  </TestContext.Provider>
);
```



In the components where we want to use it, import the `useContext` hook as well as the `CartContext` in the food component: 

```jsx
import { useState, useContext } from 'react';

import CartContext from '../context/cart-context';
```

And use the context inside the component:

```jsx
    const ctx = useContext(CartContext);
```

Calling its `addToCart` method, we can add food to the context that will be available in the application until it is running.
So until a reload or closing of the tab.

```jsx
const addToCartHandler = (event) => {
    console.log(food);
    ctx.addToCart({name: food.name, price: food.price});
}
```

Next, let's create a component or rather a page that will display our cart. Create `Cart.js` inside the `pages` folder.
Its contents should look as follows:

```jsx
function Cart () {
    return (
        <h1>Cart works!</h1>
    );
}

export default Cart;
```

Also in `Layout.js`, add a new link to it: 

```jsx
<li><NavLink to="/cart" style={customNavLinkStyle}>Cart</NavLink></li>
```

And in `App.js`, declare the route for it:

```jsx
<Route path="/cart" element={<Cart/>}/>
```

Don't forget to include the component in both cases.

Our only job in the `Cart` is to retrieve the context, map over the array in the context and display the items.

```jsx
import { useContext } from 'react';
import CartContext from '../context/cart-context';

function Cart () {

    const ctx = useContext(CartContext);

    const cartItems = ctx.cart.map((item,index) => (
        <div key={index} style={{border:"1px solid red", margin: "10px"}}>
            {item.name}, {item.price}
        </div>
    ));

    return (
        <>
            <h1>Cart works!</h1>
            {cartItems}
        </>
    );
}

export default Cart;
```



As a final exercise, let's add a `cartSum` variable to the context, and to the context's state that at any given time
would hold the sum of all the item's prices it has.

`cart-context.js`:

```jsx
const CartContext = React.createContext({
    cart: [{}],
    sum: 0,
    addToCart: (newElement) => {},
    clearCart: () => {},
});
```

Next when updating the ContextProvider, we would have a problem though. If the `sum` were to have its own state, 
we would need to set both that state, and the cart state. Naively, the functions would look something like this:


```jsx
    const [cartState, setCartState] = useState([]);
    const [cartSum, setCartSum] = useState(0);

    const addToCartHandler = (newElement) => {
        setCartState((cartState)=>[...cartState, newElement]);
        setCartSum(cartState.reduce((sum, item) => sum + item.price, 0));
    }

    const clearCartHandler = () => {
        setCartState([]);
        setCartSum(0);
    }

    const cartContext = {
        cart: cartState,
        sum: cartSum,
        addToCart: addToCartHandler,
        clearCart: clearCartHandler
    };
```

However, we will quickly notice that it will not work. Why? Because we try to set both states "at the same time". Therefore,
the second will lag behind.

Another hook, and "paradigm" to do contexts comes to the rescue. `useReducer`!

To that end, it might be even better to rewrite the `CartContextProvider` from the ground up than trying to edit it:

Do the necessary imports:

```jsx
import { useReducer } from "react";
import CartContext from "./cart-context";
```

Set a simple JS const `defaultCartState` (outside of any potential components).

```jsx
const defaultCartState = {
    cart: [],
    sum: 0,
};
```

Next, the `cartReducer` is a function that takes the current state (state) and an action (action) as parameters. 
Depending on the action type, it returns a new state for every "state" we use it for. 

```jsx
const cartReducer = (state, action) => {
};
```

In the case of `ADD` it adds the new item to the cart and updates the sum. 
For `CLEAR` it resets the cart and the sum. Either by manually or by simply returning the `defaultCartState`.
The default case ensures that if an unknown action type is provided, it returns the current state unchanged.

```jsx
const cartReducer = (state, action) => {
    switch (action.type) {
        case "ADD":
            return {
                ...state,
                cart: [...state.cart, action.item],
                sum: state.sum + action.item.price
            };
        case "CLEAR":
            // return {
            //     ...state,
            //     cart: [],
            //     sum: 0
            // };
            return defaultCartState;
        default:
            return state;
    }
};
```

Following this, we redeclare the `CartContextProvider`. It uses the `useReducer` hook, and the reducer is initialised
with the `cartReducer` function declared just above, as well as with the `defaultCartState`:

```jsx
export const CartContextProvider = (props) => {
    const [cartState, dispatch] = useReducer(cartReducer, defaultCartState);
    
    // ... the code continues ...
```

Then, the "action handlers" are declared, dispatching actions with the types defined above in the reducer (`ADD`,`CLEAR`):

```jsx
    const addToCartHandler = (newElement) => {
        dispatch({ type: "ADD", item: newElement });
    };

    const clearCartHandler = () => {
        dispatch({ type: "CLEAR" });
    };
    
    // ... the code continues ...
```


Finally, we create the context, and pass it as `value` to the `CartContext.Provider` and export the component.

```jsx
    const cartContext = {
        cart: cartState.cart,
        sum: cartState.sum,
        addToCart: addToCartHandler,
        clearCart: clearCartHandler,
    };

    return (
        <CartContext.Provider value={cartContext}>
            {props.children}
        </CartContext.Provider>
    );
};
```

And very last, let's also use the clear cart functionality we have in the `Cart` component:

```jsx
    const clearCartHandler = () => {
        ctx.clearCart();
    }
```

And in the return block:

```jsx
<button onClick={clearCartHandler}>Clear cart!</button>
```


> An alternative to React Context is [Redux](https://redux.js.org/)