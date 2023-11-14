# 1. Forms

Aside from various clickable surfaces and buttons, forms and input elements inside forms are the main way to get input from the user.

A form is a grouping of input elements, labels and buttons.
It has an opening and a closing tag, with the opening having action and method attributes that specify the endpoint in the server where we send the submitted information.

```
    <form action="http://example.com" method="post">
    [...]
    </form>
```

> We will learn about backend communication as well as what does the method means later.

### 1.1 input tags and labels

```<input>``` tags can be of a great number of types. They can behave, look, and validate input differently.

Including but not limited to:
- text
- multiline text (textarea)
- password
- number
- radio
- checkbox
- button
- file
- date
- time
- email
- color
- range
- lists
- searchable lists

Input tags are usually associated with ```<label>```s that act as tooltip and helpful descriptions also focusing on the input fields when clicked.

To that end, we can either embed the input field inside a label

```
    <label>Name:
        <input type="text">
    </label>
```

or associate them through the ```for``` and ```id``` attributes.

```
    <label for="name">Name:</label>
    <input type="text" id="name">
```


Instead of detailing all of them here, let's see an example showcasing the differences and usages of the various input types. Open and download [formshowcase.html](./resources/formshowcase.html) from the resources folder.



### 1.1.1 useful input attributes

There are a few attributes that are used extensively, such as setting a placeholder value for a text field, making a form element uninteractable, or unmodifiable, disabling browser auto-completion functions or automatically focusing an element.

```
    <input type="text" placeholder="Search...">
    <input type="text" readonly>
    <input type="text" disabled>
    <input type="text" autocomplete="off">
    <input type="text" autofocus>
```


### 1.2 Validation

Next, some primitive validation of the values entered or selected can be done through HTML.

We can make a field required, set the minimum or maximum length of the characters entered, or validate the entered text with regular expressions.
The last regular expression "[A-Za-z0-9]{10}" means that the password can contain english upper and lowercase letters as well as numbers and must be exactly 10 characters long.

```
    <input type="text" required>
    <input type="text" maxlength="10">
    <input type="number" min="1" max="10" step="1">
    <input type="password" name="code" pattern="[A-Za-z0-9]{10}">
```

>  We will see much more powerful options for validation with JavaScript, but keep in mind, that these validations are only for presenting it nicely to the user. <span style="color:red">Data have to be validated on the server side (as well), as client side validation is unsecure and trivially circumventable!</span>


# 2. Input field examples


A simple text field with no rules, validation or limitations, the most primitive of input elements.

```
    <input id="yourname" type="text" name="yourname"/>
```

An e-mail form with automatic e-mail validation due to the input type.

```
    <input type="email" name="email"/>
```

Compared to a simple text input field, a text are  is defined with specific dimensions - 40 columns and 5 rows in this case - allowing for a multi-line input. It can also be resized and automatically adds a scroll-bar allowing for even larger inputs if the user runs out of space.

```
    <textarea name="story" cols="40" rows="5"></textarea>

```

This form field is designed to capture a password. A regular expression pattern attribute is set to enforce that the password must consist of alphanumeric characters and be exactly 10 characters long. (Remember, only in the client side!!!)
Furthermore, it allows for browsers or other programs to suggest new or autofill old passwords, as well as it displays any text entered into it as black dots instead of the actual characters entered.

```
    <input type="password" name="password" pattern="[A-Za-z0-9]{10}"/>
```


This input type is used for file uploads. Users can select one or multiple files from their device. The multiple attribute allows the selection of multiple files.

```
    <input type="file" name="file" multiple/>
```

The date input allows users to select a date from a calendar picker, while the time input allows users to pick a specific time. These inputs are useful for applications that require date and time information, such as event scheduling.

```
    <input type="date" name="date"/>
    <input type="time" name="time"/>
```

Input type for numeric values. The min and max attributes define the acceptable range, and the step attribute sets the increment between allowed values. In this example, it's used to input ages within the range 0 to 100 with increments of 0.1.

```
    <input type="number" min="0" max="100" step="0.1" name="age">
```

A simple color picker, allowing users to select a color. The selected color is usually represented as a hexadecimal RGB value (#1289af). It's commonly used in applications where users need to choose or customize colors, such as in web design or image editing.

```
    <input type="color" name="color"/>
```

This  creates a slider control, allowing users to select a value within a specified numeric range. In this example, the range is from 0 to 5.

```
    <input type="range" min="0" max="5" name="cars">
```

Radio buttons are used to create a set of mutually exclusive options. In this example, each browser option (Firefox, Chrome, Safari, Edge) is associated with the same "browser" name, allowing the user to choose one and only one of the options.

```
    <label>
        Firefox
        <input type="radio" name="browser">
    </label>
    <label> 
        Chrome
        <input type="radio" name="browser">
    </label>
    <label> 
        Safari
        <input type="radio" name="browser">
    </label>
    <label> 
        Edge
        <input type="radio" name="browser">
    </label>
```

The `<select>` element creates a dropdown list, and the associated `<option>`` elements define the selectable choices. The optgroup element is used to group options. The initial option serves as a placeholder with the label "Choose something."

```
    <label>
        Your favourite animal:
        <select name="animal">
            <option selected disabled hidden>Choose something</option>
            <optgroup label="Birds">
                <option value="Pigeon">Pigeon</option>
                <option value="Seagull">Seagull</option>
                <option value="Sparrow">Sparrow</option>   
            </optgroup>
            <optgroup label="Mammals">
                <option value="Elephant">Elephant</option>
                <option value="Dolphin">Dolphin</option>
            </optgroup>
        </select>
    </label>
```

This combination of `<input>` and `<datalist>` provides a text input field with a list of predefined options. Users can either choose from the list or manually enter a value. In this case, the input is for selecting a favorite programming language from the provided options.

```
    <label>
        Favourite programming language:
        <input list="langs" name="langs">
    </label>
    <datalist id="langs">
        <option value="JavaScript"></option>
        <option value="Java"></option>
        <option value="PHP"></option>
        <option value="Haskell"></option>
    </datalist>
```

# 3. Buttons inside forms

HTML `<button>`s also behave directly once they are enclosed in a `<form>`.
The default behaviour of a button without a "type" being set, or one with the "submit" type corresponds to the "submit" action which triggers a submit event gathering all data from the form and navigating (away) from the current page at the same time.

```
<button type="submit">Submit</button>
```

Clicking on a button with the type "reset" resets all form fields to their default values, as defined in the HTML. It triggers the form's reset event.

```
    <button type="reset">Reset</button>
```

A button with a type of "button" doesn't have a predefined behavior associated with form submission or resetting. It's often used in conjunction with JavaScript to define custom behaviors when clicked.

```
    <button type="button">Click me</button>
```

Lastly, a button with the type "image" creates a graphical submit button. When clicked, it submits the form, and the coordinates of the click are sent as form data. It's less commonly used nowadays, and <button> or <input type="submit"> is often preferred styled with CSS afterwards.


> Download and open [formshowcase.html](./resources/formshowcase.html) to see all these in action!