# npm

npm (node package manager) can help us with frontend development the following ways among others:
* define and run automated tasks and scripts
* run a local web server
* keeping track of used javascript packages

## npm init

Executing `npm init` opens a short step-by-step setup for creating an npm package file.
Options include the name of the package, version number and others. For a trivial example, we can get by by just pressing "ENTER" a few times defaulting all those settings.

After running the command, a file named `package.json` is created in the current folder. If you list the contents of the folder (or open the folder with a graphical file browser), you can see this file and edit it. 

The `package.json` describes a project's metadata, dependencies and other settings in a JSON format and typically resides in the root of the project directory.

Typically it contains the following fields among others:
* `name`: The name of the package or project.
* `version`: The version number of the package or project, following semantic versioning (SemVer).
* `description`: A brief description of the package or project.
* `main`: The entry point file for the package, commonly used for Node.js modules.
* `scripts`: A set of scripts that can be executed using npm commands. For example, you might have scripts for testing, building, or starting the application.
* `dependencies`: The packages that the project depends on in production. These packages are required for the project to run.
* `devDependencies`: Similar to dependencies, but these packages are only needed during development, not in production.
* `author`: The name of the author or maintainer of the package or project.
* `license`: The license under which the project is distributed.
* `repository`: A link to the version control repository (e.g., on GitHub) where the project's code is stored.
* `keywords`: An array of keywords that describe the project, useful for searching and categorization.

* `type`: This specifies the type of module system used in your JavaScript files. It has two common values: 
  * `module` This indicates that your project is using ECMAScript modules. With this setting, Node.js treats all .js files as ESM, and you can use the `import` and `export` syntax.
  * `commonjs` or no type field: This indicates that your project is using the CommonJS module system. This is the traditional Node.js module system, and it's what Node.js defaults to if the type field is not specified.


Not all of these are required, so our newly created (empty) `package.json` might look different missing a few of the fields listed above.

See an example below:

```json
{
  "name": "npm-test",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}
```

## npm install

Above, we have discussed the `dependencies` and `devDependencies` properties.

If we execute the command `npm install` it will install both of them. In our case however no dependencies are listed, so npm will not install anything.

Adding a package name after the command will install that package and also adds it to the `package.json`.

Let's try installing a very small package.

```
npm install left-pad
```

And a little bigger one.

```
npm install moment
```

This in turn will install it putting it into the `node_modules`folder and also adds the package and its version to the `package.json`.

It should look like this:

```
  "dependencies": {
    "left-pad": "^1.3.0",
    "moment": "^2.30.1" 
  }
```

If we want to install a dependency specifically for development environments only, the `--save-dev` switch should be used with the command above.

```
npm install --save-dev live-server
```

This in turn will install the package, adds the `devDependencies` block and puts the package in there:

```
  "devDependencies": {
    "live-server": "^1.2.2"
  }
```

## Dependency version and pacakge locking

Even in this small example we can see that the version is not a fixed number here.

> The syntax for a version number in a package is typically defined by three numbers separated by dots: MAJOR.MINOR.PATCH.
> * MAJOR version: Increments for incompatible ("breaking") API changes.
> * MINOR version: Adds functionality in a backward-compatible manner.
> * PATCH version: Fixes bugs in a backward-compatible manner.

Specifying versions in `package.json`` is quite flexible and can include several operators:

* Exact version: "version": "1.3.0"
* Greater than or equal to a version: "version": ">=1.3.0"
* Less than a version: "version": "<1.3.0"
* Range of versions: "version": "1.3.x" or "version": "1.3.*" (This is equivalent to ">=1.3.0 <1.4.0")
* Caret (^): "version": "^1.3.0". This symbol signifies that  npm should install a version that is compatible with the specified version up to, but not including, the next major version. Specifically, it allows for updates that include new features and bug fixes but not breaking changes.

When installing packages, npm also creats a `package-lock.json` file. This file locks the dependency versions and their transitive dependencies (packages that our dependencies are depending on recursively). This ensures that everyone working on the project uses the exact same versions of dependencies, reducing the chance of inconsistencies across different development environments.
It also helps npm install packages more quickly and reliably by providing a snapshot of the dependency tree with exact versions.

The install process is basically as follows:

* Read `package.json`: npm reads the package.json file to identify the project's dependencies and devDependencies.
* Check `package-lock.json`: If a `package-lock.json` file exists, npm uses it to check for specific versions and their dependencies. This ensures that the exact versions mentioned in `package-lock.json` are installed.
* Install Dependencies: npm installs the specified dependencies based on the information in both `package.json` and `package-lock.json`. It installs the exact versions mentioned in `package-lock.json` for consistency across different environments.
* Update `node_modules`: The installed packages are placed in the `node_modules` directory within your project.
* Then we can use the installed packages in the project we are building.

## Scripts and live server

This section is used to define and run various scripts or commands associated with your project, which then can be executed using the npm command line.

We can run these scripty by typing `npm run <scriptname>` in the command line. Creating an empty package generates one: the test script, which we can run by typing `npm run test`. In turn it will simply print out that no test was specified and exits.

One very useful script we can add now that we have installed 'live-server' (`npm install live-server`) is a script running it.

To add it, edit the `package.json` and under the scripts section, add a new script running it:

```
"start": "live-server"
```

Then your "scripts" section should look like as follows:

```
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
	  "start": "live-server"
  },
```

> So from now on, `npm run start` will launch to live server in our machine.

That live server basically works the same as the live server plugin in Visual Studio Code which we have been using throughout the year. It automatically detects and picks up files and changes to the folder it is executed.

## Using packages for development

Now the installed packages should be usable immediately and without any hassle - providing you are writing an application with javascript only (and no html).

In that case, simply create a new file, let's name it `index.js`, enter the following three lines and run it. (It will also show you what this very small library with its single function can do)

If the package has a type of `commonjs`, the require keyword can be used to make it available for use.

```javascript
const leftPad = require("left-pad");
const moment = require("moment");

console.log('Hello!');
console.log(leftPad('Hello!',20));
console.log(moment().format('MMMM Do YYYY, h:mm:ss a'));
```

> Keep in mind this uses the require.js package automatically available through the node runtime.

If the type of the package is `module`, however you should use the import/export syntax.

```javascript
  import leftPad from "left-pad";
  import moment from "moment";

console.log('Hello!');
console.log(leftPad('Hello!',20));
console.log(moment().format('MMMM Do YYYY, h:mm:ss a'));
```

> Both of these code can be run by typing `node .\index.js` in the console.

However now if we want to use these packages in a regular "web" frontend environment as in HTML + JavaScript + CSS, we will have some trouble.

> If we try to link `index.js` in our HTML file in commonjs mode, it will require `requirejs`. We can install it with `npm install requirejs`, then also include it in the HTML first. 
> Our situation will be pretty similar trying to include them in `module` mode.
> Trying to find it and link all the modules manually from `node_modules` in the HTML will work, but will also prove to be troublesome as well.

## Webpack

Webpack is a popular open-source JavaScript module bundler that is widely used in modern web development. It can take the project's code and assets, such as JavaScript, CSS, and images, and transform them into a format that's optimized for the web. 

```
npm install webpack webpack-cli --save-dev
```

### Loading JavaScript

Let's keep the `package.json` in `commonjs` type for now. Also with the applicable js style:

```javascript
const leftPad = require("left-pad");
const moment = require("moment");

console.log('Hello!');
console.log(leftPad('Hello!',20));
console.log(moment().format('MMMM Do YYYY, h:mm:ss a'));
```

Let's also add a new file called `webpack.config.js`. It's content should be as follows:

```javascript
const path = require('path');

module.exports = {
  entry: './index.js',
  output: {
    filename: './bundle.js',
    path: path.resolve(__dirname, 'dist'),
  },
  mode: 'development'
};
```

This sets up the configuration for webpack. The `entry` specifies the entry point of the application. Webpack will start bundling the code from this entry point.

The `output` section configures the output of the webpack build. The `filename` specifies the name of the bundled file that will be generated and `path` specifies the directory the output file will be placed.

The `mode` specifies `development` or `production` mode with the latter also minifying the code.

A shortcut can also be set up in the `package.json` to run webpack. Un der the `scripts` block, add the following line:

```
    "build": "webpack"
```

From now on, `npm run build` can also be used to execute webpack.

In the HTML, simply import the bundled javascript file as normally.

```html
    <script src="./dist/bundle.js"></script>
```

To get it working with the `module` syntax (import and export), the following changes have to be made:

1. Remove the `"type":"commonjs"` line from the `package.json`.
2. eExtend the `webpack.config.js` as follows:
```javascript
const path = require('path');

module.exports = {
  externalsType: "module",
  entry: './index.js',
  output: {
    filename: './bundle.js',
    library: {
        type: 'module',
    },
    path: path.resolve(__dirname, 'dist'),
    libraryTarget: 'module',
  },
  mode: 'development',
  experiments: {
    outputModule: true,
  },
};
```

The import in the index.html should now be module:
```html
    <script type="module" src="./dist/bundle.js"></script>
```

Now we should be able to load the regular import syntax as well:

```javascript
import leftPad from "left-pad";
import moment from "moment";

    console.log('Hello!');
    alert(leftPad('Hello!',20));
    console.log(moment().format('MMMM Do YYYY, h:mm:ss a'));
```

### Loading Styles

To bundle styles we need a loaders that will solve this problem for us automatically. Simply install them:

```
npm install --save-dev style-loader css-loader
```

Then add the module block in `webpack.config.js`:

```
  },
  module: {
    rules: [
      {
        test: /\.css$/i,
        use: [
          { loader: "style-loader" },
          { loader: "css-loader" },
        ],
      },
    ]
  }
```

Now it will automatically pick up any USED css file. To use them, import them in the javascript: `import "./index.css"`.

And of course also create the `index.css` as well:
```
* {
    background-color: red;
}
```

## A webpack starter kit

[Linked here you will find an example starter project that you can use to ease up development.](https://github.com/wsuf-teaching/webpack-starter-kit)
It has all the necessary packages to run a live server, automatic compilation of resources including css and js with webpack as well as linter (static code analysis tool) to help you write better code with consistent formatting.

The README.md note for that project includes details on how to use and set it up.