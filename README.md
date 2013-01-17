# Overview

This is the source code for the http://pyladies.org/ website.

## To run locally

1. Fork http://github.com/pyladies/pyladies to your own github account.
2. Clone to your machine
3. Create a virtualenv called PyLadies
4. (PyLadies) $ `pip install -r requirements.txt`
5. (PyLadies) $ `mynt gen -f _site && mynt serve _site`

* How to fork and clone: https://help.github.com/articles/fork-a-repo
* How to create a virtualenv: http://simononsoftware.com/virtualenv-tutorial/

**Note**: It is important that when you create your virtualenv, do not
create it in the same folder as the code you downloaded. The reason is
that mynt will search the current directory for files to build and it
looks for all folders that don't start with an underscore (which means
it will find your virtualenv folder and error out).

## To write a blog post

1. Write it in Markdown (Suggestion: Mou.app for mac is create for
Markdown - gives you a preview while you write)

2. The very top of the blog post needs the following (including the
three dashes before & after the layout/title/tags):

```
---
layout: post.html
title: "Your title here"
tags: [list, of relevant, tags]
---
```

3. Save in _posts

4. (PyLadies) $ `mynt _gen -f _site && mynt serve _site`

## Hosting

It's currently hosted on Heroku for free with some .htaccess tricks to
redirect pyladies.com -> www.pyladies.com (since heroku doesn't
support naked domains).

### Your own domain/site:

You are welcome to create your own location's webspace,
e.g. seattle.pyladies.com or sea.pyladies.com, or even
www.pyladies.com/seattle etc. If you want your own URL, tell me:

1. what you want your URL to be.
2. make a pull request for your site.
3. when you want it to go live.

If you just tell me your URL I can put dummy data - e.g. your location
info etc, if you want to take your time to work on your own site.

Suggestions:
* Play with the Meetup API to show your upcoming events, number of members, etc
* Play with the Twitter API to show your group's latest tweets
* A chapter blog
* anything!

I _really_ don't mind if you want to do a whole different design that
doesn't match w/ the current homepage. Maybe keep it as mynt though
- but your choice completely.


-your friendly administrator.
