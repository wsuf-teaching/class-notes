# Flexbox

Flexbox, or the Flexible Box Layout, is a layout model in CSS (Cascading Style Sheets) designed to provide a more 
efficient and predictable way to arrange items and space among items in a container, 
even when the size of the items is unknown or dynamic. It aims to solve common layout problems that developers 
often face, such as distributing elements evenly or controlling the alignment of items.

Flex is a display property, just like `block` nad `inline`, however it allows for way more flex-ibility :) aligning elements.

We start with the following state, [a non-flexible layout](./resources/flexbox/0-nonflex).

## Flex

A parent element, the element whose children we want to arrange with flexbox needs this display property of `flex`
first and foremost.

```
    display: flex;
```

Setting this property on the "parent" class in our example will cause all the "child" elements to appear next to each
other sort of like if they were "inline-block" elements instead of "block". This is further supported by the fact
that we can set width and height properties on them as well and they will work.


## Flex-direction

Flexbox works through "two axes": horizontal and vertical. Flex-direction defines the "main" axis. Defines the direction
the flex items are places in the flex container. This property is too added on the "parent", but it only affects the "child" elements.

It's values can be: `row` (which is the default), `row-reverse`, `column` and `column-reverse`.

## Flex-wrap

By default, any element (like the "child" in our example) will try to fit into a single line, no matter what width we set on them.
Our example currently do not use width, but try setting it to a big value, like "30%". Even though they should be 
longer than the line (as 4*30% is > 100%), they do not, as the default `flex-wrap` property value prevents them from doing so.

That default value causing the single line layout is `nowrap`.
Other properties allowing the flex children to span across multiple lines are `wrap` and `wrap-reverse`.

If we try setting this property to `wrap`, what we will see is that three children will be in a line, and the fourth one
will spill over to the next as it cannot fit (as 3*30% = 90% < 100%, but 4*30% = 120% > 100%).

> You will notice that setting the size to 50% won't two elements in the same line. Why is that? Cause of the 2px margin we added on the children. :)
> Remove them, and they will fit just fine.

The stylesheet inside [1-flex-wrap](./resources/flexbox/1-flex-wrap) hosts the css properties
creating this state.

## Justify-content

Remember the two axes introduced above? This property aligns the elements along the main axis and automatically distributes
"extra" or "excess" space among them.

> To better showcase this property, set the width of the children to a smaller % or pixel value. 100px should work fine.
> Also add back the margins for a little bit of clarity.

A few options are trivial here, like `flex-start`/`left`, `center` or `flex-end`/`right`, putting all elements to their respective places 
at the beginning, center or end of the line.

> start or left and end or right behave differently in LTR or RTL layouts.
> We can set the HTML's direction by adding the `dir="rtl"` or `dir="ltr"` properties on the HTML tag.

However, it has a few more interesting one as well, which can automatically distribute the empty space around the elements
evenly based on the specific criteria.

* `space-between`: items are distributed evenly along the line
* `space-around`: evenly distributed items with equal space AROUND them (resulting in more space between elements than between the elements and the left and right borders)
* `space-evenly`: evenly distributed with equal spacing between both the elements and the border

These properties are especially interesting if the "child" elements in our case have pixel based width.

An example showcasing multiple `justify-content` values can be found in the [2-flex-justify-content folder](./resources/flexbox/2-flex-justify-content).

## Align-items

The align-items property's effects are in one way very similar to justify-content, but it works on the "cross" (or secondary) axis 
of the layout instead of the "main".

> To see the individual changes better, set a height of 100px on the parent

The default value is `stretch` which stretches the element by the cross axis (still respecting min and max width properties set).

> To see these changes better, set various different heights on the child elements.

* `flex-start` puts the elements on their "normal" HTML position with no size changes based on LTR or RTL alignment.
* `flex-end` is pretty much the same but with the other direction.
* `center` well, centers the elements across the cross axis.

The [3-align-items](./resources/flexbox/3-align-items) has a CSS file prepared with elements of multiple sizes for this purpose.

## Align-content

This applies to the alignment of the elements when they wrap, only taking effect on multi-line containers.
It basically defines how should the rows (compared to individual items) behave in their enclosing space.

The values it can take are the following: `flex-start`, `flex-end`, `center`, `stretch`, `space-between` and lastly `space-around` and
they all behave very similarly to the values of other properties discussed above.

Once again, here is a prepared example at [4-align-content](./resources/flexbox/4-align-content) showing a few of these options.

## Order

Finally, we are talking about properties children (individually) can take.
With this setting we can manually and arbitrarily reorder elements under the same flex parent.

While the "order" property in Flexbox can accept any numerical value, it's important to note that when not all elements 
have an order explicitly defined, those with a specified value will naturally position themselves at the end of the container. 
They will align correctly in relation to other elements that also have an order set, while elements without 
a defined order will default to the start of the container.

The [5-order](./resources/flexbox/5-order) folder contains an example with reordered elements.


## Flex-grow

This property defines the ability of a flex item to grow if needed. 

The default value is 0 meaning no growth can happen.
Putting 1 in each element will make them stretch equally occupying all available space in a row.

Setting it only one element under the same parent will make only that grew. Setting it on multiple element, the browser
will look at the ratio of these grow values to determine exactly how big each element should grow.

## Flex-shrink

Similar to flex-grow, but the other way around. It enables an element to shrink, to reduce in size if necessary to fit.

The next example ([6-grow-shrink](./resources/flexbox/6-grow-shrink)) shows both a flex grow and a shrink property in practice.

## Flex-basis

Related to grow and shrink, it kind of like sets a starting place before the elements begin to grow or shrink. We can treat
it similarly to setting some minimum or maximum sizing on elements in relation to flex grow or shrink.
Indeed, if set to auto, the browser will look up the respective width or height values.

Let's show this with an example as well: [7-basis](./resources/flexbox/7-basis).
The width of the children is set to 300px, however as by default flex elements will stretch - all of them will grow. 
However, when the element with the "c111" class reaches a width of 400 pixel, it alone will grow further, as starting
from the point the `flex-basis` property was set, it is the only element having a `flex-grow` property.

## Align-self

The same as the align-items property for the parent (as in aligning items on the secondary axis), but using it on a single
element we can override the alignment of them individually.

Can take the same properties as align-items.

Align-self examples are shown in the [8-align-self](./resources/flexbox/8-align-self) folder.

