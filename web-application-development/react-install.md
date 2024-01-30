React is a popular JavaScript library for building user interfaces, particularly for building single-page applications where user interactions are dynamic and data changes frequently.

React uses a component-based architecture where everything is built by components, reusable self-contained units that encapsulate a specific piece of the user interface.
It also uses a declarative syntax allowing developers to describe how the UI should look based on the current application state. This is in contrast to imperative programming, where developers would explicitly specify the steps to achieve a particular outcome.


## Installation

There are numerous ways how we can start up a react application.

### Using CDN links

In this version, we simply import the required packages in our .html file, then use React in the .js files starting with `App.js` for example.

```html
<html>
    <head>
        <link rel="stylesheet" href="index.css">
        <script crossorigin src="https://unpkg.com/react@18/umd/react.development.js"></script>
        <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
        <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
    </head>
    <body>
        <div id="root"></div>
        <script src="App.js" type="text/babel"></script>
    </body>
</html>
```

```jsx
ReactDOM.createRoot(document.getElementById('root')).render(<h1>Hello world!</h1>);
```

Now, just use Live server in VS Code to run this very small react application.

### Using a (custom) webpack project

Using this package.json, install it (`npm install`), and create index.html and App.js in the src folder:

```json
{
  "name": "react-starter",
  "version": "1.0.0",
  "description": "",
  "main": "App.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "lint": "eslint \"src/**/*.{js,jsx}\" --quiet",
    "stylelint": "stylelint ./src/**/*.css",
    "dev": "parcel ./src/index.html --open",
    "format": "prettier --write \"src/**/*.{js,jsx}\""
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "eslint": "^8.29.0",
    "eslint-config-prettier": "^8.5.0",
    "eslint-plugin-import": "^2.26.0",
    "eslint-plugin-jsx-a11y": "^6.6.1",
    "eslint-plugin-prettier": "^4.2.1",
    "eslint-plugin-react": "^7.31.11",
    "parcel": "^2.8.0",
    "prettier": "^2.8.0",
    "process": "^0.11.10",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "stylelint": "^14.16.0"
  }
}
```

In this case, the HTML file will become simpler, without all the imports:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="./style.css" />
    <title>Document</title>
  </head>
  <body>
    <div id="root">not rendered</div>
    <script type="module" src="App.js"></script>
  </body>
</html>
```

```javascript
import { createRoot } from 'react-dom/client';
import React from 'react';


createRoot(document.getElementById('root')).render(<h1>Hello world!</h1>);
```

The structure should look like this after installing the package file:

![f](https://i.imgur.com/XuTJSom.png)

### Create-react-app

Lastly, the third option is to use `create-react-app`. Probably the most straightforward option, but may also set up many (for now) unneeded things as well.

Install create-react-app globally.
```
npm install -g create-react-app
```

Afterwards you can execute `npx create-react-app my-app` - where "my-app" is the name you would like to give to your new application - anywhere on your system.

> Alternatively, `npm init react-app my-app` should also work.

Go into the newly created folder `cd my-app`, then use the automatically created launch script to start the react application: `npm start`.