# Recursion

We have seen numerous times how we can call a function from another.

```javascript
function a() {
    b();
}

function b() {
    // do something...
}
```

Can we do the same with a single function? A function calling itself?
Yes, we can do that. It is called recursion. In our case it means a function calls itself in order to solve a problem.

Basically what we do is breaking down a larger problem into simpler, more manageable subproblems. Then continue this process until the problem becomes simple enough to be solved directly, without further recursion. In essence, recursion involves solving a problem by reducing it to smaller instances of the same problem.



### Factorial example:

> A factorial represents the product of all positive integers up to a given number and is denoted by the "!" symbol in mathematics. In other words the factorial of a non-negative integer \( n \) is the product of all positive integers less than or equal to \( n \). 
So for a non-negative integer \( n \), it is denoted as \( n! \).

 n! = n * (n-1) * (n-2) * ... * 2 * 1 

The factorial function is defined as follows:

- \( 0! = 1 \) (The factorial of 0 is defined to be 1).
- \( 1! = 1 \) (The factorial of 1 is 1).
- For \( n > 1 \): \( n! = n * (n-1)! \)

For example:

 5! = 5 * 4 * 3 * 2 * 1 = 120 

 3! = 3 * 2 * 1 = 6 


Here we can see how this problem can be easily represented by recursion, as for any \( n > 0 \),  the factorial is \( n \) times the factorial of \( n-1 \).

The factorial of 10 with loops:
```javascript
function factorialWithLoop(n) {
    for (let i = 1; i <= n; i++) {
        result = result * i;
    }
    return result;
}

```

Now with recursion:
```javascript
function factorialWithRecursion(n) {
  // Base case: factorial of 0 or 1 is 1
  if (n === 0 || n === 1) {
    return 1;
  }
  // Recursive case: n! = n * (n-1)!
  return n * factorialWithRecursion(n - 1);
}
```

- The `if()` block in this example is/are the "base case(s)". These are the conditions under which the function stops calling itself. The base case(s) provide a direct solution without further recursion. Without a base case, the recursive calls would continue indefinitely, leading to a stack overflow or infinite loop.

- The `return` statement in this example is the "recursive case". This is where the function calls itself with a modified or simpler version of the original problem. 

- Behind them is the "call stack". Each recursive call creates a new frame on the call stack, storing the local variables and execution context for that specific call. As the recursive calls reach the base case, the stack starts to unwind, and the function returns values back through the call stack.


The base case (or breaking condition in loops) is very important here as well, as otherwise we would get a stack overflow (or infinite loop) crashing the application like in the following example:

With recursion:
```javascript
function printIncreasingNumbers(num) {
  console.log(num);
  printIncreasingNumbers(num++); 
}

printIncreasingNumbers(0);
```

With loops:
```javascript
let num = 0;
while(true) console.log(num++);
```



Everything that can be done with loops can be done with recursion and the other way around, but some problems are easier and/or faster with one or the other.

In JavaScript, using recursion to go through an array is probably an overkill:

```javascript
function traverseArrayRecursively(arr, index = 0) {
  // Base case: stop when the index is equal to the array length
  if (index === arr.length) {
    return;
  }
  // Process the current element 
  console.log(arr[index]);
  // Recursive call to traverse the rest of the array
  traverseArrayRecursively(arr, index + 1);
}
```

### Head and tail recursion

Tail recursion and head recursion refer to the position of the recursive call within a function and how it affects the call stack.
This translates to lower or higher cpu and memory usage.

#### Head

* In head recursion, the recursive call is placed at the beginning of the function, before any other operations.
* It involves performing the recursive call first and then processing the result.
* Head recursion tends to use more memory as each recursive call is added to the call stack before any computation is done.

Example of head recursion for summing elements in an array:
```javascript
function headSum(arr, index = 0) {
  if (index === arr.length) {
    return 0;
  }
  return arr[index] + headSum(arr, index + 1);
}
const result = headSum([1, 2, 3, 4, 5]);
console.log(result); // 15
```

#### Tail

* In tail recursion, the recursive call is the last operation in the function, and its result is directly returned without further computation.
* The variable storing the current state of the computation is usually called "accumulator".
* Tail recursion can be optimized by some JavaScript engines to use constant stack space, as it eliminates the need to keep track of previous stack frames.

Example of tail recursion for summing elements in an array:
```javascript
function tailSum(arr, index = 0, accumulator = 0) {
  if (index === arr.length) {
    return accumulator;
  }
  return tailSum(arr, index + 1, accumulator + arr[index]);
}
const result = tailSum([1, 2, 3, 4, 5]);
console.log(result); //  15
```
The following snippets illustrate the stack differences with calling it in an array with [0...10]:

```
headSum(A,0)
[ 1 + headSum(A,1) ]
[ 1 + [ 2 + headSum(A, 2) ]]
[ 1 + [ 2 + [ 3 + headSum(A, 3)]]]
[ 1 + [ 2 + [ 3 + [ 4 + headSum(A, 4)]]]]
[ 1 + [ 2 + [ 3 + [ 4 + [ 5 + headSum(A, 5)]]]]]
[ 1 + [ 2 + [ 3 + [ 4 + [ 5 + [ 6 + headSum(A, 6)]]]]]]
[ 1 + [ 2 + [ 3 + [ 4 + [ 5 + [ 6 + [ 7 + headSum(A, 7)]]]]]]]
[ 1 + [ 2 + [ 3 + [ 4 + [ 5 + [ 6 + [ 7 + [ 8 + headSum(A, 8)]]]]]]]]
[ 1 + [ 2 + [ 3 + [ 4 + [ 5 + [ 6 + [ 7 + [ 8 + [ 9 + headSum(A, 9)]]]]]]]]]
[ 1 + [ 2 + [ 3 + [ 4 + [ 5 + [ 6 + [ 7 + [ 8 + [ 9 + [ 10 ]]]]]]]]]]
[ 1 + [ 2 + [ 3 + [ 4 + [ 5 + [ 6 + [ 7 + [ 8 + [ 19 ]]]]]]]]]
[ 1 + [ 2 + [ 3 + [ 4 + [ 5 + [ 6 + [ 7 + [ 27 ]]]]]]]]
[ 1 + [ 2 + [ 3 + [ 4 + [ 5 + [ 6 + [ 34 ]]]]]]]
[ 1 + [ 2 + [ 3 + [ 4 + [ 5 + [ 40 ]]]]]]
[ 1 + [ 2 + [ 3 + [ 4 + [ 45 ]]]]]
[ 1 + [ 2 + [ 3 + [ 49 ]]]]
[ 1 + [ 2 + [ 52 ]]]
[ 1 + [ 54 ]]
55
```

```
tailSum(B,0,0)
tailSum(B,1,1)
tailSum(B,2,3)
tailSum(B,3,6)
tailSum(B,4,10)
tailSum(B,5,15)
tailSum(B,6,21)
tailSum(B,7,28)
tailSum(B,8,36)
tailSum(B,9,45)
55
```

## Fibonacci example:

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The sequence starts with 0 and 1.

Here, the recursive version start being simpler and easier compared to the iterative one.

Iterative Fibonacci:
```javascript
function fibonacciIterative(n) {
  if (n <= 1) {
    return n;
  }

  let fib = [0, 1];
  for (let i = 2; i <= n; i++) {
    fib[i] = fib[i - 1] + fib[i - 2];
  }

  return fib[n];
}
```


Recursive fibonacci:
```javascript
function fibonacciRecursive(n) {
  if (n <= 1) {
    return n;
  }

  return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}
```

### Traversing trees

A binary tree is a hierarchical (recursive) data structure in which each node has at most two children, referred to as the left child and the right child. These children are also nodes, forming subtrees of their own. The topmost node in a binary tree is called the root, and nodes with no children are called leaves.

![tree](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/1200px-Binary_search_tree.svg.png)

The definition of a Tree node as a class:

```javascript
class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}
```

Creating an example tree:

```javascript
const root = new TreeNode(1);
root.left = new TreeNode(2);
root.right = new TreeNode(3);
root.left.left = new TreeNode(4);
root.left.right = new TreeNode(5);
root.right.left = new TreeNode(6);
root.right.right = new TreeNode(7);
```

Traversing the tree: tomorrow :)