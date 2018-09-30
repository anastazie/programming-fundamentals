# W2 - terminal exercise


1. Using [this tutorial](http://swcarpentry.github.io/shell-novice/setup.html) from Software Carpentry, download [data-shell.zip](http://swcarpentry.github.io/shell-novice/data/data-shell.zip) folder and extract it to the Desktop.

    - **Warning**: depending on the language settings in your computer your desktop can me named differently (e.g. Plocha in Czech)

**For the following questions write answer and code to produce that answer**

2. How many folders are there? (Hint: use `ls` with appropriate parameter to print only directories)
  BONUS: using pipe print just the number of folders

3. Move to `molecules` folder in `data-shell`. In what folder will you be by typing `cd ../..`?

4. In `molecules` folder, sort files by file size in descending order (biggest files at top). What is the name of the first file?

5. Rename `creatures` directory to `non-existent creatures`. What do you see when you go into thet directory and type `pwd`?

6. Copy all files from `molecules` directory to north-pacific-gyre. What command will you use?

7. Now, put everything as it was before step 5 and 6. What commands will you use?

8. Create empty file and name it `random_stuff.txt`. What command will you use?

9. Print to the file created in previous file output of `ls -l` of current directory. What do you see when you open that file ?

10. Remove file `random_stuff.txt`. What command will you use?

11. BONUS: using pipes create command that:
    - Read `planets.txt` file in `data` directory
    - Remove first row (header)
    - Search for `WASP` in file
    - Prints number of lines

    
