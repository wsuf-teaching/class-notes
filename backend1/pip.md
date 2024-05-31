## pip

Python packages are collections of Python modules that extend the functionality of the base language. These packages cover a wide range of functionalities, from web development and data analysis to machine learning and artificial intelligence.

Pip is the package installer for Python. It's a command-line tool that allows us to install, manage, and uninstall Python packages and their dependencies from the Python Package Index (PyPI) and other package indexes.

* We can install a package using pip by running `pip install package_name`.

* To see a list of all installed packages and their versions, we can use the command `pip list`.

* If we have a `requirements.txt` file listing all the packages our project depends on, we can install them all at once using `pip install -r requirements.txt`.

* If we want to remove a package, we can do so with `pip uninstall package_name`.

* We can upgrade a package to the latest version using `pip install --upgrade package_name`.

* We can search for packages available on PyPI using `pip search search_query`. (Searching for functionalities we need in Google may be better for this use case though).

* To generate a `requirements.txt` file with all the packages currently installed in our environment, we can use `pip freeze > requirements.txt`.

## venv

The `venv` module in Python is used to create isolated virtual environments and is represented as a self-contained directory that contains a Python installation for a particular version of Python, along with a number of additional packages.
It allows us to manage dependencies for different projects separately. We can have different versions of certain packages installed in different projects as each virtual environment is isolated from the others and from the system Python installation. This prevents dependency clashes and ensures that changes in one environment don't affect others. Furthermore, using venv helps in making projects more reproducible. By documenting the dependencies in a `requirements.txt` file, we can recreate the same environment on different machines (kind of like npm with the use of package.json).

### Installing, activating, deactivating

To create a virtual environment, run the following command creating a directory named `env` that contains the virtual environment.

```bash
python -m venv env
```

To activate the created environment, run the appropriate command from below:
   
- On **Windows**:
    ```bash
    env\Scripts\activate
    ```
- On **macOS/Linux**:
    ```bash
    source env/bin/activate
    ```
   
After activation, your command prompt will change to indicate that the virtual environment is active.


Once the virtual environment is activated, you can install packages using pip just as before. For example:

```bash
pip install numpy
```

This installs the package inside the virtual environment, not globally.


When you’re done working in the virtual environment, you can deactivate it by simply running:

```bash
deactivate
```

### Using a `requirements.txt` File**:
   
To freeze the current environment's packages into a `requirements.txt` file, use:

```bash
pip freeze > requirements.txt
```

To install the packages listed in a `requirements.txt` file into any virtual environment, use:

```bash
pip install -r requirements.txt
```