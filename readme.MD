Collagebot
==========

Collagebot is a Slack bot that automatically combines two images into a single
one. It was designed for news organizations where reporters and editors
frequently work with graphics, but don’t have access to graphical editing tools
like Photoshop or GIMP.

Disclaimer
----------

Collagebot is a work in progress created by a non-professional programmer for
his specific workplace. It is very buggy and in active development and may not
be right for you. But if it is helpful, super!

How to set up
-------------

1.  Create a new bot user (default “collagebot”) and a channel for that bot user
    to live in (default \#x-bot-collage”).

2.  Clone the git repo and create a new Heroku app for it. Install the
    redis-to-go extension for the app.

3.  Use the URL of your new Heroku app (plus "/request” on the end) to create an
    outgoing web hook trigger in your new Slack room (default “collage”)

4.  Insert the API key on line 8 in utils.py and the outgoing request token in
    line 13 of server.py.

5.  Push your code to Heroku and you should be in business.

How to use the bot
------------------

There are currently two different types of requests the bot can process. One is
to force the collage to an aspect ratio of 48 x 27 (maxing out at 2400 x 1350),
resizing by height and cropping by width to fit. The other just makes a collage
at the width and height of the smallest of the two photos, no resizing or
cropping.

Tip:The force option is much more useful.

To do a force request, go to the channel with the bot and type

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
collage url url -f
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

where the URLs are publicly-available URLs where your images can be accessed.
The bot will upload the resulting collage to the channel. To do a non-forced
version, simply leave off the “-f”

### Future improvements

I have a lot of plans for the bot, such as making multi-picture collages and
making the non-forced option more useful (or just getting rid of it). I’m going
to add all these planned improvements to the issues list, so check that for more
info.

### Contact

My e-mail is [patrick.hogan\@fusion.net ](mailto:patrick.hogan@fusion.net)and my
twitter is \@[phogan](http://www.twitter.com/phogan). I’ll answer questions to
the best of my ability, but remember I am a reporter first and a programmer
second.
