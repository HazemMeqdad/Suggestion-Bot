# Suggestion-Bot
# Discord.py bot with command Suggestion


### Pre-Setup

If you don't already have a discord bot, click [here](https://discordapp.com/developers/), accept any prompts then click "New Application" at the top right of the screen.  Enter the name of your bot then click accept.  Click on Bot from the panel from the left, then click "Add Bot."  When the prompt appears, click "Yes, do it!" 

![Left panel](https://i.imgur.com/hECJYWK.png)

Then, click copy under token to get your bot's token. Your bot's icon can also be changed by uploading an image.

![Bot token area](https://i.imgur.com/da0ktMC.png)

### Setup

Create a file named `.env`

Add `token=<your bot token>`

Your .env file should look something like this:

```
token=<Bot token>
```

After adding your bot token to your .env file, navigate to line 10 in `main.py`. Change  `487258918465306634` to your user id. To get your id, ensure developer mode is enabled (Settings->Appearance->Advanced->Developer Mode) then right-click on yourself and click copy id.

When you hit start everything should startup fine.

### Uptime

So now, all you have to do to keep your bot up is setup something to ping the site your bot made every 5 minutes or so.

Go to [uptimerobot.com](https://uptimerobot.com/) and create an accout if you dont have one.  After verifying your account, click "Add New Monitor".

+ For Monitor Type select "HTTP(s)"
+ In Friendly Name put the name of your bot
+ For your url, put the url of the website made for your repl.
+ Select any alert contacts you want, then click "Create Monitor" 
![Uptime robot example](https://i.imgur.com/Qd9LXEy.png)

Your bot should now be good to go, with near 100% uptime.


[![Run on Repl.it](http://i8.ae/a3UWz)](https://repl.it/github/hazemmeqdad/Suggestion-Bot)

[![Contact with me](http://i8.ae/KmScX)](https://discordapp.com/channels/@me/740700552593145876)

All rights reserved © HazemMeqdad 2020
