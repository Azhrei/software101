# Instructions for Chapter 2 Lab

### Part 0 (background)

1.  If you are ever asked by `PyCharm`, "Project configurations files
    can be added to Git", select **Don't Ask Again**.
    
2.  The lab steps below will sometimes tell you to right-click on
    `software101` and choose a Git option, and other times will tell you
    to right-click on `ch01_overview` and choose a Git option. It
    doesn't actually matter which one you use, as Git operations apply
    to the entire project, not individual pieces. I use both in this lab
    to demonstrate that they operate the same way.

### Part 1 (committing changes)

1. Using `PyCharm`, find the `ch01_overview` directory and the
   `python_info.py` script that you executed in the previous lab.
   Double-click the file in the **Project** panel so that it opens a tab
   on the right-hand side.
   
2. Edit the script and remove the string `'path'` from the `for` loop.
   Also remove the trailing comma on that string as well. The result
   should look like this:
   
   ```python
   for item in ('version', 'implementation'):
   ```

3. Save the file.

4. Right-click on the `ch01_overview` directory and choose _Git > Commit
   Directory..._ This will cause `PyCharm` to invoke Git and tell it to
   commit all changes in the directory to the repo.
   
5. A window will open in which you should type a commit message. For our
   purposes, just use "First change" and then click **Commit** in the
   bottom right corner.

6. You've now saved your changes. Let's say you've made several commits
   and you're ready to publish your code so that other programmers will
   have access to it. Normally, you don't publish your code unless it
   has passed all of its unit tests and other requirements.
   
7. Publishing your changes means making them available to other
   programmers. We do that by _pushing_ the changes in our repo to
   wherever we got the repo from. In our case, that would be the `https`
   URL that you used in the previous lab.
   
8. Unfortunately, we can't do the _push_ operation. I can't have
   students pushing code to my repository on GitHub! So let's just
   pretend that we did and move on to the next step.

### Part 2 (multiple developers working on the same project)

1. First, create a new branch to represent a bug fix. Right-click on
   `software101` in the **Project** panel and select _Git \> Repository
   \> Branches..._
   
2. Select _New Branch_ and enter `bug123` as the name of the branch.
   Leave the **Checkout** checkbox turned on and click **OK**.

3. Go back to the `for` loop in `python_info.py` and remove the
   `'version'` string time, and its trailing comma. Save the file.

4. Right-click on the `ch01_overview` directory and choose _Git > Commit
   Directory..._
   
5. A window will open in which you should type a commit message. For our
   purposes, just use "Second change" and then click **Commit** in the
   bottom right corner.
   
6. Your changes have been committed to the `bug123` branch. They are
   _NOT_ part of the main branch, called the _master_ branch. I'll prove
   it to you.

7. Switch back to the `master` branch by right-clicking on `software101`
   and choosing _Git \> Repository \> Branches..._ and then clicking on
   _master_ and choosing _Checkout_.
   
8. You should see the content of `python_info.py` revert back to the
   value it had before, meaning that the word `'version'` should come
   back! (Removing that word was part of a different branch and those
   changes are stored in that branch, not in _master_.)

9. However, we want the bug fix incorporated into the _master_ branch.
   Let's merge the changes from that branch into the current one.
   Right-click on `software101` and choose _Git \> Repository \>
   Branches..._ and then click on `bug123` and choose **Merge into
   Current**.

10. Look at `python_info.py` and you'll see the changes from `bug123`
    are now there! At any point, you can use the right-click menu to
    choose _Git \> Show History_ and see what has been committed or
    merged to whatever you right-clicked on; right-click on
    `software101` to see its history, or right-click on `ch01_overview`
    to see its history.

11. All done! Get up and stretch before we continue on...
