---
layout: post.html
title: "Introduction to IRC"
tags: ["how-to", "irc"]
category: [resources, pyladies]

---

Updated March 7, 2019

[IRC](http://en.wikipedia.org/wiki/Internet_Relay_Chat) is a great way to get
in touch with open source developers around the world. The FreeNode network
hosts chat rooms, formally called channels, for almost any open source project
or framework which you are likely to encounter as a Python developer.

PyLadies has it very own IRC channel #pyladies on the FreeNode network. Here's
a guide for getting started with IRC and joining the discussion on the #pyladies
channel. Let's start by using a web based IRC chat client, setting up an IRC
nickname, and joining the friendly #pyladies channel.

## Connect to IRC using a web client

Let's start by using a web based IRC client:

- Go to https://webchat.freenode.net/?channels=pyladies
- For an IRC "Nickname", pick an available username (legal characters are
  anything <code>A-Z</code>, <code>0-9</code>, <code>-</code> and <code>_</code>)
- Fill out the captcha code
- Do not fill in any other fields (other than nickname and captcha) and hit
  the "Connect" button

## Register your Nickname

Once you decide that you will use IRC on a regular basis, you may wish to
register an IRC nickname that you may use each time you connect to IRC. Here
are the basic steps to registering a nickname:

- Pick a VERY INSECURE password (all communication with IRC is viewable by
  anyone on the internet so don't use a sensitive password!!!) and use it to
  register, via email.
- At the bottom of the messaging window, type the following (all IRC commands
  begin with the forward slash):

  `/msg nickserv register YOUR_INSECURE_PASSWORD your_email@address.com`

- Check your email and verify that you are now registered by following the
  email's instructions (it'll tell you to type something like the following
  in the message window):

  `/msg NickServ VERIFY REGISTER YOUR_NICKNAME THEIR_VERIFICATION_CODE`

## Installing an IRC client

While a web client is a handy way to get started with IRC, you may wish to use
an installed IRC client which is especially useful to follow multiple channels.
There are many different IRC clients available for Windows, Mac OSX, Linux, as
well as Android and iOS.

Some popular clients are:

- XChat (Linux, Mac OSX, Windows)
- LimeChat (Mac OSX)
- mIRC (Windows)

### Installing XChat

- Download from http://xchat.org
- Install and open. You will get the following window. Fill in Nickname with
  the nickname you just registered. Fill in the * other fields if you'd like.
- In "Networks", find and select "FreeNode"

#### (Optional) XChat Configuration

Configure XChat so that you can `Identify` yourself to IRC and automatically
join `#pyladies` whenever you open XChat.

Otherwise, you will have to do run these commands yourself to connect manually
every time:

```
/msg nickserv identify YOUR_NICKNAME YOUR_INSECURE_PASSWORD
/join #pyladies
```

## IRC Etiquette

- Although IRC is an instant-messaging medium, people are not necessarily
  expected to respond immediately, even if they appear to be available in a
  chatroom.
- To call someone out in particular, you can write (into the channel input line)
  `ping PERSON'S_NICK`. When they are available, they will respond to you with
  the word "pong"
- You are free to speak directly to specific people in the general channel
  (with the understanding that literally everyone will be listening in on your
  convo.
- You may also privately message a person. It's good etiquette to first ask in
  the general channel if you may send them a private message. (Note: In XChat,
  right-click their nick and select "Open Dialogue Window")
- Please be aware that IRC communication is transmitted in plaintext - i.e., it
  is very insecure (which is why you should register with a very casual
  password which you are not using for other accounts and NEVER share critical
  or privacy information over IRC)

## Well-known Python Channels on FreeNode

* #pyladies
* #python
* #pycon
* #django
* #pyramid
* #pocoo
* #positivepython
* #openhatch

## Helpful commands

Other useful commands to get you started:

* `/help` -- get help from the IRC bot
* `/join #CHANNEL` -- join a channel
* `/me ACTION` -- describe yourself performing an action
* `/msg OTHER'S_NICKNAME MESSAGE `-- send someone a private message
* `/part` -- leave a channel
* `/quit` -- leave IRC
