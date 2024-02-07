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

