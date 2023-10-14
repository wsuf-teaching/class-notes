# Linux terminal basics

As an additional exercise, let’s do the same in a linux-like environment as well. We will cover the first half of the exercises; creating folders, files and navigating the file system.

First of all, we need git bash for that, as it provides a unix-like environment and emulated bash syntax in its window.

Many of them as you will see work very similarly or exactly the same as their equivalents in Windows.

> IMPORTANT! While usually in Windows, both slash ```"/"``` and backslash ```"\"``` works, on Linux you have to use regular slashes ```"/"```

> All the commands that we will use have very good manual pages which you can access with the ```--help``` option. For example ```cd --help```

## 1.1 creating, deleting folders, navigating the file structure

```mkdir``` and ```rmdir``` works exactly like in Windows with a little syntactical difference in their advanced functions.

Creating and deleting a folder:

```
mkdir exercise2

rmdir exercise2
```

Creating folder hierarchies:

```
mkdir {dist,src,src/{blueprints,models,models/database}}
```

We could list separated with spaces (but not commas!) as before, but this is an alternative syntax to it.

What does it mean though?
Between curly brackets, we have a list of items created at the same level in the hierarchy with the slash "/" indicating a subfolder or subfolders.

```
rootfolder
└─ dist
└─ src
   └─ blueprints
   └─ models
      └─ database
```

Changing directories work the same way.
We enter the folder "exercise2" then go back to its parent directory.
```
cd exercise2

cd ../
```

A notable cd command is just ```cd``` or ```cd ~``` which navigates to the user home directory from anywhere in the system.

## 1.2 creating, deleting and reading files

For creating a file, ```touch``` is the command that we need.

```
touch README.md
```

If we also want to have some conent inside, ```echo``` works similarly as its Windows counterpart:

```
echo "#some heading in the readme" > README.md
```

To read a files contents, we can (among plenty others) use ```cat``` to display them in the terminal

```
cat README.md
```

For deleting a file ```rm``` is the way to go.

```
rm README.md
```

```rm``` can also delete folders if used with the ```-r``` option. Let's delete the whole ```src/``` folder structure.

```
rm -r src/
```

## 1.3 renaming, moving files and folders

```mv``` can be used to both move and rename files or folders. We ~~rename~~ move the file ```README.md``` to be ```DONTREADME.md``` from now on.

```
mv README.md DONTREADME.md
```

In the meanwhile ```cp``` can be used to copy stuff around. We copy the file ```DONTREADME.md``` and create a new file (while leaving the original alone) called ```README.md``` that would have the same contents as the original.

```
cp DONTREADME.md README.md
```

## 1.4 displaying directory contents

```ls``` lists the content of a directory, ```ls -l``` lists the contents formatted as a list (ll is a shorthand alis of that), while ```ls -la``` lists the hidden files as well.

![ll](https://i.imgur.com/4s4jtg6.png)
From left to right, permissions, owner (blurred), group names, size, last modification date then the name of the files or folders.


## 1.5 Misc useful tidbits

> Alternatives to reading parts of a file are ```head```, ```tail``` and ```less```. Try to find out what they do.

> You can create a sufficiently big file by redirecting the output of ls to a file.
For example  ``` ls -lah /c/windows/system32 > bigfile.txt ```
Then you can run them on it.

> HINT:
![cathint](https://i.imgur.com/Jhljrnn.png)

> From ```less``` you can leave by pressing the ```Q``` button on your keyboard.

## 1.6 creating and running a script locally, text editing in terminal

Going to exercise 2, we make a simple bash script.
We can naturally do it visually or through various command line utilities. We can also edit texts here in the terminal. A popular command line editor and probably the easiest to use of its kind is called nano.

We can enter it by simply typing nano.

```
nano
```

![nano](https://i.imgur.com/wiWDFjK.png)

Here we can type as we usually would, but the use of computer mouse and therefore the cursor is limited to copy-pasting if we run it in a window, and in a linux terminal-only system it would have no functionality whatsoever.

In the bottom, there are also various options you can see. It can be quite cryptic for first timers.

In the editor, you can navigate around the lines and columns with the ARROW keys. Furthermore you can use the: 

- ```Shift+ARROWKEYS``` to select text

- ```Ctrl+K``` to cut

- ```Ctrl+U``` to insert

- ```Ctrl+W``` to search for

- ```Ctrl+_``` is to jump to a line or column number

- ```Ctrl+O``` writes out the results to the file and 

- ```Ctrl+X``` exits, also prompting file name if we hadn’t created one yet. When it prompts, just enter the name as you usually would.


Getting back to the task, a bash shell script always starts with us telling the operating system to invoke the specified shell or program to execute the commands that we have in our script, then comes the actual content:

```
#!/bin/bash
echo "hello, this is a bash script"
```

Then when prompted name it ```script.sh```

Having it created, we can run it by typing

```
./script.sh
```

> In an actual Linux system first we would have to give execution permission as well, but here we can do without.

![script](https://i.imgur.com/3S32XTO.png)

You may wonder, why the ```./``` at the start. It is to signify, that this script resides in the current working directory.

> You can check the full path of the current working directory with ```pwd```

## 1.7 running a script globally

What we did on windows regarding the environmental variables is also different.
To see what we have, we can echo it out to the console using the following command.

```
echo $PATH
```

> To print all the other environment variables, the command you have to use is ```env```.

We can add a variable locally for the current session through typing the following into the console. However it will no longer work after we close and reopen git bash.

```
export PATH=$PATH:/path/to/folder-we-want-to-add
```

If we want to make this more permanent, it has to be added to the shell configuration variables which in our case is the ```.bash_profile``` file.
It is typically located in the home directory of the user.

Let's create it (or edit it if it exists) with nano!

```
nano ~/.bash_profile
```

and add the export line above into it.

If you were successful, that script can be invoked anywhere from your system by typing:

```
script.sh
```

## 1.8 Misc useful tidbits again

Bash also stores your history of executed commands. You can always check them by typing:

```
history
```

Waht is even more useful, that you can search in the history (in multiple ways). A practical example of this is "reverse-i-search". Press ```CTRL+R``` and start typing a command. If you previously used it, it will show up. Pressing ```CTRL+R``` additional times scrolls between the recent history hits. You can escape out of the history search either by pressing ```ENTER``` executing the currently selected comment or ```CTRL+C``` closing it without doing anything else. 