#!/usr/bin/env python3

"""
Demonstrates how Python can retrieve information from the environment that it's running
in.  This lets it tailor itself based on the operating system version, the user credentials,
or even which version of Python is running the script.
"""

import sys
import pprint

print("Values that apply to the running instance of Python:")
for item in ('path', 'version', 'implementation'):
    print("\n{0:=^80}".format(item))
    pprint.pprint(vars(sys)[item])
