# Git

Before g~~e~~itting into git, let's start with adding VSCode into the path if not already there.

> You can check whether it is on the path already by typing ```code``` into the terminal. If it opens, then cool :)

> [Here](cmd-basics.md/) under section 1.6, we have already discussed how to add things to Path.

The default VS Code installation location is usually ```C:\Users\USERNAME\AppData\Local\Programs\Microsoft VS Code\bin\``` that's what you have to add there replacing USERNAME with your actual username.

Following that, we can set the default git editor to VS Code escaping vim (hah!).

```
git config --global core.editor "code --wait"
```

Afterwards now the VS Code window will open (```git config --global -e```), where we can set the rest of the operations to VS Code as well. Modify your configuration according to the values below.

```
[merge]
  tool = vscode
[mergetool "vscode"]
  cmd = code --wait $MERGED
[diff]
  tool = vscode
[difftool "vscode"]
  cmd = code --wait --diff $LOCAL $REMOTE
[core]
  editor = code --wait
```

From then on, various git commands normally requiring a text editor will open in a VS Code window providing a nicer environment than the default terminal editor.

## Installing plugins, and opening a terminal inside VS Code

Throughout this course, we will use Visual Studio Code to look at the state of our git repository visually as well, not just from the command line. To that end, we need to install a plugin to help us out.

To install it, click on the extensions icon on the left side of the window.

![extension1](https://i.imgur.com/Zy4TNoF.png)

then search for it on the top and click on the "Install" button.

![extension2](https://i.imgur.com/JCWjp0M.png)


After installing it, a permanent button will be added to the bottom left of the window.

![extension3](https://i.imgur.com/uPyP0Ih.png)

Last, open the folder where we created our branches in Visual Studio Code.


You can also open a git bash window inside Visual Studio Code. Click on the "Terminal" dropdown on the menu bar at the top left, then click on "New Terminal". A terminal should have opened at the bottom of your window. As it is most probably Windows PowerShell, we should change it to Git Bash by clicking on the dropdown next to the plus (+) sign and then on "Git Bash" like on the picture below.

![gitbashvscode](https://i.imgur.com/J2Tjtb8.png)


# 1. Git fundamentals

Starting from the very basics this time. You set up the git environment last week, but let us quickly check it.
In git bash, type

```
cat ~/.gitconfig
```

and if your user name and e-mail address is present, it should probably be fine now.

## 1.1 Creating a repository, adding files

First let's create a folder called git_project_1 and enter it.

```
mkdir git_project_1
cd git_project_1
```

Once inside that folder, fundamentally there are two different ways to create a new git project. We can either create it online on a git portal like GitHub or locally through either the command line or visually in other programs.

> Along this course, we will continue to use the command line for git, but feel free to try recreating all the steps in your favourite editor later as an additional exercise!

The following command initialises a git repository on the current working folder:

```
git init
```

![gitinit](https://i.imgur.com/PDoW9n6.png)

If you see something like the image above, then you were successful. It created a hidden folder called ```.git``` in the current working directory. We can check it out with ```ls -la```.

Now that git is initialised, we can start working on our new project adding and committing files.

First, let's create a file called ```script.js```.

```
touch script.js
```

Now if we were to check the status of git here:

```
git status
```

![gitstatus](https://i.imgur.com/zd8oO1g.png)

we would see that it says "untracked files: script.js".
Git automatically detects files added to this directory, but we have to manually add them for git to track and store them in version control. Do as the prompt says and add the script to git.

```
git add script.js
```

Create aother file called ```index.html```.

```
touch index.html
```

![indexgit](https://i.imgur.com/gYkjgbz.png)

Now we see that ```script.js``` by now is tracked by git since we added it, but ```index.html``` is not yet.
We can also add multiple files or folders (or everything that is not specified to be ignored by .gitignore) with git add:

```
git add .
```

Checing the status again we should see, that both files are listed under the "changes to be committed section".


## 1.2 gitignore

There is one more important thing we should look into before having our deep dive into commits and the rest.

Consider a case where we have some local file filled with secrets.

Something like the following. Create it and optionally add something inside.

![secrets](https://i.imgur.com/4y1xtNf.png)

Either these, or module or plugin codes that would be installed anyway from some file specifying which ones are used.

Surely we do not want to save all these to git as well?

![nodevendor](https://i.imgur.com/WPkzWpb.png)

A solution to this; namely to ignore and do not add specific files or folder to the git versioning system is gitignore. That is usually one of the first thing we do when creating a git repository and many IDEs automatically do it for us too.

Create the ```.gitignore``` file and add our example ```secret``` file inside and lastly add ```.gitignore``` to git as well.

```
nano .gitignore
```

put a single line with the following inside: ```secret``` then add ```.gitignore``` to git.

```
git add .gitignore
```

> Check out how to use nano [here](cmd-basics.md/).

![gitignore2](https://i.imgur.com/I7ZUp7L.png)

Once again, if everything went correctly, you should see the result above. ```.gitignore``` added, but no sign of the ```secret``` file either in the tracked or committed sections.

## 1.3 ~~git~~ get committed

Commit is one of the core command of git. It records changes from the repository, effectively capturing a snapshot of it's current state. It's usage is very simple.

```
git commit
```

or

```
git commit -m "initial commit"
```

Every commit has to have a commit message. With the ```-m``` option we can supply it right there at the command line. If we do not do it, simply typing ```git commit``` git will launch a text editor where we are prompted to enter one.

![gitcommit](https://i.imgur.com/Warx9rk.png)


## 1.4 reset

Reset, well resets the HEAD to a specific state. With it, we can undo specific changes in our history.

Hard reset is the most dangerous option. Both the HEAD, the working directory and the git history reset as well. This cannot be undone.

To try it out, we add a few commits first as usual

```
echo "change" >> file.txt; git add .; git commit -m "change1"; echo "change" >> file.txt; git add .; git commit -m "change2"; echo "change" >> file.txt; git add .; git commit -m "change3"; echo "change" >> file.txt; git add .; git commit -m "change4";
```

to have something like the following:

![reset1](https://i.imgur.com/8OBHk4y.png)

If we would like to hard reset git to "change1", copy its hash from either Git Graph in VS Code or from git log in your console.

```
git reset --hard COMMITHASH
```

![reset2](https://i.imgur.com/8Sj46AB.png)

A mixed reset is less destructive. It resets the staging index to the state of the specified commit.

Everything else that was added or modified in git after has been moved to the working directory becoming uncommited and unstaged changes.

Add our changes again:

```
echo "change" >> file.txt; git add .; git commit -m "change2"; echo "change" >> file.txt; git add .; git commit -m "change3"; echo "change" >> file.txt; git add .; git commit -m "change4";
```

then reset now with the ```--mixed``` option once again to the "change1" commit.

> Mixed is the default option.

```
git reset --hard COMMITHASH
```

![reset3](https://i.imgur.com/zu2THhk.png)



# 2. Branching out

Everything that we tried so far was in a single user, single branch environment. That may work for you, and our small examples, however it is not realistic and not representative of how git is used at companies. Multiple users, and numerous feature branches are the norm.

> Example:
![branch example](https://i.imgur.com/51TcK5v.png)

> GOOD TO KNOW: when working with remote remote repositories, ```git fetch --all``` gets all the remote branches. In newer versions of git, simply ```git checkout``` should work as well.

## 2.1 Creating and checking out a branch

> For testing it out, we need a clean project, so let's practice everything we have learned so far.
\
- Create a folder in your home directory,
- enter it,
- initialize a local git repository inside,
- add a file named "file.txt" which has a single line "here be branches",
- add this file to git,
- and make a single commit with the message "initial commit".


<details>
    <summary>solution (<i>click to expand</i>)</summary>

with a single copy-pasteable command:
```
mkdir ~/branch-example; cd ~/branch-example; git init; echo "here be branches" > file.txt; git add file.txt; git commit -m "initial commit"

```
or line by line:
```
mkdir ~/branch-example
cd branch-example
git init
echo "here be branches" > file.txt
git add file.txt
git commit -m "initial commit"
```
</details>

To create a new branch, we can use the command ```git branch <BRANCHNAME>```. It will create a new one from the current branch.

Let's say create a branch named ```develop```.

```
git branch develop
```

Using the same command without a name lists all the branches:

```
git branch
```

![branch1](https://i.imgur.com/iauvn81.png)

> Here, the green color and the star signifies that the HEAD (the current branch reference, the pointer to a commit we are on in our workplace) is on the master branch currently. 

The command ```git branch``` does not automatically change our current branch to the newly created one. For that, we can use the ```git checkout <BRANCHNAME>``` command.

```
git checkout develop
```

> We can create and check out a branch at the same time with ```git checkout -b <BRANCHNAME>```

Finally, deleting a branch is just as easy as creating one.
```git branch -d <BRANCHNAME>``` or if it has unmerged changes, in which case a simple deletion would not work: ```git branch -D <BRANCHNAME>```.

> Your HEAD cannot be on the same branch that you want to delete, checkout another one first.


## 2.2 working with branches, merging strategies part 1

Before installing the extension, we checked out the ```develop``` branch, so that's where we should be. Opening the console window on the right it also shows the branch we are on.

Edit our only file, "file.txt". Add a line saying "line added in development".

> Feel free to use VS Code for editing files from now on.

![vscodedit](https://i.imgur.com/V5ZNuH1.png)

> As an IDE, VS Code it shows changes, modifications, deletions and additions line by line in the file we edit. That you can already see with the little blue line next to line 2. Save the file, then commit it from git bash.

```
git add file.txt
git commit -m "added a second line"
```

Then if we try to open the Git Graph window, it should show something along the lines of this:

![vscodegraph1](https://i.imgur.com/9MvaUa3.png)

Now the develop branch as well as the HEAD is ahead of the master branch. However it is still a trivial example, as the master branch will stay the same, making the merging process rather easy.

Merging as you have learned is git’s way of putting a forked history, integrating two branches back together again.

For merging to work, first we have to be on the receiving branch. So we checkout master.

```
git checkout master
```

Then we can try merging it with ```git merge <BRANCH>```. The meaning behind is get the changes from \<BRANCH\> to the currently active one.

```
git merge develop
```

![fastforward](https://i.imgur.com/n66Kvl9.png)

And now the two branches are back together again, and we can also see in the file list that even though we are on the master branch, the second line is present too.

This trivial case of merging is called "fast-forward merge" and it happens when there is a linear path from the current branch to the tip of the receiving branch. In this case git simply combines the histories of the branches. 

An alternative case of merging is a "3-way merge" in which case we are using a dedicated commit to tie together the two histories and the two different versions of file contents. This happens when the receiving branch also sees changes while we are working on an another one. 

Let’s see this continuing our current project. Create and commit a new file on develop.

Checkout develop again, then create and commit a new file.

```
git checkout develop
echo “this is the second file” > file2.txt
git add file2.txt
git commit -m “added file2 on develop”
```

> Once again feel free to use VS Code for creating and editing files from now on instead of using "echo".

Then we go back to master, create and commit a new file there as well.

```
git checkout master
echo "this is the third file on master" > file3.txt
git add file3.txt
git commit -m "third file on master"
```

The result should be the following, where develop branched out, and now has a different history to master which also changed during that time.

![branchout](https://i.imgur.com/mFualhx.png)

We merge them.

```
git merge develop
```

A window might pop up prompting us for the commit message, because we learned in a three-way merge, a dedicated commit is made to wrap the two branch histories together.

![commitmsg](https://i.imgur.com/UsFhOqW.png)

The command line says that we were successful as well.
![mergegitdin](https://i.imgur.com/NPp6zE7.png)

It worked again as there were no conflicts between the files. We integrated the changes made in develop (adding file2) into master.
Looking at the Git Graph we should see the same in a visual way:

![mergedvisual](https://i.imgur.com/Z8CZApw.png)

> You might have to reopen that tab for it to correctly display the merge.

However, if we now checkout into develop

```
git checkout develop
```

we will see, that file3.txt (that we previously made on master) is no longer present. That's because merging changes is a one-way process. We added the changes made in develop to master, but did not add the master changes back to develop.

Now merge master to develop (we will see better ways to do that later).

```
git merge master
```

Notice how once againthe master and develop are pointing to the same commit.

![samecommit](https://i.imgur.com/aeE8y6n.png)

## 2.3 merge conflicts

Now we will create a situation where there is a merge conflict.

While in the develop branch (and that is where we should be already) edit "file.txt" and add two more lines at the end, for example:

```
another line added in development
one more line added in development
```

add and commit them, then checkout master

```
git add file.txt
git commit -m "further development lines added to file.txt"
git checkout master
```

and edit the same file.txt, adding the following two lines at the bottom of it:

```
master line added
master line 2 added
```

Add and commit once again. By now it should be routine :)

<details>
    <summary>solution (<i>click to expand</i>)</summary>

```
git add file.txt
git commit -m "lines added in master"
```

</details>

This as we planned will once again result in diverging branches.

![divergconflict](https://i.imgur.com/60lL1Ny.png)


If we were to try merging here, it would result in a merge conflict that cannot be automatically resolved. Git does not know, whether we want lines 3 and 4 from file.txt in develop, or the lines 3 and 4 from master.

```
git merge develop
```

![mergeconflict2](https://i.imgur.com/cPrtDqC.png)

At this point the git repository is in a MERGING state with the files needing merge conflict fixes being in a funny state that lookes something like this.

![mergenotepad](https://i.imgur.com/CALNImG.png)

file.txt now contains both sides of the conflicting content. You can see some special visual indicators that were not there before.

These are:
- <<<<<<< HEAD
- =======
- \>>>>>>> develop

Lines between ```<<<<<<< HEAD``` and ```=======``` is from the receiving branch (master in our case), and lines between ```=======``` and ```>>>>>>> develop``` are from the merging branch.

If we open the file in VS Code or other editors, we might see the merge conflict annotated with colours and clickable options as well.

![mergevscode](https://i.imgur.com/FdO34HQ.png)

We can accept either the lines from the master (Accept current change) or from the develop branch (accept incoming change), or even both of them.

> You can even delete them all and add arbitrary lines instead, as a new merge commit will be created, in which you can do whatever.

This default file view with the annotation can be more than enough to resolve a conflict, but the merge editor (see button below the file contents) can be another powerful tool for more involved changes.

We can accept changes from only the incoming (develop) branch, 

![mergeinc](https://i.imgur.com/5nw2oVm.png)

or from only the current (master) branch,

![mergecurr](https://i.imgur.com/sZB1SIp.png)

or any combination of the two.

![mergecomb](https://i.imgur.com/FD209Ao.png)

In our case, let's say we would like to have the two lines from the master first, then the two lines from develop and save the commit that way.

![mergefin](https://i.imgur.com/tozbxCG.png)

Clicking on the complete merge button (or if we do this by editing the conflicting file.txt then after saving it) we are still stuck in the MERGING state.

All there is to do now is to commit file.txt to conclude the merge process.

```
git commit -m "finished merging file.txt"
```

![mergefin2](https://i.imgur.com/nFXEpWH.png)

## 2.4 merge conflict useful tidbits

```git log --merge``` shows a list of commits that have conflicting parts between the merging branches.

```git merge --abort``` aabborts the merge and undoes all changes made during the merging process.

If we know which of the version of a file (in its entirety) we need effectively ignoring any and all changes to it from the other branch, we can also use git checkout with specific options.

```git checkout --ours FILENAME``` selects the file from the current branch and ```git checkout --theirs FILENAME``` selects the file from the merging branch.

## 2.5 detached HEAD state

If you get the message "detached HEAD", it is nothing wrong, it is a valid state in GIT. Detached HEAD state happens if you checkout a single commit instead of a branch.

Let's see that through a quick example.

```
mkdir ~/hour2project; cd ~/hour2project; git init; echo "first line" > file.txt; git add file.txt; git commit -m "first line added"; echo "second line" >> file.txt; git add file.txt; git commit -m "second line added"; echo "third line" >> file.txt; git add file.txt; git commit -m "third line added";
```

> You can copy-paste this in one go. It creates three commits, adding one more line to the file each time.

> "\>\>" is the append operator in bash. It does not overwrite the file contents, but inserts to its end.

Then inspecting our repository history with ```git log``` should result in something like this:

![dethead1](https://i.imgur.com/H5FLP4O.png)

We see the commit hashes. We can also checkout them, not only the branches.

Check out one of your previous commit.

```
git checkout COMMITHASHOFSECONDCOMMIT
```

![dethead2](https://i.imgur.com/iInuuLS.png)

VS Code simply shows that we are just at a previous commit - and we are.

![dethead3](https://i.imgur.com/c5THV3S.png)

And the command line will also show that you are at a single commit instead of a tip of a branch.

![dethead4](https://i.imgur.com/yitSuvd.png)

Going back in time, we can start new branches from any point.
