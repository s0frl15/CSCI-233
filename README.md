# CSCI-233
Project repository for Application Program Development. 

If you haven't already, go ahead and install git on your computer. This will allow you to access the project directly from your IDE.

How to install git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

Once you have git installed, create a project folder on your computer and clone this repository in that folder. In VS Code, you can do this by pressing Ctrl+Shift+P to pull up the Explorer window and typing in Git: Clone.

Note: You may have to link VS Code to your github account, but VS Code should walk you through this the first time you try to clone a directory.

Once you have successfully cloned the repository, you should see all the project files from github in your IDE.

While git has many commands that may be usefull, for this project you will mainly be using push and pull.

Push allows you to overwrite a branch on github with your local files, while pull allows you to overwrite your local files with the files from that branch.

It is VERY IMPORTANT that you only use the push command if you know for certain that your local files are 100% updated and only adding to what is already contained on the github page. It is incredibly easy to lose progress because of this. For instance, if person A pushes a change to the repository, and then person B tries to push a change to the repository without first pulling the repository with person A's change, then person A's change will be lost. This can very quickly make it messy to recover the project.

To circumvent this problem, Github has implemented branches. Branches can be thought of as copies or versions of a project. You have your main branch, and then you have sub branches. 

The main branch will contain only files and changes that have first been approved to be moved from a sub branch. You can think of this as a checkpoint of sorts. 

The sub branches are copies of the main branch which may contain updates that have not been finalized. Always push your changes to a sub branch first, so that we can later determine as a group if those changes are ready to be moved to the main branch.

When you are ready to commit to a branch, do the following:
1. Make sure your local files are updated (save a backup somewhere just in case)
2. Go to your terminal in your project directory and type:
   git add .                                     (This will add all of your changes to the staging area)
   git commit -m "Commit message goes here"      (Be sure to include a meaningful message indicating what was changed)
   git push origin <localbranch:remotebranch>
NOTE: you can find the name of your local branch by running the command "git branch". Remote branch will be the name of the branch you are pushing to.

For example, on my machine I would run:
   git add .
   git commit -m "I am making a change to the README"
   git push origin main:test

Hope this helps! -Antony
