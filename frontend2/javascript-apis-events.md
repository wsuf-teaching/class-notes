# JavaScript APIs

Aside from the basic data structures and control sequences, JavaScript also comes with numerous APIs out of the box which we can use
to make web applications.

Here is a non-exhaustive list of them:
- DOM: used to manipulate HTML and CSS
- fetch: to dynamically get data from other sites or endpoints
- windows: to get information about the window, to close or open new ones.
- storage: every website has some form of access to various storage options inside a browser
- cookies: to set small snippets of data in the browser
- notifications: displaying notifications to the user through the browser
- third party APIs like for Google maps or Facebook
- and see many more on [MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API)

## Important objects inside a browser

### Navigator

Stores the browser's state. We can for example get the type and version of the browser,
the user's preferred language, geolocation and many other high level things.

```javascript
navigator.userAgent
navigator.language
```

### Window

Window in this context refers to the active "tab" where the website is loaded.
We can access the browser console here, this is the place where global objects (created without the `var`, `let` or `const` keywords) are created,
This object stores the page's URL we can access (and modify) and also the history object which we can also override or change.

```javascript
window.location.href
window.location.href = "https://example.com"
```

### Document

The actual DOM that gets loaded inside a window. We can use the document to modify the currently loaded webpage.

## DOM

The DOM, the document object model describes the whole structure of the HTML page in a tree structure. Its root is the "document" object
then come the rest of the page hierarchically.

![dom](https://developer.mozilla.org/en-US/docs/Web/API/Document_object_model/Using_the_Document_Object_Model/using_the_w3c_dom_level_1_core-doctree.jpg)

### Retrieving DOM elements 
<span id="retrieving-dom-elements"></span>

We can retrieve a single element by its ID:

```javascript
document.getElementById("youridhere");
```

Multiple elements by their class or tag names:

```javascript
document.getElementsByClassName("yourclassnamehere");
document.getElementsByTagName("img");
```

There are also general selectors that can do all the previous combined retrieving either one or multiple matching elements:

```javascript
document.querySelector("a.myclass#myid:hover");
document.querySelectorAll("div.myotherclass.mythirdclass");
```

Then after getting 1 or more elements with these selectors, we can modify their content, their styles, or add newly created elements inside or around them.
More about this very in a section or two.

### Creating DOM elements

> From here below you can try these out on the starter project found in the [resources](./resources/events-example-starter.zip) folder.

The `document.createElement()` method is used to create a new HTML element. The argument it takers should be the type of the element as a string.

```javascript
const newElement = document.createElement('div');
```

> The function `document.createTextNode("some text")` working similarly can create texts without an associated HTML tag

Attributes like "id" and such can be set or added with the `setAttribute` and `removeAttribute` methods.

```javascript
newElement.setAttribute('id','newDiv');
newElement.removeAttribute('newDiv');
```

Styling can be accomplished by setting properties on the `style` property of any elements:

```javascript
newElement.style.backgroundColor = "#ccc";
newElement.style.border = "2px solid red";
```

> Any and all CSS properties can be set this way. The only difference is that the dashes inside the property names are replaced with a camelCase notation.
> In the example above `background-color` became `backgroundColor`.

Content - either text or further inlined HTML can be inserted inside this element as well. Keep in mind, that both the `innerHTML` and `textContent`
functions would override any previous content set on the element.

```javascript
newElement.innerHTML = '<p>This is a new paragraph inside the previously created div.</p>';
newElement.textContent = 'Text inside the div'; 
```

If we don't want to override, but rather insert into an existing element, we can use either the `appendChild`, `insertBefore` and `insertAfter`, `insertAdjacentElement` functions.

`appendChild` appends the newly created element to an existing element. Appends as in it puts it just before the end of it.

```javascript
const parentElement = document.getElementById('firstDiv');
parentElement.appendChild(newElement);
```

![append](https://i.imgur.com/G4TvAHo.png)

`insertBefore` inserts the new element before an existing child element. You can think about `appendChild` as inserting a new element in relation to just their new parents,
while `insertBefore` places them also in relation to their new siblings.

```javascript
const parentElement = document.getElementById('firstDiv');
const existingChild = document.getElementById('existingChildDiv');
parentElement.insertBefore(newElement, existingChild);
```
![insertbefore](https://i.imgur.com/ylkuyiJ.png)

A more generally usable function is `insertAdjacentElement`. With that, we can place an element right before another one starts, or right after it ends, or inside an element as its first or last child.
These positions should be given to the methods as strings as the first parameter:
- `beforebegin`
- `afterbegin`
- `beforeend`
- `afterend`

```javascript
const parentElement = document.getElementById('firstDiv');
parentElement.insertAdjacentElement("beforebegin", newElement);
```

![beforebegin](https://i.imgur.com/NCfyh1O.png)

```javascript
const parentElement = document.getElementById('firstDiv');
parentElement.insertAdjacentElement("afterend", newElement);
```

![afterend](https://i.imgur.com/nohMKQg.png)

```javascript
const parentElement = document.getElementById('firstDiv');
parentElement.insertAdjacentElement("afterbegin", newElement);
```

![afterbegin](https://i.imgur.com/YTylUjq.png)

```javascript
const parentElement = document.getElementById('firstDiv');
parentElement.insertAdjacentElement("beforeend", newElement);
```

![beforeend](https://i.imgur.com/ZGolBP8.png)

> `insertAdjacentHTML` and `insertAdjacentText` can be used in a similar fashion for insert a string as HTML content, or simply inserting plain strings.

## Listening to events

There are [numerous events](https://developer.mozilla.org/en-US/docs/Web/API/Element#events) we can "subscribe" to on specific elements.

For example:
- clicking on an element (click)
- hovering over an element (mouseover)
- hitting a key on the keyboard (keypress)
- when an element is being focused (focus)
- when copying or pasting something (copy, cut, paste)
- changing the value of an input field (change)
- etc.

### Inline event listeners

The most primitive way to subscribe to events of an element. The listener is inlined directly on the element as a property in the HTML.

```html
<button onclick="alert('button is clicked')">Click me</button>
```

```html
<input type="text" onkeyup="console.log(event.target.value)"/>
```

> Note, how we use the `event.target.value` property to retrieve the input field's current value. `target` in this case refers to the element
> that triggered the event. This might not be the same as the element that actually has the event listener attached, as elements can bubble (more about this soon!).
> To get the value of the element that has the event listener we can use the `currentTarget` property.

All in all, inline events are not that great in more complex application, as they require a tighter integration between HTML and JS and thus make certain events harder to find and the HTML harder to read as well. 
Just like how we prefer to add CSS styles in a separate file instead of inlining them.

## Loading of elements

One important note here, before we delve further into event handlers.
We can only register events on elements after they have been created. 
We can wait for that specific time multiple ways:

0. Registering the elements inlined on the HTML elements (as shown above).

1. Waiting for some 'global' event until registering event listeners and writing the rest of our JS logic:

```javascript
document.addEventListener('DOMContentLoaded', function () { 
    // doing our logic here 
});
```
2. Waiting for the `window.onload` event before writing our listeners and logic:

```javascript
window.onload = function () {
    // code to run after everything else has loaded
};
```

3. Putting the `<script>` tags to the very end of the `<body>`.

```html
    [...]
    [...]
    <script src="script.js"></script>
</body>
```

4. Adding the `defer` attribute to the script to defer its loading until the HTML document is fully parsed.

```html
<script src="script.js" defer></script>
```

## Events

After the elements have loaded, we are free to register the event listeners.

First, we have to search and identify the element we want to attach a listener to.
This can be achieved in various ways, some of which were discussed in the chapter titled [Retrieving DOM elements](#retrieving-dom-elements) above.

### Registering a single event

After grabbing it, we can simply refer to the various events prefixed with the "on" keyword as properties.
For example the click event listener will be `onclick` and so on..

Let's see this in practice through an example:
> ```html
> <button id="myBtn">Click me</button>
> ```
> 
> Then we can retrieve it using `document.querySelector`.
> 
> ```javascript
> let myButton = document.querySelector('#myBtn');
> ```
> 
> Finally, we can attach the event handler function on it:
> 
> ```javascript
> myButton.onclick = () => {
>     alert('cicked');
> }
> ```

Here is another example where we use the event property automatically passed on to the event handler function.

> ```html
> <input type="text" id="myText"/>
> ```
>
> ```javascript
> let myText = document.getElementById("myText");
> ```
>
> ```javascript
> myText.onkeyup = (event) => {
>   console.log(event.target.value);
> }
> ```

### Registering multiple events

The previous syntax only allows one event of a certain type (like click or keydown) to be registered on any elements.
Any further assignment on it would simply overwrite the previously assigned one.
If we want to have multiple, we can use the `addEventListener()` function.
It has to be called on the element we are adding an event listener to, and it's two parameters are the event listener type (now WITHOUT the 'on' prefix) and the function to be run on firing an event.

Let's see it in practice:

> ```html
> <button id="myOtherBtn">Click me</button>
> ```
> 
> ```javascript
> let myOtherButton = document.querySelector("#myOtherBtn");
> 
> const listener1 = () => alert('First listener');
> const listener2 = () => alert('Second listener');
> const listener3 = (event) => {
>   console.log(event);
>   alert('Third listener');
> }
> 
> myOtherButton.addEventListener('click',listener1);
> myOtherButton.addEventListener('click',listener2);
> myOtherButton.addEventListener('click',listener3);
> ```
> 
> Here, the event listener functions would run in the order they were added.

### Binding listeners

There is but one problem still with the `addEventListener` construct above. Aside the `event` parameter that is automatically filled and added by JavaScript, 
we have no (proper) way to pass arguments to these functions.

One of these solutions is function binding. When we "bind" a function it actually created a new function that,
when called, calls the original function with (as the first argument the `this` keyword set to the provided value) and
a given sequence of additional arguments provided.

Adding to the previous example, it would look like the following passing a string, a number and a boolean value as parameters:

> ```javascript
> const listener4 = (p1, p2, p3) => alert(`Fourth listener with params: ${p1}, ${p2}, ${p3}`);
> 
> myOtherButton.addEventListener('click', listener4.bind(null, 'some text', 123456, true));
> // in this example we don't need "this", so we set it to null
> ```

### Event bubbling

Event bubbling is a phase in the event propagation model in JavaScript, 
where an event starts from the target element that triggered the event and bubbles up 
through its ancestors in the DOM hierarchy. During this process, each ancestor 
element has the opportunity to handle the event. After a listener on an ancestor finishes,
the event bubbles up one level to the next ancestor all the way up to the `window` object.

![eventbubbling](https://www.w3.org/TR/DOM-Level-3-Events/images/eventflow.svg)

Let's also see this in motion:

> ```html
> <div id="outer">
>     <div id="middle">
>         <div id="inner">Click me!</div>
>     </div>
> </div>
> ```
> 
> ```javascript
> window.addEventListener('click', function() {
>     alert('Window clicked!');
> });
> 
> document.addEventListener('click', function() {
>     alert('Document clicked!');
> });
> 
> document.body.addEventListener('click', function() {
>     alert('Body clicked!');
> });
> 
> document.getElementById('outer').addEventListener('click', function() {
>     alert('Outer div clicked!');
> });
> 
> document.getElementById('middle').addEventListener('click', function() {
>     alert('Middle div clicked!');
> });
> 
> document.getElementById('inner').addEventListener('click', function() {
>     alert('Inner div clicked!');
> });
> ```

> At any level, we can stop this chain of calls with the `event.stopPropagation()` method 
> (which of course needs the event object to be passed as a parameter to the concerned event listener).

Event bubbling is the usual way we handle events.
This is in contrast to event capturing, where the event travels from the top of the DOM hierarchy down to the target element.

Switching between the two methods can be done by passing a third boolean parameter to the `addEventListener` calls.
That third param which we usually don't supply - defaults to `false` and thus makes the site handle the events in the "bubble" phase.
Setting it to `true` makes them fire in the "capture" phase - effectively in reversed order.