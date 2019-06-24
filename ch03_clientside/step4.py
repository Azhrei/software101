#!/usr/bin/env python3.7

"""
Grabs an HTML page off the web and extracts a table of data.
Due to the ever-changing nature of the web, this script will likely need periodic
updates as the format of the web page changes.  Because of that, we will check that
the overall structure is what we _expect_ it to be, and if it isn't, we'll print a
warning to the user -- but we'll still print out whatever data we find.
"""

import sys
import requests
from bs4 import BeautifulSoup

FORMAT_TITLE = "Page title: '{0}'"
FORMAT_ARTICLE = "{0:>2}. {1}"

url = "https://www.nist.gov/topics/cybersecurity"

# If you need a proxy to get to the Internet, fill in the data here, then change which line is commented
# out, below.
my_proxies = {
    "http": "http://your.proxy.info/here",
    "https": "http://your.proxy.info/here",
}

# There are two lines here, but only one is needed.  If you need a proxy configuration to get
# to the Internet, move the comment from the first line to the second and adjust the `my_proxies`
# variable, above.

# response = requests.get(url, proxies=my_proxies)
response = requests.get(url)

# Print a list of all topic headings that appear under the "News and Updates" section.  TO do this,
# we must parse the HTML content into separate fields, then search for the pieces we want.

# Start by convert the HTML into a Python object.
soup = BeautifulSoup(response.text, 'html.parser')

# Here's an example of selecting a particular field from the HTML.  Without the `.text`, it would
# print the HTML, such as '<title>Cybersecurity | NIST</title>' and we don't want all that extraneous
# HTML stuff.
print(FORMAT_TITLE.format(soup.title.text))

# Now find 'div.newspaper-icon'
# Inside there, look for 'div.view-content'
# Inside there, look for all 'article div header h3' and extract the .text for printing
nodes = soup.select('div.newspaper-icon div.view-content article h3')

# When `enumerate` is used in a loop, it returns one element from the list, but also returns
# a counter that automatically increments each time through the loop.  That's why there are
# two variables listed in the `for` loop:  the counter, and the actual data.
for num, node in enumerate(nodes, 1):
    print(FORMAT_ARTICLE.format(num, node.text))
