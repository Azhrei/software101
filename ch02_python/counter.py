#!/usr/bin/env python3.7

"""
Counts the number of times a particular hostname appears in an FTP
server log file.  The goal is to show how easily a Python script can
create such aggregate data.

For the lab:

1.  Open this script in `PyCharm`.

2.  Right-click inside the source code somewhere and choose the "Run"
    option.

3.  Examine the output that is produced.  Are they correct?

    Of course, you can't know that unless you actually look in the
    logfile being used for input and verify it.  Go ahead and do that
    now.  I'll wait.  (First, you'll need to figure out what the log's
    filename is.  Search the source code for that information.)

4.  What if the filename were wrong?  What would the output look like?
    Let's find out...

    Change the contents of the `log_file` variable to a filename that
    doesn't exist (adding an extra character at the beginning of the
    filename is probably the easiest thing to do).  Run the script
    again.

    The result is a pretty ugly mess, right?  Let's clean it up.  We'll
    do that the same as the previous script:  adding a try-except block.

    Add a line above the "with" statement that contains only, "try:".
    You'll need to indent the "with" statement and the lines following
    it, down to the end of the "with" block (about 10 lines).

    Add a line below the "with" block and contains only "except:".  When
    you press Enter, `PyCharm` will indent the following line.  Add a
    print statement and then terminate the script.  It will look
    something like this:

        except:
            print("Can't process file '{0}'.".format(log_file))
            sys.exit(1)

    Notice the use of `sys.exit(1)`?  You might also notice that there's
    an import statement for `sys` that up until now, wasn't being used.
    In fact, `PyCharm` should've had it grayed out until you added those
    three lines, above.

    Run the script again.  Much better error message this time, right?!

    Extra credit:  What possible errors could occur inside the "with"
    block that the try-except will capture?  How did you figure that
    out?

5.  If you think you'll have time left, try playing with the formatting
    of the output.  You did some of that in the last script, but I want
    you to try something different in this one.

    First, swap the output fields so that the value is printed first,
    then the client IP address/hostname.  Do this without modifying the
    `print()` statement at the bottom of the script.  Run the script to
    make sure it works as expected.  (It should print the quantity
    first, then the IP address/hostname.)

    Now add some formatting to the numeric field so that it is always
    four characters wide (in other words, pad the value with spaces so
    that the numeric fields all line up).  Run the script again and
    notice how it looks _so_ much better with the numbers lining up!
"""

import sys

FORMAT = "{0} {1}"

# Look inside the log file and you'll see it has fake data...  but it's
# good enough for our purposes here.
log_file = 'xferstats.log'

# Do you remember what this data type is called?  Ten extra points on
# the test if you can name it!
quantity = {}

with open(log_file, encoding='utf8') as f:
    for line in f:
        fields = line.split()

        # First field is the client IP address for the incoming request
        client = fields[0]
        if client in quantity:
            quantity[client] += 1
        else:
            quantity[client] = 1

# We're done reading the file.  Now we sort by IP address.  The results
# of `quantity.items()` is a list of all keys and values in the
# dictionary, one at a time.  Which is perfect, because that's just what
# the `sorted()` function requires!
results = sorted(quantity.items())

for k,v in results:
    print(FORMAT.format(k, v))
