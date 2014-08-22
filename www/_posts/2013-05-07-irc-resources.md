---
layout: post.html
title: "Introduction to IRC"
tags: ["how-to", "irc"]
category: [resources, pyladies]

---


[IRC](http://en.wikipedia.org/wiki/Internet_Relay_Chat) is a great way to get in touch with open source developers around the world. The FreeNode network in particular is host to channels (chat rooms) for almost any open source framework you are likely to encounter as a Python developer.

Here's a guide to setting up an IRC name and joining the #pyladies channel, a friendly place to become familiar with how IRC works.

## Create your account

* Go to http://webchat.freenode.net
* For "Nickname", pick an available username (legal characters are anything <code>A-Z</code>, <code>0-9</code>, <code>-</code> and <code>_</code>)
* Don't fill out anything else except the captcha, and hit "Connect"

![Webchat window](https://dl.dropboxusercontent.com/u/39730/freenode0.PNG)



## Register your Nickname

* Pick a VERY INSECURE password (all communication with IRC is viewable by anyone on the internet so don't use a sensitive password!!!) and use it to register, via email.
* At the bottom of the messaging window, type the following (all IRC commands begin with the forward slash):

`/msg nickserv register YOUR_INSECURE_PASSWORD your_email@address.com`

* Check your email and verify that you are now registered by following their instructions (it'll tell you to type something like the following in the message window:

`/msg NickServ VERIFY REGISTER YOUR_NICKNAME THEIR_VERIFICATION_CODE`

![registering your name](https://dl.dropboxusercontent.com/u/39730/freenode1.PNG)

## Install XChat

* Download from http://xchat.org
* Install and open. You will get the following window. Fill in Nickname with the nickname you just registered. Fill in the * other fields if you'd like.
* In "Networks", find and select "FreeNode"

![Networks](https://dl.dropboxusercontent.com/u/39730/freenode2.PNG)

#### (Optional) Configure XChat so that you can Identify yourself to IRC and automatically join #pyladies whenever you open XChat.
Otherwise, you have to do run these commands yourself every time:

`/msg nickserv identify YOUR_NICKNAME YOUR_INSECURE_PASSWORD`
`/join #pyladies`


![Auto](https://dl.dropboxusercontent.com/u/39730/freenode3.PNG)

## IRC Etiquette

* IRC is an instant-messaging medium but people are not necessarily expected to respond immediately, even if they appear to be available in a chatroom .
* To call someone out in particular, you can write (into the channel) `ping PERSON'S_NICK`
* When they are available, they will respond to you with "pong"
* You are free to speak directly to specific people in the general channel (with the understanding that literally everyone will be listening in on your convo, but you can also privately message them (in XChat, right-click their nick and select "Open Dialogue Window"
* Please be aware that IRC communication is transmitted in plaintext - i.e., it is very insecure (which is why you should register with a very casual password and NEVER share critical information over IRC)

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
