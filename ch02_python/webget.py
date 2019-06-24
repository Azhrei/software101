#!/usr/bin/env python3.7

"""
Grabs an HTML page off the web and extracts a table of data.

Due to the ever-changing nature of the web, this script will likely
need periodic updates as the format of the web page changes.  Because
of that, we will check that the overall structure of the web page is
what we _expect_ it to be, and if it isn't, we'll print a warning to
the user -- but we'll still print out whatever data we find.

For the lab:

0.  Open the web browser and visit the URL stored in the `url` variable,
    below.  It will be a summary of cybersecurity information.
    Familiarize yourself with the structure and content of the page; the
    script will be loading that same content and extracting a portion of
    it...

1.  Right-click inside the source code and choose the "Run" option.

2.  You should see a summary of the first set of articles that appear on
    the NIST web page for cybersecurity information.

3.  Figuring out what this script is actually doing is quite tricky,
    particularly if your background with HTML is minimal.  Spend the
    remaining lab time reviewing this code and we'll discuss how it
    works in the lab review.
"""

import sys
import requests
from bs4 import BeautifulSoup

FORMAT_TITLE = "Page title: '{0}'"
FORMAT_ARTICLE = "{0:>2}. {1}"

url = "https://www.nist.gov/topics/cybersecurity"

# If you need a proxy to get to the Internet, fill in the data here,
# then change which line is commented out, below.
my_proxies = {
    "http": "http://your.proxy.info/here",
    "https": "http://your.proxy.info/here",
}

# There are two lines here, but only one is needed.  If you need a proxy
# configuration to get to the Internet, move the comment from the first
# line to the second and adjust the `my_proxies` variable, above.

# response = requests.get(url, proxies=my_proxies)
response = requests.get(url)

# Print a list of all topic headings that appear under the "News and
# Updates" section.  TO do this, we must parse the HTML content into
# separate fields, then search for the pieces we want.

# Start by convert the HTML into a Python object.
soup = BeautifulSoup(response.text, 'html.parser')

# Here's an example of selecting a particular field from the HTML. 
# Without the `.text`, it would print the HTML, such as
# '<title>Cybersecurity | NIST</title>' and we don't want all that
# extraneous HTML stuff.
print(FORMAT_TITLE.format(soup.title.text))

# Now find 'div.newspaper-icon'
# Inside there, look for 'div.view-content'
# Inside there, look for all 'article div header h3' elements and
# extract the .text for printing (this last part is done in the loop,
# below).
nodes = soup.select('div.newspaper-icon div.view-content article h3')

# When `enumerate` is used in a loop, it returns one element from the
# list, but also returns a counter that automatically increments each
# time through the loop.  That's why there are two variables listed in
# the `for` loop: the counter, and the actual data.
for num, node in enumerate(nodes, 1):
    print(FORMAT_ARTICLE.format(num, node.text))
