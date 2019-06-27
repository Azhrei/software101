#!/usr/bin/env python3.7

"""
Converts Fahrenheit temperatures to Celsius.  Incoming temperatures can
be placed on the command line.  If no temperatures are provided, a
hard-coded list of temperatures built into the script will be used.

For the lab:

1.  In order to add temperatures to the command line from inside PyCharm,
    run the script once to create a "runtime configuration".  Then use the
    Run > Edit Configurations... menu option.  In the dialog that opens,
    select this script from the list on the left.

    Now you can put command line parameters into the "Parameters"
    field on the right-hand side of the panel.  Add the string, "100 0 -40"
    and then click OK.  Now run the script again.  You should see the
    conversions for those three temperatures.

2.  Change the command line parameters again and choose your own values.
    Pick at least two negative numbers and two positive numbers.

3.  Change the format string so it uses "9.1f" instead of "6.2f" in both
    places.  Now run the script.  Can you explain the difference in the
    output?

4.  Try using "hello" as a temperature on the command line (that would
    be Run > Edit Conifgurations... again).  What happens when you run
    the script?

    Let's fix the error.  We could handle this error a few different
    ways, such as printing the error and continuing to process the
    remaining temperatures, or simply print the error message and abort.
    We're going to do the former.  Start by adding a try-except block
    around the body of the for loop.  The following steps will
    accomplish this.

    Find the "for" loop, below.  On the line following the for command,
    add the string "try:" (note that it's four characters).  `PyCharm`
    will automatically indent the command for you, so the "t" in "try"
    should be in column 4.

    But that's a problem, because the rest of the loop is NOT indented
    and thus won't be considered to be inside the try-except block.  So
    indent all of the remaining lines (all lines below the "try" line)
    by 4 spaces.  You should be able to highlight those lines and type
    TAB to cause them to shift over by 4 spaces.  (If it doesn't work,
    just indent them manually, one by one.)

    Add a new line at the very bottom of the file that contains only
    "except:".  Again, `PyCharm` should take care of indentation for
    you.  You should find that the "try" and the "except" are at the
    same indentation level.

    Add a line below "except" that prints an error message.  For
    example:

        except:
            print("Can't convert '{0}' to floating point.".format(temp))

    (We will discuss what that is doing more in the lab review.)

    Run the script again and watch what happens when it gets to the
    string "hello".  Change the command line parameters again and give
    it a number, the word "hello", and another number (thus proving that
    it's handling the word properly by printing the error message but
    otherwise ignoring it).
"""

import sys

# I like putting my format strings at the top of the script, so it's
# easier for other programmers to find and modify them in the future, if
# necessary.
FORMAT = "{0:6.2f}\N{degree sign}F = {1:6.2f}\N{degree sign}C"

# If there are temperatures on the command line, use them.  Otherwise,
# use the built in values.
if len(sys.argv) > 1:
    temp_list = sys.argv[1:]
else:
    temp_list = ['-40', '0', '32', '212']

# Process each entry in the `temp_list` one at a time.
for temp in temp_list:
    # First, convert the string into a floating point number.
    fahr = float(temp)
    # Now calculate the Celsius value.
    cels = (fahr - 32) * 5 / 9
    # And print it when we're done...
    print(FORMAT.format(fahr, cels))
