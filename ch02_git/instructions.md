# Instructions for Chapter 2 Lab

### Part 1 (clone the `software101` repo and modify it)

1. Open a `Terminal` prompt if you don't have one open already.
Then execute `cd` by itself, that'll put you into `student`'s home
directory.

1. Clone the `software101` repo into another directory named `copied`.
You can use this command:  `git clone software101 copied`.

Normally, the source repo would be remote and you'd use an `https://`
or `git://` prefix to access it, but cloning a local repo is perfectly
valid as well.

2. At any point throughout this lab, you can execute `git status` or
`git log` to see the current state of the repo (some lab steps will
tell you to run these commands, but you can do so at any time)

2. Modify two existing files and create a new file (your choice as
to which ones); you can use `PyCharm` for this, but be sure you're
in the correct directory!  That will require using the _File_ menu
and choosing _Close project_, then selecting the new directory from
the `PyCharm` window that appears

3. Run `git status` to see the result.

4. Now we're going to commit our changes into the git repo.  You
will be thrown into `vi` in the next command if you don't specify
a different editor, so let's change it to `nano` instead.  Execute
`export EDITOR=nano` before running the next command and it'll use
that editor instead of `vi`

Run `git commit` and notice only the two modified files are
represented, not the new one you created.  Exit without committing.

5. Run `git add .` to add the new file to the repo's index

6. Run `git status` to see the result.

7. Run `git commit` again and notice all three are included (since you
terminated the previous commit, the two modified files are still shown)

### Part 2 (multiple developers working on the same project)

1. Create a new branch by executing `git checkout -b bug123`

3. Modify a file and commit it

4. Switch back to the `master` branch with `git checkout master`

5. Merge the change by executing `git merge bug123`.  This simulates
someone else making a change in the "bug" branch and you merging in
their changes.

6. Run `gitk` to view the commit tree graphically
