## Preparations, small "bug" fixes

The initial list of foods should load immediately with only the images being borked.
Fix up the code in `FoodListItem.js` (`<img src={food.image_url} alt="food"/>`). If you want, change the image links to real ones in the DB.

A little further CSS fixes in `foodlist.css`. Replace the `.add-to-cart-col` and `.food-cart-col` block with the following:

```css
.add-to-cart-col {
    align-self: center;
    margin-right: 1em;
    display: flex;
    flex-direction: column;
}

/* ... */

.food-card-col {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 1em;
    flex-grow: 1;
}
```

Finally, in the cartModal, tidy things up a little bit:

```js
    const totalAmount = cartContext.totalAmount.toFixed(2);
    const totalAmountText = `€ ${totalAmount}`;

    /* ... */

    <span className={classes.totalAmount}>{totalAmountText}</span>
```

## Signing up

We will start the actual point of this class with implementing the sign up logic.
Let's grab the `SignupPage.js` and implement an even listener their for the form submission. To keep it simple, we will keep validation and the response display to minimal.

Pretty simple, really. We do not do anything here that we haven't already learned during web application development.

The changes in a nutshell:
- Add some refs to the form fields.
- Replace the hardcoded form action and method with a React handler function.
    - Grabs the submitted values and does some basic validation.
    - Creates the data to be sent to the back-end.
    - Sends the data, and checks the response.
    - Navigates back to the homepage if the call was successful using the react-router-dom library's navigate function.

```js
import { Link, useNavigate } from 'react-router-dom';
import './signin.css';
import { useRef } from 'react';

const SignupPage = () => {

    const navigate = useNavigate();
    const emailRef = useRef();
    const passwordRef = useRef();
    const passwordRepeatRef = useRef();

    const signupHandler = (e) => {
        e.preventDefault()
        console.log("Signup");

        const email = emailRef.current.value;
        const password = passwordRef.current.value;
        const passwordRepeat = passwordRepeatRef.current.value;

        if(password !== passwordRepeat) {
            alert('Passwords should match!')
            return;
        }

        let data = {
            'username': email,
            'password': password
        };

        console.log(data);

        fetch('http://localhost:5000/register', {
            method: 'POST',
            body: JSON.stringify(data)
        })
        .then(response => {
            console.log(response);
            if(!response.ok) {
                alert('Registration failed.');
                return;
            }
            navigate('/');
        });

      }

    return (
        <div class="body-wrapper">
            <section class="login-card">
                <img src={process.env.PUBLIC_URL + "/images/junkbanklogo.png"} class="logo" alt="logo"/>
                <h1>Sign up for JunkBank!</h1>
                <form class="form" onSubmit={signupHandler}>
                    <label for="email">
                        E-mail:
                    </label>
                    <input 
                        type="email" 
                        name="email" 
                        id="email" 
                        ref={emailRef}
                        required/>
                    <label for="password">
                        Password:
                    </label>
                    <input 
                        type="password" 
                        name="password" 
                        id="password" 
                        ref={passwordRef}
                        required/>
                    <label for="password-repeat">
                        Password repeat:
                    </label>
                    <input 
                        type="password" 
                        name="password_repeat" 
                        id="password-repeat" 
                        ref={passwordRepeatRef}
                        required/>
                    <button type="submit">Sign up</button>
                </form>
                <Link to="/login">Sign in instead</Link>
            </section>
        </div>
    );
}

export default SignupPage;
```

To persist login information, we need more. For ease of use, probably our best bet is to use a context object (or redux alternatively).

`auth-context.js`:

```js
import { createContext } from "react";

const AuthContext = createContext({
    token: null,
    login: (newToken) => {},
    logout: () => {},
    roles: [],
    isLoggedIn: false
});

export default AuthContext;
```

> Install the `jwt-decode` library through NPM: `npm i jwt-decode`.

`AuthProvider.js`:

```js
import react, {useState, useEffect} from "react";
import AuthContext from "./auth-context";
import { jwtDecode } from "jwt-decode";

const AuthProvider = props => {
  const [token, setToken] = useState(null);
  const [roles, setRoles] = useState([]);

  useEffect(() => {
    const storedToken = localStorage.getItem("token");
    if (storedToken) {
      setToken(storedToken);
      const decodedToken = jwtDecode(storedToken);
      setRoles(decodedToken.rls || []);
    }
  }, []);

  const authContext = {
    token: token,
    login: (newToken) => {
      setToken(newToken);
      if (newToken) {
        const decodedToken = jwtDecode(newToken);
        setRoles(decodedToken.rls || []);
      } else {
        setRoles([]);
      }
      localStorage.setItem("token", newToken);
    },
    logout: () => {
      localStorage.removeItem("token");
      setToken(null);
      setRoles([]);
    },
    roles: roles,
    isLoggedIn: !!token
  };

  return (
    <AuthContext.Provider value={authContext}>
      {props.children}
    </AuthContext.Provider>
  );
};

export default AuthProvider;
```

The `AuthProvider` component manages the authentication state using the `token` (storing the JWT token itself) and `roles` (storing roles available to the user to whom the token belongs to) variables.
Furthermore, the component provides logout functionality as well as a handy `isLoggedIn` support variable so the rest of the application can easily query the login status of a user.
Through the `useEffect` hook, the component can set up its state from the local storage if a JWT token is present there.
Finally, the component returns the provider to be used throughout the application.

Next, we add the provider in the root of the app in `index.js`:

```js
// ...
import AuthProvider from './context/AuthProvider';
// ...
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <AuthProvider>
        <CartProvider>
          <App/>
        </CartProvider>
      </AuthProvider>
    </BrowserRouter>
  </React.StrictMode>
);
```

Similarly to the signup component, the login component needs some modifications as well, however its responsibilities have a bigger scope.

Some highlights of the changes:
    - Creation of the signin POST request works pretty much the same way as the signup call.
    - The success check of the response is the same as well.
    - If the call was a success, the response object should contain the JWT token. Based on that, the `AuthProvider` sets up its inner state through the `login` function.
    - Otherwise, it resets itself (logging out, cleaning up its state).


```js
import { Link, useNavigate } from 'react-router-dom';
import './signin.css';
import { useRef, useContext } from 'react';
import AuthContext from '../context/auth-context';

const LoginPage = () => {

    const authContext = useContext(AuthContext);

    const navigate = useNavigate();

    const emailRef = useRef();
    const passwordRef = useRef();

    const signinHandler = (e) => {
        e.preventDefault();
        const email = emailRef.current.value;
        const password = passwordRef.current.value;
        let data = {
            'username': email,
            'password': password
        };

        fetch('http://localhost:5000/login', {
            method: 'POST',
            body: JSON.stringify(data)
        })
        .then(response => {
            console.log(response);
            if(!response.ok) {
                alert('Login failed.');
                return;
            }
            return response.json();
        })
        .then(response_text => {
            console.log(response_text.access_token);
            authContext.login(response_text.access_token);
            alert('login succ');
            navigate('/');
        })
        .catch(error => {
            authContext.logout();
        })

    }

    return (
        <div class="body-wrapper">
            <section class="login-card">
                <img src={process.env.PUBLIC_URL + "/images/junkbanklogo.png"} class="logo" alt="logo"/>
                <h1>Login to JunkBank!</h1>
                <form class="form" onSubmit={signinHandler}>
                    <label for="email">
                        E-mail:
                    </label>
                    <input 
                        type="email" 
                        name="email" 
                        id="email" 
                        ref={emailRef}
                        required/>
                    <label for="password">
                        Password:
                    </label>
                    <input 
                        type="password" 
                        name="password" 
                        id="password" 
                        ref={passwordRef}
                        required/>
                    <button type="submit">Log in</button>
                </form>
                <Link to="/signup">Sign up instead</Link>
            </section>
        </div>
    );
}

export default LoginPage;
```

With that set up, the login and logout mechanisms should be set.

Let's see this in action first in an existing component, then do a dummy page as well showing how it can be used to show or hide content from unauthorized users.

Grab the `Header.js` component, and import the provider:

```js
import AuthContext from "../context/auth-context";
```

Use it with the appropriate hook, and grab the needed properties and functions:

```js
    const {isLoggedIn, logout} = useContext(AuthContext);
```

Finally, between the "info" and the "cart" button, wrap the "login" and "signup" buttons as follows, so as to only display them when needed, similarly with the newly added "logout" button:

```js
{!isLoggedIn &&
<>
    <li className="item">
        <Link to="/login">Login</Link>
    </li>
    <li className="item">
        <Link to="/signup">Sign up</Link>
    </li>
</>
}
{isLoggedIn && 
    <li className="item">
        <a onClick={logout} style={{cursor:"pointer"}}>Logout</a>
    </li>
}
```

Let's also create a dummy page that will be protected both in the frontend, and the call it makes in the backend as well.

If the user is not logged in, it will be navigated back to the homepage. Otherwise, using the token from the context, it makes an authenticated call to a specific endpoint, and displays that data in the page.

```js
import { useContext, useEffect, useState } from 'react';
import AuthContext from '../context/auth-context.js';
import { useNavigate } from 'react-router-dom';

const SecretPage = () => {

    const [secret, setSecret] = useState(null);
    const authContext = useContext(AuthContext);
    const navigate = useNavigate();

    useEffect(()=>{
        if(!authContext.isLoggedIn) {
            navigate('/');
        }
    },[]);

    useEffect(()=>{
        if(authContext.token) {
            fetch("http://localhost:5000/adminonly",{
                headers: {
                    "Authorization": `Bearer ${authContext.token}`
                }
            })
            .then(response => {
                if(!response.ok) {
                    return;
                }
                return response.json();
            })
            .then(data => {
                setSecret(data.message);
            })
            .catch(error => console.log(error));
        }
    },[authContext.token]);


    return (
        <>
            <h1>Secret Page</h1>
            <p>The secret message is: {secret}</p>
        </>
    );
}

export default SecretPage;
```

Add the secret page to the router as well in the `App.js`:

```js
import SecretPage from './pages/SecretPage';

// ...

<Route path="/secret" element={<SecretPage/>}/>
```

> Technically, an option we can use is protecting the secret route through invoking the context in the router object.
> 
> ```js
> // ...
> import SecretPage from './pages/SecretPage';
> import { useContext } from 'react';
> import AuthContext from './context/auth-context';
> 
> // ... 
> function App() {
>   const {isLoggedIn} = useContext(AuthContext);
> 
> // ...
> 
>   return (
>     <>
>         <Routes>
>             <Route path="/" element={<MainPage/>}/>
>             <Route path="/login" element={<LoginPage/>}/>
>             <Route path="/signup" element={<SignupPage/>}/>
>             {isLoggedIn && <Route path="/secret" element={<SecretPage/>}/>}
>             <Route path="*" element={<img src="https://http.cat/404"></img>}/>
>         </Routes>
>     </>
> 
> // ...
> ```


As the last thing, implement the cart submission logic properly - now submitting real data to a backend system.

In `CartModal.js`, add the necessary imports, as well as grab the AuthContext inside the component:

```js
import AuthContext from '../context/auth-context';
```

```js
    const authContext = useContext(AuthContext);
```

And then finally edit the submission function as such:

```js
 const handleOrder = () => {
        const street = document.getElementById("street").value;
        const city = document.getElementById("city").value;
        const zip = document.getElementById("zip").value;

        if(street === "" || city === "" || zip === "") {
            window.alert("Please fill your address");
            return;
        }

        if(!authContext.isLoggedIn) {
            alert("You need to be logged in to submit your cart");
            return;
        }

        const newOrder = {
            street, 
            city, 
            zip,
            items: cartContext.items.map(item => ({
                id: item.id,
                amount: item.amount
            }))
        };

        console.log(newOrder);
        //alert("Your order was successful!");

        fetch('http://localhost:5000/order', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                "Authorization": `Bearer ${authContext.token}`
            },
            body: JSON.stringify(newOrder),
        })
        .then(response => {
            if (!response.ok) {
                alert("Submitting order failed");
                return;
            }
            return response.json();
        })
        .then(data => {
            alert("Submitting order was successful");
        })
        .catch(error => {
            alert("Submitting order failed");
        });


        cartContext.clearCart();
        props.onToggleModal();
    }
```

