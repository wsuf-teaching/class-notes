# Command line basics

Knowing how a terminal works is essential for any developer. This document is meant as a quick recap or re-introduction to the very basics already discussed in class.

It will follow the structure of the [class exercise](https://moodle.wsuf.hu/mod/assign/view.php?id=786) just as we did during the exercise session.

We will go through the same exercises on both Windows, and through the git-bash command line on a linux-like system as well.

More in-depth discussion of useful commands and utilities in linux will come at a later time. Now we will focus on certain commands on a need to know basis. Lastly, the capabilities of what we can do now with git-bash is also limited.

# 1. Windows command line basics

If we enter "cmd" from the start menu, the default folder it will have opened is the Home of the currently logged in user, which will suffice for now. In a few minutes we will learn how to navigate between them.

## 1.1 creating and removing directories

We start by creating a directory in which we will work throughout the first exercise.

```
mkdir exercise1
```

This created the folder named "exercise1".
As ```mkdir``` is an abbreviated short for "make directory" we also have its counterpart that is ```rmdir``` for removing a directory. The usage is the same.

```
rmdir exercise1
```

As now we no longer have the directory, we need to recreate it again. Luckily enough, we already know how:

```
mkdir exercise1
```

## 1.2 showing directory contents, changing working directories

A useful command to know is ```dir``` which displays a list of a directory's files and subdirectories.


> PRO TIP: you can learn about commands and their parameters from either the [official Microsoft knowledge base](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/dir), or running the command with the /? parameter.

Continuing on with the abbreviations, we have ```cd``` that stands for "change directory". Enter the folder we just created:

```
cd exercise1
```

## 1.3 creating directory hierarchies

With mkdir, we can create multiple folders all at once by supplying it with a space or comma separated list.

```
mkdir dist, src
```

Also hierarchies:

```
mkdir src\blueprints src\models src\models\database
```

> Now it is your task, to create the second half of the structure. Templates and its subdirectories.

<details>
    <summary>solution (<i>click to expand</i>)</summary>

```
mkdir src\templates src\templates\auth src\templates\index
```

and

```
mkdir src\templates\auth\login src\templates\auth\register
```

...obviously there are many different ways to achieve the same.

</details>

## 1.4 navigating locally and globally

With our known commands, we are not limited to the current working directory. Most of them work either locally or globally on the whole system.

Let's say we are in the ```exercise1\src``` folder. First we enter it

```
cd src
```

Then create a folder back at the ```exercise1``` folder. We can do it from here, without having to change directories back.

```
mkdir ..\data
```

The double dot ".." at the start means the parent directory, or one directory up.

This functionality is the same with ```cd```.
Typing 

```
cd ..
```

will go one folder up in the hierarchy and we arrive back to the ```exercise1``` folder.

Another useful prefixes are the backslash ```\``` which means the root of the current system partition (`C:\` for example) or we can use a global path as well by specifying the whole path the following way listing the contents of the `C:\Users` folder.

```
dir C:\Users\
```

Lastly, if we want to set the current working directory to another partition, cd needs the `/d` option.

```
cd /d d:\
```

![folders](https://i.imgur.com/LEaUHul.png)

## 1.5 creating, reading and deleting files

Getting back on track, our next subtask in the first exercise is creating files.
Of course we can do them visually through some editor like Notepad or VSCode, but through the command line is another option.

> Let's confirm your current working directory first, check if you are at the right place, and if not, navigate back with CD as we have learned.

A command to create a file (or read a file) is ```type```:

```
type nul > .gitignore
```

> We will learn about this later, in a nutshell, we redirect the output of the first command to a file. So from the type command to the .gitignore file in this case.

> Nul is also a special type of file that discards all data written to it while also returning nothing when prompted.

Therefore the command above creates an empty file named ```.gitignore```.

If we want to create another file that has actual text content inside, ```echo``` will be our friend.

```
echo #this is a readme file > README.md
```

This creates the file README.md while also setting its contents to "#this is a readme file".

Listing the directory contents, they are there alright.

![img2](https://i.imgur.com/cfOvXer.png)

As mentioned, ```type``` can also be used to read contents of a file. For example:

```
type README.md
```

To delete a file, the command we need is ```del```.

```
del .gitignore
```

And with that, our ```.gitignore``` file is no more.

> There are various other useful symbols in cmd. One notable is ```&```. If we put it between two commands, it will execute both.

> What would happen if I were to type the following? ```mkdir folder & cd folder & mkdir ..\folder2```

<details>
    <summary>answer (<i>click to expand</i>)</summary>

Creates a folder named ```folder```, enters it, then created another subfolder named ```folder2``` back in the parent folder (notice the ..\ at the start) right next to ```folder```.

</details>

## 1.6 nodejs and batch files, renaming things

You should already have node.js installed on your system.

> If not, install it from [here](https://nodejs.org/en/), regular next-next-finish process. 

If yes, just typing ```node``` in the CMD will launch an interactive node.js console.

> You can exit out of it by either pressing CTRL+D or typing ```.exit```.

Let's use what we have learned, create a js script file from the command line.

```
echo console.log("hello") > greetme
```

I forgot the extension. Even though it is not strictly required, let's fix that. You can use the ```rename``` command to rename a file.

The syntax is ```rename <OLDNAME> <NEWNAME>```

```
rename greetme greetme.js
```

Now we can run the script by typing the following:

```
node greetme.js
```

As we don't want to call node.js every time trying to invoke this script, we make a batch script that will call node with the javascript file as a parameter instead.

Open your favourite text editor and create a file named ```greetme.bat``` with the following contents:

```
@echo off
cd /d C:\Users\YOURUSERNAME\exercise1
node greetme.js
```

> The ```@echo off``` is not strictly needed. If you decide to leave it out however, all the lines of your batch file will be displayed in the command line window while being executed.

Exit out of the folder, for example with ```cd ..``` going one level up. 
Try running the script again.

![img3](https://i.imgur.com/IrbGOAy.png)

> Of fluff!

It's not working, as we did not tell Windows to make it available globally (through environment variables for example). And that is our next step now.

We can open them either from the command line by running the following snippet:

```
rundll32.exe sysdm.cpl,EditEnvironmentVariables
```

or simply searching for ```Environment variables``` in the Start Menu.
In the opened window, among the "User variables for USER" list, find the Variable named ```Path```, open it with "Edit..." and add a "New" value which will be the path to the folder where the greetme.bat (and the greetme.js) file is located.

For example: ```C:\Users\USER\exercise1\```

After saving AND relaunching the command line window, you should be able to run it from anywhere.

## 1.7 groups and users

Going a little bit into system management kind of topics. You all have users, probably passwords as well on your computer. 
While it is quite easy to change it from Settings / Control panel. However, we can do the same from the command line as well.

```whoami``` displays the current active user. You may notice something like ```desktop-blablah\``` before your username. That part is the domain (in this case, localpc, localdomain) name.

```net user``` allows us to display all the user accounts present on the system, while ```net localgroup``` shows the list of groups present.
Furthermore, we can also filter between these, showing what groups a certain user is in with ```net user USERNAME```.

> There are numberous parameters that we can use with the [net user command](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc771865(v=ws.11)).

To create or delete an existing user, one can use the following two commands respectively.

```
net user USERNAME PASSWORD /add
```

```
net user USERNAME /del
```

> You might have to have administration privilages for these to work. From the Start menu, just right click on the command prompt and select the option ```Run as administrator```.

Let's create a user called ```temp```.

```
net user temp /add
```

We can take control of that user even without logging out from our system with the ```runas``` utility. Launch a cmd with the permissions of our new user.

```
runas /user:temp cmd
```

> What would happen if we type ```type nul > C:\Users\temp\text.txt```? And if we type ```type nul > C:\Users\text.txt```?

<details>
    <summary>answer (<i>click to expand</i>)</summary>

The first one would create the file successfully, while the second would most probably fail due to insufficient permissions.

</details>

We can address these pesky permission issues with the net command as well by adding a user to a specific group. More about this at a later course.

```
net localgroup GROUPNAME USERNAME /add
```

Finally, delete the newly created user as we don't need it anymore, and don't want to clutter our login screen with it :)

```
net user temp /delete
```

## 1.8 Network related tidbits

Numerous networking related settings are under the ```ipconfig``` command.

If we use it without parameter, it should display physical and virtual network interfaces present on our system.

```
ipconfig
```

![img4](https://i.imgur.com/hSCw28l.png)

Using it with the ```/all``` option, it displays even more detailed information like physical address, DHCP, DNS and other options as well.

> The integrated help page option (```/?```) works with ipconfig too

Lastly, answering the question of the exercise
```
ipconfig /flushdns
``` 
is the command clearing the OS DNS cache in Windows and 
```
netsh wlan show profile
``` 
is the one displaying available wifi networks.

---
# 2. Linux command line basics

As an additional exercise, let’s do the same in a linux-like environment as well. We will cover the first half of the exercises; creating folders, files and navigating the file system.

First of all, we need git bash for that, as it provides a unix-like environment and emulated bash syntax in its window.

Many of them as you will see work very similarly or exactly the same as their equivalents in Windows.

> IMPORTANT! While usually in Windows, both slash ```"/"``` and backslash ```"\"``` works, on Linux you have to use regular slashes ```"/"```

> All the commands that we will use have very good manual pages which you can access with the ```--help``` option. For example ```cd --help```

## 2.1 creating, deleting folders, navigating the file structure

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

## 2.2 creating, deleting and reading files

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

## 2.4 renaming, moving files and folders

```mv``` can be used to both move and rename files or folders. We ~~rename~~ move the file ```README.md``` to be ```DONTREADME.md``` from now on.

```
mv README.md DONTREADME.md
```

In the meanwhile ```cp``` can be used to copy stuff around. We copy the file ```DONTREADME.md``` and create a new file (while leaving the original alone) called ```README.md``` that would have the same contents as the original.

```
cp DONTREADME.md README.md
```

## 2.3 displaying directory contents

```ls``` lists the content of a directory, ```ls -l``` lists the contents formatted as a list (ll is a shorthand alis of that), while ```ls -la``` lists the hidden files as well.

![ll](https://i.imgur.com/4s4jtg6.png)
From left to right, permissions, owner (blurred), group names, size, last modification date then the name of the files or folders.


## 2.4 Misc useful tidbits vol1

> Alternatives to reading parts of a file are ```head```, ```tail``` and ```less```. Try to find out what they do.

> You can create a sufficiently big file by redirecting the output of ls to a file.
For example  ``` ls -lah /c/windows/system32 > bigfile.txt ```
Then you can run them on it.

> HINT:
![cathint](https://i.imgur.com/Jhljrnn.png)

> From ```less``` you can leave by pressing the ```Q``` button on your keyboard.

## 2.5 creating and running a script locally, text editing in terminal

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

## 2.6 running a script globally

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

## 2.7 Misc useful tidbits vol2

Bash also stores your history of executed commands. You can always check them by typing:

```
history
```

Waht is even more useful, that you can search in the history (in multiple ways). A practical example of this is "reverse-i-search". Press ```CTRL+R``` and start typing a command. If you previously used it, it will show up. Pressing ```CTRL+R``` additional times scrolls between the recent history hits. You can escape out of the history search either by pressing ```ENTER``` executing the currently selected comment or ```CTRL+C``` closing it without doing anything else. 