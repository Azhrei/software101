# Instructions for Chapter 5 Lab

### Part 0 (setup)

1. Open `File Manager`, navigate to the `software101` directory.
Now, double-click on the `get_updates.sh` script.

### Part 1 (initialize the Flask demo)

1. Open `Terminal` and change to the `software101` directory by executing `cd software101`

2. Change to the Chapter 5 directory by executing `cd ch05_serverside`

3. Change to the tutorial directory by executing `cd tutorial`

4. Run `flask init-db` in the tutorial directory

### Part 2 (setup the environment variables and run the application)

1. You must be in the `software101/ch05_serverside/tutorial` directory.
If you just finished Part 1, this will already be the case.

2. Set the environment (both case-sensitive and space-sensitive):

    `export FLASK_APP=flaskr FLASK_ENV=development`

3. Execute `flask run` to run the tutorial

4. Use a web browser to visit the URL (shown in the output) and interact with the server

    1. Register as a user on the server

    2. Login using the newly registered account

    3. Add two posts to the chat channel

5. Edit `flaskr/templates/auth/login.html`.  It's probably easiest to use `PyCharm` for this.

6. Change the message from `Log In` to `Log In to the Flaskr Application`

7. Go back to the browser window and logout of the application, then log
back in.  Did your new message come up?  Should it have?

8. During the lab review, we will execute `wireshark` while executing this application and
discuss the output it shows
