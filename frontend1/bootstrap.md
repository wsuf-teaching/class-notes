# Bootstrap

Bootstrap is a popular open-source front-end framework that simplifies the process of building responsive and visually appealing websites.

One of the key features of Bootstrap is its flexible grid system, which is designed to create responsive layouts.

In practice, using bootstrap is about adding the necessary classes on our elements, as easy is that.

## Setting it up

To work with bootstrap we need to import it either through a "CDN" (Content Delivery Network) link, downloading its core files manually
or installing it through a package manager like NPM.

We can choose always up-to-date commands fitting our specific needs from [Bootstrap's official site](https://getbootstrap.com/).

## Grid

### Containers

The grid system is based on a 12-column layout and is implemented using a combination of container, row, and column classes.

Containers, denoted by the `container` class, act as the outermost wrapper for the content.
They are used to contain, pad, and (sometimes) center the content within them.

```
<div class="container">
   [...]
</div>
```

Containers are responsive, and depending on the exact "version" used, can have different sizes with different breakpoints in them.
See the table snippet from Bootstrap's official page below:

![bootstrapcontainerbreakpoints](https://i.imgur.com/dQMhCV3.png)

### Rows

Within containers, content is organized into rows using the `row` class.
The row class is used to create horizontal groups of columns.

```
<div class="container">
   <div class="row">
      [...]
   </div>
</div>
```

We can justify the content in various ways.
For example to the, left, right or center using further pre-defined classes on our rows.

* justify-content-start
* justify-content-center
* justify-content-end
* justify-content-evenly

### Columns

And lastly columns are designated with classes to define the width of each column.
As discussed above, a row can contain a maximum of 12 columns.

![columns](https://i.imgur.com/KI3dQMs.png)

The snippet below creates two rows. The first row hosts 2 columns, while the second row hosts 3.

```
<div class="container">
  <div class="row">
    <div class="col-md-6">1/2</div>
    <div class="col-md-6">2/2</div>
  </div>
  <div class="row">
    <div class="col-md-4">1/3</div>
    <div class="col-md-4">2/3</div>
    <div class="col-md-4">3/3</div>
  </div>
</div>
```

> Notice how all colum "numbers" add up to 12. If we were to go above 12, the columns will automatically wrap to a new line as a line can only take 12.

By adding multiple col classes with different breakpoints we can make the layout behave differently across different device sizes.

In the following snippet, we modify the previous code in such a way that every column appears like a row, nicely below each
other in small screens.

```
<div class="container">
  <div class="row">
    <div class="col-12 col-md-6">1/2</div>
    <div class="col-12 col-md-6">2/2</div>
  </div>
  <div class="row">
    <div class="col-12 col-md-4">1/3</div>
    <div class="col-12 col-md-4">2/3</div>
    <div class="col-12 col-md-4">3/3</div>
  </div>
</div>
```

We can also reorder columns using the `order-1` to `order-5` classes.

Offset classes are also present if we want to increase margins in a specific row, or in between elements.
The syntax for them are `offset-[BREAKPOINT]-[NUMBER]` with breakpoint options being the same as col and container breakpoints, and numbers being in the range of 1-11.


### Bootstrap additions

In addition to the grid system, Bootstrap provides a wide range of pre-designed components, 
such as navigation bars, forms, buttons, and more, to help developers build web interfaces faster.

Learn more about various Bootstrap components here from their [official documentation site](https://getbootstrap.com/docs/5.0/getting-started/introduction/).


