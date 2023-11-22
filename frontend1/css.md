# Cascading Style Sheets

With CSS we can define the style; the overall look and feel of our webpage.
It describes how HTML elements should look like.

## 1. Selectors

Every CSS rule starts with a <b>selector</b>. A selector describes which elements the rules should apply.

A selector contains key-value pairs to set the rules.

A HTML page can link to one or more CSS files, contain a style block in its head as well as apply styles directly on elements.

A few examples:

```
/* make a heading red and bigger in size */
h1 {
    color: #FF0000;
    font-size: 30px;
}

/* make links white with a green background-color and red border... */
a {
    color: #FFFFFF;
    background-color: #00FF00;
    border: 2px solid red;
}

/* except when they are in a nav, because then the text color should be yellow then */
/* more specific selectors are "stronger" and override/rule weaker ones */
nav a {
    color: #FFFF00;
}
```

### 1.1 Type of selectors




<table border="0">
 <tr>
    <td>CSS Selector</td>
    <td>HTML Tag</td>
 </tr>
 <tr>
    <td colspan=2>
        Selectors for HTML tags: just use them with the tag's name.
    </td>
 </tr>
 <tr>
<td>

```
a {
    color: red;
}
```

</td>
<td>

```
<a>
    Some link
</a>
```

</td>
 </tr>
 <tr>
    <td colspan=2>
        Selectors for classes which we refer to with "class" attributes in HTML.
    </td>
 </tr>
 <tr>
    <td>

```
.myclass {
    color: red;
}
```

</td>
<td>

```
<div class="myclass>
    Some text
</div>
```

</td>
 </tr>
  <tr>
    <td colspan=2>
        Selectors for unique elements which we refer to with "id" attributes in HTML.
    </td>
 </tr>
 <tr>
    <td>

```
.myuniqueid {
    color: red;
}
```

</td>
<td>

```
<div id="myuniqueid">
    Some text
</div>
```

</td>
 </tr>
</table>


Then we can have complex or compound selectors as well, combining the ones mentioned above in various ways:

<table border="0">
 <tr>
    <td>CSS Selector</td>
    <td>HTML Tag</td>
 </tr>
 <tr>
    <td colspan=2>
        Class directly inside a specific tag (direct children).
    </td>
 </tr>
 <tr>
<td>

```
nav > .link {
    color: red;
}
```

</td>
<td>

```
<nav>
  <a class="link">...</a>
</nav>
```

</td>
 </tr>
 <tr>
    <td colspan=2>
        Class inside a specific tag.
    </td>
 </tr>
 <tr>
    <td>

```
nav .link {
    color: red;
}
```

</td>
<td>

```
<nav>
  <ul>
    <li>
      <a class="link">...</a>
    </li>
  </ul>
</nav>
```

</td>
 </tr>
  <tr>
    <td colspan=2>
        Tag (or class or id) and class (or id) at the same time. When a tag (or class or id) has a specific class (or id) on it.
    </td>
 </tr>
 <tr>
    <td>

```
nav.main {
    color: red;
}
```

</td>
<td>

```
<nav class="main>
 ...
</nav>
```

</td>
 </tr>
</table>

Further useful selectors:

Universal selector. Selects ALL elements on the page:

```
* { 
    color: red;
}
```

Attribute selector. Only selects links that has a "href" attribute with the value of example.com:

```
a[href="https://example.com"] {
  color: #FF0000;
}
```

Sibling selector. Selects elements next to (being in the same level of the DOM, and both being under a same parent) another specific elements:

```
div ~ p {
    color: red;
}
```

Adjacent sibling selector. Only selects siblings directly next to each other.

```
div + p {
    color: red;
}
```

And a lot more. See at the [MDN page about CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_selectors).

## 1.2 Pseudo classes

Disabled input:

```
:disabled { 
    color: yellow; 
}
```

First children of an element:

```
:first-child {
    color: yellow;
}
```

If the cursor is hovering above an element:

```
:hover {
    background-color: purple;
}
```

And a lot more. See at the [MDN page about pseudo classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes).

## 1.3 Pseudo elements

Creating a new "fake" element as first child of an element:

```
div::before {
    content: 'before the element';
    background-color: red;
}
```

Creating a new "fake" element as last child of an element:

```
div::after {
    content: 'after the element';
    background-color: green;
}
```

Selected (highlighted) parts of a page: 

```
::selection {
    background-color: orange;
}
```

Making the first character of an element bigger:

```
::first-letter{ 
    font-size: 30px; 
}
```

And a lot more. See at the [MDN page about pseudo elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements).

## 2. Inline and block elements

Every element is surrounded by a rectangular "box". No matter whether it looks like a triangle, a circle or if it does not have any background. It still resides inside a "bounding box".

This bounding box defines the size the element will take in the page.

> We can see the bounding box of every element of a page if we type the next snippet in our browser's developer tools, or if we add it in our CSS. 

```
* {
    border: 1px dashed red !important;
}
```

This brings us to a way we can divide elements into (mostly) two. To inline and block-like elements.

<b>Inline</b> elements are elements which are naturally "placed next to each other".

Examples of these are `<span>`, `<a>`, `<img>`, etc.

<b>Block</b> elements, which always start in a new line and always fill their parents.

Examples of these are `<div>`, `<form>`, etc.

### 2.1 Inline elements

Inline elements appear next to each other in a single line, and only get placed in a new line in case there is not enough space for them in the current one. These are usually elements fitting into the text stream. Consequently this flow is from left to right (and from top to bottom).

Furthermore, inline elements's `width`, `height` and vertical padding and margin properties cannot be set (so as not to break the text flow). However they have other properties like `text-align`, `line-height` and `vertical-align`.



### 2.2 Block elements

Always start in a new line and always fill their parents. Therefore they always appear below each other (provided their styles are not overwritten in other ways) in the DOM. This is called block-flow, and its direction is from top to bottom (and from left to right).

Blocks can be embedded into each other, and the block-flow will be in effect therein as well.


In comparison, the aforementioned `text-align`, `line-height` and `vertical-align` properties do not work on block elements, however other properties like `width`, `height` and various other padding and margin options can be set on them.

> Setting % for height can be tricky, as this percentage is always relative to the size of the parent including `body` and `html`.


### 2.3 "Converting" between inline and block elements

Any inline element can be converted to block elements by setting the `display` property to `block`. Similarly, every block element can be made to be inline by setting it to `inline`.

Some other properties applied on an element interrupt the inline flow making them effectively behave like block elements. For exmaple `float`, `position`, etc. Consequently we can set block-only properties on them like `width` and `height`.

### 2.4 Margin and padding

Simply put, `margin` is around the element, while padding is between the `border` of the element and the element itself.

![marginpadding](https://i.imgur.com/CgNJcmM.png)

> Margin collapse should be mentioned here. If a block's bottom margin meets the nextr block's top margin, the two margins do not add up, rather only the bigger margin shows.


### 2.5 Inline-block elements

Inline elements are useful, as the elements are put nicely next to each other, while block elements are good as we can play around with margins, paddings and sizings.

Inline-blocks combine these properties of inline and block elements. An element with a `display` property set to `inline-block` will stay part of the "inline-flow", however we can set various "block" properties on it.

Elements that are inline-block: `button`, `select`, in various browsers `input`. 

> `img` is shown as inline by the browser, but works as an inline-block element. Remember that we can set its sizes!

> Setting the `float` property to `left` or `right`, or the `position` property to `absolute` or `fixed` will also make an element behave like a "box". Therefore, it is redundant to also set the `display` property on them most of the time.

### 2.6 More display modes

There are also a few more values the display property can take.
For example `table`, `table-row`, `table-column`, `table-cell` used by tables.
Also `flex`, about which we will learn a lot more later.

## 3. Positioning

By setting the `position` property on an element, we can take it out from the normal document flow and instead place it somewhere else on the page.

### 3.1 position: static

This is the default positioning value. In this case, the element is part of the standard document flow. As it is the default, we
very rarely set it manually.

### 3.2 position: relative

Setting position to relative on an element makes the originally space "intended" for the element empty while moving the element around; thus the arrangement of the rest of the elements will not change.

How it is achieved is basically putting the element in a separate "layer", "above" the rest of the elements.

### 3.3 position: absolute

Precise positioning of the element in the current coordinate system we are in. Who defines what the "current" coordinate system is?
Either a parent element with `position` set to `relative`, or the `body` itself.

If an element has absolute positioning it is totally taken out of the document flow and to a new "layer", it's original "intended" place 
used by the next element instead, like if it wouldn't even be there.

Furthermore, absolutely positioned elements will behave block-like. `width` and `height` are allowed to (and usually have to) be set on them.
In comparison to block elements however, these elements would not automatically fill the full width of their parents,
but the minimal size that they absolutely need.

Absolute positioning can do pixel-perfect layouts trivially easy, however they are very inflexible in creating flexible layouts.
Therefore, we are mostly using this positioning in smaller components where we need pixel-perfect arrangement and while
we do not have many elements to work with.

### 3.4 position: fixed

Very similar to `absolute`, however the element will stay in its place even when we scroll away.

As another difference compared to absolute elements, the coordinate system here is (almost, except when using css transformations) 
always the top-left corner of the browser window.

Fixed positioning is very useful for example for making navigation menus.

### 3.5 Z-index

As we can gather from above, any positioning setting aside from `static` makes the element appear on a "new layer".
But what is this new layer? How can we define a new layer? Or how can we reorder them?

We can use the setting `z-index` to define the order of elements. Which element should be below or above others.
The default value is `auto`, but we can set it to any integer number, even to negatives.

These z-index values are hierarchical, and starts "anew" 
- at every element with an absolute or relative positioning
- at a new flexbox element
- at an element with an opacity smaller than 1
- any transform property

### 3.6 Float

It's original purpose was to wrap text around an image either from the left or right. The emphasis is on <b>text</b>
now, but basically everything else will try to wrap around the floated element as well.
This property makes it so useful in creating layouts (and also so hard).

At the first look, what `float`ing does to an element is possibly the worst that can happen. Tears it out of the document flow
while also having an effect on the flow itself. 

A floated element will behave "block-like" in regard to listening to height, width, margin and similar properties.
Also, while they are teared out of the flow, they won't be placed in a new layer, so z-index will not work on them either.

Related to float is the `clear` property which disables the wrapping effect on either or both sides.

## 4. Media queries

Media queries or rules allow us to apply styles conditionally, based on a condition such as 
the characteristics of the device like the size of its screen. This in turn is incredibly useful for creating responsive
designs that adapt to different screen sizes and devices. Media rules use the `@media` keyword, and you can 
specify various conditions within the media query.

The following example shows an element occupying 50% of the place available to it, but 100% if the screen's size is 800 pixel or less.

```
.myElement {
    width: 50%;
}

@media screen and (max-width: 800px) {
    .myElement {
        width: 100%;
    }
}
```

See more media queries at the [MDN page about media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries).





