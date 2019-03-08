# Overview

[![CircleCI](https://circleci.com/gh/pyladies/pyladies/tree/master.svg?style=svg)](https://circleci.com/gh/pyladies/pyladies/tree/master)

This is the source code for the http://pyladies.com/ website. It uses
`mynt`, a static site generator.

## Directory Layout

This is a general overview of the top-level directory structure, which lives
in the `www` folder. The things that aren't labeled contain content for the 
website.


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
3. Create a virtualenv called PyLadies and launch it (see Note below).
4. (PyLadies) $ `pip install -r requirements.txt`
5. (PyLadies) $ `cd www` (navigate to the `pyladies/www` directory of the cloned repository on your machine.)
6. (PyLadies) $ `mynt gen -f _site && mynt serve _site`
7. Copy the IP address provided once mynt has completed building the site. (It will say something like `>> Serving at 127.0.0.1....`), then paste the IP address into the URL bar of a browser window and load it to view the site.
8. To view any changes you make to the site code, type ctrl+c in the terminal to stop the local server, then run the command from Step 6 again and refresh the browser window.

* How to fork and clone: https://help.github.com/articles/fork-a-repo
* How to create a virtualenv: http://simononsoftware.com/virtualenv-tutorial/

**Note**: It is important that when you create your virtualenv, do not
create it in the same folder as the code you downloaded. The reason is
that mynt will search the current directory for files to build and it
looks for all folders that don't start with an underscore (which means
it will find your virtualenv folder and error out).


## To write a blog post

See [CONTRIBUTING.md](https://github.com/pyladies/pyladies/blob/master/CONTRIBUTING.md) for instructions and guidelines.

## To contribute to the repository

See [CONTRIBUTING.md](https://github.com/pyladies/pyladies/blob/master/CONTRIBUTING.md) for instructions and guidelines.

## To write a resource (more "sticky" than a blog post)

### Collection of outside resources

If you want to add a bullet item to an existing subject matter, find the relevant post in `www/_posts` (file titled by it's general category) and add to the `.md` file.  Please also update the date in the `.md` file.  For instance, if you want to add another suggestion to text editors, the original file is: `www/_posts/2013-04-19-tools-resources.md`, and once you're done editing, it would be renamed to `www/_post/todays-date-tools-resources.md`.

If there is a collection of resources that do not fit into our loosely-named categories, like "tools" or "tutorials", etc, then start your own in `www/_posts/` and name the Markdown file with today's date, general category, plus the word "resources", like: `2013-04-21-developer-tips-resources.md`.  You will also need to have the following at the top:

```
---
layout: post.html
title: "Your title here"
tags: [list, of relevant, tags]
category: resources
---
```

### Your own resource
If you want to write your own resources, like [Barbara's beginner workshop notes](http://www.pyladies.com/blog/intro-python-april-6-recap/) or [Juliana's Mac setup](http://www.pyladies.com/blog/Get-Your-Mac-Ready-for-Python-Programming/), in addition to [CONTRIBUTING.md](https://github.com/pyladies/pyladies/blob/master/CONTRIBUTING.md), you will need to add more items in the header portion, like so:

```
---
layout: post.html
title: "Your title here"
tags: [list, of relevant, tags]
author: Name, or blank/none
author_link: Twitter/Blog/etc or blank/none
category: resources, pyladies
---
```

Notice that `pyladies` and `resources` are required in for `category`.

Once done, save it in `www/_posts/` with the date and title in the name of the file, like so: `2013-04-21-lynns-awesome-resource.md`.

To find this resource online, you would navigate to http://pyladies.com/blog/[your_post_name]

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
