# Instructions for Chapter 6 Lab

### Part 0 (setup)

1. Open `PyCharm` and open the `software101` project, if it's not
   already open.

2. Right-click on `software101` and choose _Git \> Repository \>
   Pull..._ and click **OK** to pull down and merge anything that
   might've changed from the original GitHub repository.

### Part 1 (initialize the Flask demo)

1. Open `Terminal` and change to the `software101` directory by
   executing `cd PycharmProjects/software101`.

2. Change to the Chapter 6 directory by executing `cd ch06_serverside`.

3. Change to the tutorial directory by executing `cd tutorial`.

4. Set the environment (these are both case-sensitive and
   space-sensitive):

   `export FLASK_APP=flaskr FLASK_ENV=development`

5. Run `flask init-db` in the tutorial directory.

### Part 2 (run the application)

1. You must be in the `PycharmProjects/software101/ch06_serverside/tutorial` directory.
   If you just finished Part 1, this will already be the case.

2. Set the environment (these are both case-sensitive and
   space-sensitive). If you just finished Part 1, this will already be
   the case:

    `export FLASK_APP=flaskr FLASK_ENV=development`

3. Execute `flask run` to run the tutorial.

### Part 3 (use the browser to interact with the application)

1. If we want to see how the browser exchanges data with the server, we
   need to generate some of it first. That's what the next few steps do.

2. Use a web browser to visit the URL (shown in the output) and interact
   with the server.

   1.  Register as a user on the server (pick any username and password
       you wish).

   2.  Login using the newly registered account.

   3.  Add two posts to the chat channel.

3. Edit `flaskr/templates/auth/login.html`. It's probably easiest to use
   `PyCharm` for this, but you'll need to drill down deep into the
   `tutorial` directory to locate this file.

4. Change the message from `Log In` to `Log In to the Flaskr
   Application`

5. Go back to the browser window and logout of the application, then log
   back in. Did your new message come up?

6. During the lab review, we will use the _DevTools_ of the browser to
   look at the data being passed back and forth between the browser and
   the server.
