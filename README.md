# Overview

This is the source code for the http://pyladies.com/ website. It uses
`mynt`, a static site generator.

## Directory Layout

This is a general overview of the top-level directory structure. The
things that aren't labeled contain content for the website.


```
.
├── CodeOfConduct
├── _assets        # javascript and CSS stuff goes here
├── _posts         # these are the blog posts written in markdown
├── _templates     # these are the base templates that other things use.
├── about
├── archives
├── blog
├── locations
├── resources
└── sponsor
```

## To run locally

**Note**: before continuing, make sure you have headers for Python and libevent
installed (e.g., on Ubuntu, **python-dev** and **libevent-dev**). Packages in
requirements.txt require these to compile successfully.

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

See [CONTRIBUTING.md](https://github.com/pyladies/pyladies/blob/master/CONTRIBUTING.md) for instructions and guidelines.

## For Organizers
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
