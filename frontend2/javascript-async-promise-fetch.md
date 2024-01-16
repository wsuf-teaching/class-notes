# Fetch, asynchronous execution, promises

The fetch function is used to make network requests, typically to fetch resources from a server. It is a modern and versatile replacement for the older XMLHttpRequest object. The fetch function returns a Promise that executes asynchronously to the Response to that request, whether it is successful or not. We either call it resolve or reject.

In the context of programming, "synchronous" and "asynchronous" refer to the way tasks or operations are executed and managed in a program.

In a synchronous programming model, tasks are executed one after the other in a sequential order. Each task must complete before the next one begins. Synchronous code is straightforward to read and understand because it follows a linear flow. However, it can lead to blocking behavior, where the program waits for a task to complete before moving on to the next one. 
This can be inefficient, especially when dealing with time-consuming operations. Also, if that operation "blocks" the "UI thread" (the visible stuff of our program or web application), then the whole interface will hang and will be unresponsive. 

The following is a trivial example of synchronous code. Each step executes after the other, strictly in the order they were typed. We can see that the output will be in the same order. The same goes for regular functions; even though they may be declared in various orders, the execution flow remains the same.

## Synchronous, asynchronous

```javascript
console.log("Start");
console.log("Step 1");
console.log("Step 2");
console.log("End");
```

In an asynchronous programming model, tasks are not executed in a strict sequential order. Instead, tasks that do not depend on each other can be executed concurrently or without waiting for each other to complete. Asynchronous code is often used for operations that may take some time to complete, such as fetching data from a server or reading from a file. Instead of blocking the program, it allows other tasks to continue while waiting for the asynchronous operation to finish.

Let's see a trivial asynchronous function example with `setTimeout`. The inner anonymous function printing "aaa" will be delayed in execution for 1000ms. Therefore, on any computer (with reasonable speed), it will execute long after the following statements. It does not wait for the timeout; instead, it executes the next operations in the meanwhile.

```javascript
setTimeout( () => {
    console.log("aaa");
},1000);
console.log("bbb");
console.log("ccc");
```

> `setInterval` works the exact same way, but it repeats the code written inside it indefinitely (or until we stop it or it crashes).

And asynchronous running of functions like this is beneficial; otherwise, the UI thread would hang, and the web application would be unusable in the meantime. 
The following is an example for that, you can put it anywhere in a HTML file's `<body>` and then click on the button. After, notice how you cannot interact with the website while it does ["busy-waiting"](https://en.wikipedia.org/wiki/Busy_waiting).


```html
<button id="but1">Button1</button>
<script>
    const but1 = document.querySelector('#but1');
    but1.onclick = async () => {
        let start = new Date().getTime();
        while (new Date().getTime() - start < 5000) {
            // simulate a delay of 5 seconds
            alert('after five seconds');
        }
    }
</script>
```

## Promises

Promises are a mechanism for handling asynchronous operations. When you create a Promise, it represents a value that might be available now, or in the future, or never. 
The `then` method is used to handle the resolution of a Promise (when it is fulfilled), and the `catch` method is used to handle any errors that might occur during the asynchronous operation (when it is rejected). Finally `finally` executes in either of these cases. This allows you to write code that can gracefully handle asynchronous tasks without blocking the rest of the program.

A Promise can be in one of three states:

* Pending: The initial state. The Promise is neither fulfilled nor rejected.
* Fulfilled: The operation completed successfully, and the Promise has a resulting value.
* Rejected: The operation failed, and the Promise has a reason for the failure.

The basic syntax of a Promise is as follows:

```javascript
// declare it first, the default state of it will be "pending"
const myPromise = new Promise((resolve, reject) => { // supplying both parametres is optional
  // Asynchronous operation, e.g., fetching data, reading a file, etc.
  // If successful, call resolve with the result. In this case it is a string, but it can be anything else.
  // If there's an error, call reject with the reason.
  setTimeout(() => {
    resolve("Async operation completed");
    //reject("Async operation failed");
  }, 1000);
});
```

It can be handled through the then/catch/finally syntax.

```javascript
myPromise.then((result) => {
    console.log(result);
}).catch((error) => {
    console.log(error);
}).finally(() => {
    console.log("executes either way");
});
```

Or through the use of await to stop the asynchronous execution and wait for the Promise (the asynchronous operation) to settle (either resolve or reject):

```javascript
await myPromise;
const promiseValue = await myPromise;
```

```javascript
function delay(ms) {
  // here we don't really do anything to resolve the promise, just resolve it doing nothing
  return new Promise(resolve => setTimeout(resolve, ms));
}
async function myAsyncFunction() {
  console.log("Start");
  await delay(1000); 
  console.log("After waiting for 1 second, execution stops in the meanwhile");
  console.log("End");
}
myAsyncFunction();
```

## Fetch

`fetch` works based on Promises. It is actually returning a Promise that resolves to the Response to that request.

An example usage of `fetch` can be seen below:

```javascript
fetch("http://127.0.0.1:5000/test")
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Fetch error:', error));
```

Let's break it down:

We try to get the data from the URL supplied. `fetch` returns a Promise that will `resolve` (on success) to the response of that request or otherwise fail (`reject`).

If the call was successful (in the sense that the server returned "something" – it doesn't necessarily mean that it's something good), then the response object will be returned. The body of the response is a stream object, which can be quite large.

> It is a good practice to also check the status of the response here, whether it indeed indicates success (either response.ok or response.status being in the 2xx range [200]).
> This way, the code would look something like the following:
> ```javascript
> fetch("http://127.0.0.1:5000/test")
>     .then(response => {
>         if (!response.ok ) {
>             return Promise.reject(`HTTP error! Status: ${response.status}`);
>         return response.json()
>     })
>     .then(data => console.log(data))
>     .catch(error => console.error('Fetch error:', error));
> ```

If the status code of the response is OK, we can process its body once again asynchronously. Of course, we can do it manually (see this [documentation](https://developer.mozilla.org/en-US/docs/Web/API/Response/body)), but as we usually work with JSON data on websites, the `.json()` function does this for us. It treats and converts the response data to JSON. In a successful operation, we can just return the value we want, as it being "resolved" is implicitly agreed on. This would mean the same as: `return Promise.resolve(response.json());` or `return response.json();` for short.

Then, if the response was ok and the JSON conversion was successful as well, we get an array of (JSON) objects. We can treat it as a regular JavaScript array and do anything with it as we would otherwise.

Lastly, if any of the promises (including the `fetch` call and the `then` blocks as they are promises themselves) fail, we catch and print out the errors here. The `finally` block executes either way, both in a success or a failure case.

### Further parametres of fetch

The URL is only one of the parameters `fetch` can take. The second parameter it accepts is an object that can contain various parameters, including but not limited to the request method, various headers (name and value pairs), and a potential request body (data we send to the server).

For example:

```javascript
fetch("http://127.0.0.1:5000/test_flights", {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    key1: 'value1',
    key2: 'value2'
  })
})
```

You can read more about `fetch` [here](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API).

