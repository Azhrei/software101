# Instructions for Chapter 1 Lab

### Part 0 (setup)

1. Open `Terminal` and navigate to the `software101` directory by
typing `cd software101` and pressing _Enter_ at the command prompt.
Execute `git pull` to pull any updates to the GitHub repository down to
your virtual machine.

2. You'll do this as the first step of every lab to download the
latest and greatest changes.  (In reality, unless changes have
actually been made, you can skip this step.  But it's not difficult,
so doing it is the safest play.)

### Part 1 (overview of `PyCharm` and Python)

1. Execute `PyCharm`.

2. Close the _Tip of the Day_ window when you're done reading the tips.  (I invariably find one that I didn't know about and end up reading two or three each time I start `PyCharm`!)  You can deselect the checkbox if you don't want the window to show up the next time you start `PyCharm`.

3. Inside the Project panel on the left, you should see the `software101` folder.  Click the arrow to the left of it to see the expanded contents of the folder.

4. Now click again on the arrow to the left of the `ch01_overview` folder.

5. Double-click on `python_info.py` and the contents of that text file will be shown in a separate tab on the right.  (You can go into _File > Settings..._ and change font sizes and such, if you like, but we won't be doing that as part of the lab.)

6. Run the code by right-clicking somewhere in the source code and selecting the _Run 'python\_info'_ option that's about half-way down the popup menu.

7. A new tab will open below the others that shows the output of the script.  Please spend a few minutes examining the output and we'll discuss the particulars during the lab review. (If you're the curious type, you can examine the other options on the right-click menu, or even browse through the pulldown menus at the top of the window.  I frequently do this when using a new application for the first time, just to get an idea of the kinds of options that the application supports.  Don't be shy about trying them to see what they do!)

### Part 2 (optional demonstration of Jupyter)

0. This part is optional.  If you have time and want to try these steps,
please do so, but they're not used within Cisco and the lab review
may or may not cover them.

1. We'll now try something that doesn't involve `PyCharm`.  (`PyCharm`
is great, but you have to install the application.  Let's try a
browser-based editor that stores all of its results on a remote
server.)

2. Open a `Terminal` and type `jupyter-notebook`, then press _Enter_.

3. You'll see some output scroll in the terminal window (maybe a dozen lines or so), and then a browser window will open that obscures the terminal.  This is the main browser-based interface to `Jupyter`.

4. Click on `software101`.

5. Click on `ch01_overview`.

6. As you might guess, you're now in the same directory as you were when using `PyCharm`.

7. You should see the `python_info.py` script that you just ran.
(If you click on it, you'd be able to edit it within the browser
and save it when you are done, but we're not going to do that right
now.)

8. You should also see the `python_info.ipynb` as well.  Click on
it and a new browser tab will open that shows the content of this
file.  This is called an _IPython Notebook_.  We'll discuss how a
notebook works during the lab review, but feel free to click around!

9. When you're done reviewing the notebook, you can close all of
the browser tabs (and the browser window, too).  If you have made
changes that you want to keep, use the _File_ menu or click on the
_Save_ icon (at the far left end of the toolbar).
