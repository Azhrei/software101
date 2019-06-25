# Instructions for Chapter 5 Lab

### Part 0 (setup)

1. Open `Terminal` and navigate to the `software101` directory by
typing `cd software101` and pressing _Enter_ at the command prompt.
Execute `git pull` to pull any updates to the GitHub repository
down to your virtual machine.

### Part 1 (clone the `software101` repo and modify it)

1. Open a `Terminal` prompt if you don't have one open already.
Then execute `cd` byt itself, that'll put you into `student`'s home
directory.

1. Clone the `software101` repo into the current directory

2. Modify two existing files and create a new file

3. Run git status to see the result.

4. Run git commit and notice only the two modified files are represented.  Exit without committing.

5. Run git add to add the new file to the repo.

6. Run git commit again and notice all three are included.

7. Transition: “But what about multiple developers working at the same time?”

8. Create a new branch by executing git checkout -b bug123

9. Modify a file and commit it

10. Switch back to the master branch with git checkout master

11. Merge the change by executing git merge bug123

12. Run gitk to view the commit tree graphically
