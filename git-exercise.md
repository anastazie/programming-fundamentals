# W3 - Git

1. Create repository on GitHub, e.g. `inspirational-quotes` and clone repository to your computer


1. Create file `quotes.md` locally in repository 


1. Write your favourite quote in `quotes.md` and commit changes


1. Check repository status 


1. View the log of commits

1. Push the commits to the server

1. Create new branch, e.g. `education-quotes`

$ git checkout -b new_branch
Edit your new file and commit the result

Swap back to the master branch

$ git checkout master
Merge new_branch to master

$ git merge new_branch
Now create conflicting commits in new_branch and master and try to merge them. Note the conflict-resolution markers will look something like this.

<<<<<<< HEAD
This is the new line in master
=======
This is the new line in branch
>>>>>>> branch
resolve the conflict (i.e. edit the conflict markers to match how you want the file to look like) and commit the result. Use git log to see the resulting commits on the master branch.
