# Instructions for Chapter 3 Lab

### Part 0 (setup)

1. Open `Terminal` and navigate to the `software101` directory by
typing `cd software101` and pressing _Enter_ at the command prompt.
Execute `git pull` to pull any updates to the GitHub repository down to
your virtual machine.

2. Open `PyCharm`, if it's not already open.

3. Expand the listing for the chapter 3 directory.

### Part 1 (demonstration of the browser's developer tools)

1. Load the `Firefox` browser and navigate to the NIST web site
(the same one as the previous lab exercise,
<https://www.nist.gov/topics/cybersecurity>)

2. Open the browser's _DevTools_ by selecting _Tools → Web Developer → Toggle Tools_

3. Click the browser's `Reload` button that appears in the content of the `Network` tab

4. Answer these questions about the results: 

    1. How many HTML documents are there?

    2. How many CSS documents?

    3. Which component of the page took the longest to load?

    4. Were any of the requests loaded in parallel to the others?  How can you tell?

### Part 2 (demonstration of `wireshark`)

1. Open `wireshark` and select `enp0s3`

2. Click the `Capture Options` button to set the capture filter

3. Click the `Capture Filter` and enter `tcp port https` (if a
warning comes up, click OK to ignore it)

5. Click `Start` to begin capturing network packets

6. While the capture is running, switch to `PyCharm` and run the
`webget.py` script (it's a copy of the HTML screen scraper from the
previous chapter)

7. When the script has completed, go back to `wireshark` and stop the capture

8. Analyze the contents of the `wireshark` display and answer these questions:

    1. Can you identify the various network protocols?  TCP, UDP, and so on?

    2. You should see some HTTPS packets.  What do they contain?

9. We'll be discussing the contents of the `wireshark` window in
the next chapter.  For now, you can close the browser and the
`wireshark` window -- you won't be using them again right away
