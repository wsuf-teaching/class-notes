# Command line basics

Knowing how a terminal works is essential for any developer. This document is meant as a quick recap or re-introduction to the very basics already discussed in class.

It will follow the structure of the [class exercise](https://moodle.wsuf.hu/mod/assign/view.php?id=786) just as we did during the exercise session.

We will go through the same exercises on both Windows, and through the git-bash command line on a linux-like system as well.

More in-depth discussion of useful commands and utilities in linux will come at a later time. Now we will focus on certain commands on a need to know basis. Lastly, the capabilities of what we can do now with git-bash is also limited.

# Windows command line basics

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