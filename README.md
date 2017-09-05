# Message Mail Bot
Discord Bot which will send every message in a channel to specified email adresses using gmail
 
## Getting started

Ever wanted to have your own Discord server for your local reading group, school club or Tabletop RPG group (nerd!) ?

It sure would be convenient to have a chat room for everyone, an announcement channel for important messages and a channel to put all the awkward pictures of your christmas party!

But what's this - someone doesn't want to join for whatever reason? That's fine! With this Bot, they will still get the important announcements! 
Every message you or an authorized member of the server writes in the announcement channel will get picked up by the bot and sent to every email address you want!

### Prerequisites

Follow these instructions to add your own Bot to your Discord Server

* Go to the [Discord application page](https://discordapp.com/developers/applications/me#top)
* Create a new App (I named my bot AnnounceMailBot but I'm sure you can come up with even better names!)
* Now click on Create a Bot User so the bot can join your server
* Copy this link and substitute clientid with the Client ID of your bot! https://discordapp.com/oauth2/authorize?client_id=clientid&scope=bot
* Choose the server and click on Authorize. Done!

### Configuring the bot

Now you just need to get the main.py file and edit it with your favorite text editor. You need to change the following variables:

* gmail_user - your gmail address from which the bot will send the emails.
* gmail_pwd - your gmail password. If you use 2 factor authentication you will need to use an [app password](https://myaccount.google.com/apppasswords)
* FROM - your name or alias
* SUBJECT - subject of the email, for example "new announcement from your favorite Call of Cthulhu group!"
* botuser on line 81 - the username of your bot. You can find it on the Discord page you were just on.
* token on line 86 - the token of your bot. you can find it on the Discord page you were just on by clicking on reveal.

I recommend using a different gmail account than your own. Or maybe you like to live dangerously and have your password in plain text in some python file.

### Configuring the Discord Server

* Change the New Member Message Channel of your server to the channel your bot will listen in.
* Change the permission of all other channels so that the bot can't read messages there.
* Create a new channel 'botconf' where you can send commands to configure the bot. Set permissions so that only you and the bot can see and write the messages.

### Configuring the email adresses

Emails are saved in a text file called emails.txt wherever main.py is run from. You can add addresses using the commands.

## Starting the bot

We're nearly done! Now you just need to start the bot by running main.py on your favorite little server. I really want a Raspberry Pi right now. 

The bot will now send every text message written by a user other than itself to every single email address in emails.txt

### Commands

There are 3 Commands. Please don't use them in the announcement channel or everyone will be confused.

## !list

Lists all the email addresses currently saved in emails.txt

## !add email

Will add email to emails.txt

```
!add example@domain.com
```

## !del email

Will remove email from emails.txt

```
!del example@domain.com
```


## Built With

* [Discord.py](https://github.com/Rapptz/discord.py) 


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
