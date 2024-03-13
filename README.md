# PyLadies

This website is managed by the [PyLadies Tech and Infra team](PROJECT_TECH_INFRA.md). If you would like to join as an official member, read more here! You can also join us in Slack, `#project-tech-infra` channel.

This website welcomes pull requests from anyone in the community.

## Overview

[![Netlify Status](https://api.netlify.com/api/v1/badges/5b4a3b67-b753-45c2-aa90-2db0c38e8de4/deploy-status)](https://app.netlify.com/sites/pyladies/deploys)

This is the source code for the http://pyladies.com/ website. It uses
`mynt`, a static site generator, and is powered by 🐍 Python 3.10 🐍!

**Contents**
- [Understanding the repo's directory layout](#understanding-the-repos-directory-layout)
- [Setting up a development system](#setting-up-a-development-system)
- [To add a new PyLadies location](#to-add-a-new-pyLadies-location-to-the-pyladies-website)
- [To write a blog post](#to-write-a-blog-post)
- [To contribute source code to the repository](#to-contribute-to-the-repository)
- [To write a resource](#to-write-a-resource-more-sticky-than-a-blog-post)
- [For Organizers](#for-organizers)
- [License](#license)

### Understanding the repo's directory layout

Before adding a new location or contributing to the pyladies website, it's
helpful to understand a bit about the repo and its contents.

This is a general overview of the repo's root directory structure.
`requirements.txt` specifies the dependencies. `.github/workflows` contains
the configuration for CI testing and deployment. The repo's root directory also contains
the `www` folder. Most of the time, contributors will edit or add files in
the `www` folder.

```bash
requirements.txt   # file with dependencies used by pip
netlify.toml       # file setting up netlify build commands
www                # directory which contains the content of the website
├── CodeOfConduct
├── _assets        # javascript, CSS stuff, and images go here
├── _posts         # contains blog posts written in markdown
├── _templates     # contains the base templates (html and Jinja2) used by the site
├── about
├── archives
├── blog
├── locations      # Use the config.yml file to add new locations or update location info
├── resources
└── sponsor
```

### Setting Up a Development System

If you wish to add a location, new chapter, or make code changes, please
review the next few sections. There are a few tasks to set up a development
system:
- [Set up Python and a project directory](#set-up-python-and-a-project-directory)
- [Create and activate a virtual environment](#create-and-activate-a-virtual-environment)
- [Fork and clone your pyladies repo](#fork-and-clone-your-pyladies-repo)
- [Run the site locally](#run-the-site-locally)

#### Set up Python and a project directory

**Linux, macOS**

1. Check that Python 3.10 is installed with `python --version`. If it is not
   installed, it can be downloaded at [https://python.org](https://www.python.org/downloads/release/python-3610/):
   ```bash
   $ python --version
   Python 3.10
   ```

2. (Optional) Learn the directory which this Python version is installed `which python`:
   ```bash
   $ which python
   /usr/local/bin/python
   ```
   You may see a different directory name which is fine.

3. Create a directory for development `mkdir pyladies-dev`:
   ```bash
   $ mkdir pyladies-dev
   ```

4. Change into the directory `cd pyladies-dev`:
   ```bash
   $ cd pyladies-dev

   # To check your current directory (`<YOUR_PATH>` will be different on
   # your system.)
   $ pwd
   YOUR_PATH/pyladies-dev
   ```

Great!

**Windows**

The process will be similar though the commands will vary slightly. Reference: [Table of basic Powershell commands](https://devblogs.microsoft.com/scripting/table-of-basic-powershell-commands/).

### Create and activate a virtual environment

1. From the `pyladies-dev` directory, install the `virtualenv` package:

   ```bash
   $ pip install virtualenv
   ```

2. Create a virtual environment named `pyladyenv`:

   ```bash
   $ virtualenv pyladyenv
   ```

3. Activate the virtual environment:

   ```bash
   $ source pyladyenv/bin/activate

   (pyladyenv)
   $
   ```

   After activation, you should see `(pyladyenv)` above your command prompt.

**Troubleshooting note (`AttributeError: 'module' object has no attribute 'X509_up_ref'`):** The error comes from PyOpenSSL. Either your OpenSSL is too old or too new. Try upgrading or downgrading OpenSSL and PyOpenSSL.

### Fork and clone your pyladies repo

1. On GitHub, fork http://github.com/pyladies/pyladies to your own GitHub account
   `<YOUR_GITHUB_USER_NAME>` by pressing the green Fork button on the upper right of
   the screen.
2. From the `pyladies-dev` directory, clone your fork to your machine using
  `git clone`:

  ```bash
  (pyladyenv)
  $ git clone https://github.com/<YOUR_GITHUB_USER_NAME>/pyladies.git
  Cloning into 'pyladies'...
  remote: Enumerating objects: 47, done.
  remote: Counting objects: 100% (47/47), done.
  remote: Compressing objects: 100% (29/29), done.
  remote: Total 5877 (delta 22), reused 38 (delta 16), pack-reused 5830
  Receiving objects: 100% (5877/5877), 39.73 MiB | 3.62 MiB/s, done.
  Resolving deltas: 100% (2922/2922), done.
  ```

  You have successfully cloned your pyladies fork. :smile:

## Run the site locally

**Troubleshooting note** for some operating systems: Make sure you have headers for Python and libevent
installed (e.g., on Ubuntu, **python-dev** and **libevent-dev**). Packages in
`requirements.txt` are required for the website to build successfully with mynt.

1. Change to the root of the pyladies repo (your virual environment should
   still be activated):
   ```bash
   (pyladyenv)
   $ cd pyladies
   ```
2. Install dependencies using `pip`:
   ```bash
   (pyladyenv)
   $ pip install -r requirements.txt

   # You will see files being installed and this message at completion
   # It's okay if the versions differ slightly
   Successfully built hoep MarkupSafe mynt pathtools pycparser PyYAML watchdog
   Installing collected packages: argh, asn1crypto, six, pycparser, cffi, bcrypt, idna, enum34, ipaddress, cryptography, docutils, pyasn1, PyNaCl, paramiko, Fabric, hoep, MarkupSafe, Jinja2, Pygments, PyYAML, pathtools, watchdog, mynt
   Successfully installed Fabric-1.13.1 Jinja2-2.9.6 MarkupSafe-1.0 PyNaCl-1.1.2 PyYAML-3.12 Pygments-2.2.0 argh-0.26.2 asn1crypto-0.22.0 bcrypt-3.1.3 cffi-1.10.0 cryptography-2.0.3 docutils-0.14 enum34-1.1.6 hoep-1.0.2 idna-2.6 ipaddress-1.0.18 mynt-0.3.1 paramiko-2.2.1 pathtools-0.1.2 pyasn1-0.3.2 pycparser-2.18 six-1.10.0 watchdog-0.8.3
   ```

3. Navigate into the `pyladies/www` directory.
   ```bash
   (pyladyenv)
   $ cd www
   ```

4. Use mynt to generate and serve the website locally with
   `mynt gen -f _site && mynt serve _site`:
   ```bash
   (pyladyenv)
   $ mynt gen -f _site && mynt serve _site
   >> Parsing
   >> Rendering
   >> Generating
   Completed in 1.114s
   >> Serving at 127.0.0.1:8080
   Press ctrl+c to stop.
   ```
5. Copy the IP address provided once mynt has completed building the site.
   It will say something like `>> Serving at 127.0.0.1:8080`. Then paste the IP address into the URL bar of a browser window and load it to view the site.

**Congrats on running the site on your machine** :tada: :snake:

6. (Optional: After making changes to the source code) To view any changes
   you make to the site code, type ctrl+c in the terminal to stop the local
   webserver. Then run the command from Step 5 again and refresh the browser
   window.

* How to fork and clone: https://help.github.com/articles/fork-a-repo
* How to create a virtualenv: http://simononsoftware.com/virtualenv-tutorial/

**Note**: It is important that when you create your virtualenv, do not
create it in the same folder as the code you downloaded. The reason is
that mynt will search the current directory for files to build and it
looks for all folders that don't start with an underscore (which means
it will find your virtualenv folder and error out).

## To add a new PyLadies location to the PyLadies Website

Follow the instructions for [setting up a development environment]().

To add or edit a location, you will make changes to the `config.yaml`
file found in the `pyladies\www\locations` directory.

YAML files are often used for configuration information. They can be
fussy about spacing, indentations, and punctuation. It can be helpful
when troubleshooting to use an online YAML validator to see if the file
is correctly formatted. An example is [YAML Lint](http://www.yamllint.com/)
though there are many others and some editors provide similar functionality.

An example of a location:
```yaml
- email: berlin@pyladies.com
  external_website: true
  image: pyladies_berlin.png
  location:
    latitude: 52.52
    longitude: 13.38
  meetup: PyLadies-Berlin
  meetup_id: 4663512976
  meetup_image: https://secure.meetupstatic.com/photos/event/6/b/8/6/highres_454587526.jpeg
  name: Berlin, Germany
  organizer: Anett G.
  pro_network: Python Software Foundation Meetup Pro Network
  twitter: PyLadiesBer
  website: http://berlin.pyladies.com
```

Please note: if you wish to use the `website` field, you need to create an official website through the [PyLadies Chapter Website repository](https://github.com/pyladies/chapter-websites/issues). Otherwise you can skip that field.

**For Unicode accents in some languages**
To use a Unicode accent in a YAML file, it's important to use the
HTML entity character for the accent. The
[HTML entity](https://developer.mozilla.org/en-US/docs/Glossary/Entity)
can found be found in
[a table of characters](https://dev.w3.org/html5/html-author/charref).

For example, México will have the HTML entity `M&eacute;xico`.

## To write a blog post

See [CONTRIBUTING.md](https://github.com/pyladies/pyladies/blob/master/CONTRIBUTING.md) for instructions and guidelines.

## To contribute to the repository

See [CONTRIBUTING.md](https://github.com/pyladies/pyladies/blob/master/CONTRIBUTING.md) for instructions and guidelines.

## To write a resource (more "sticky" than a blog post)

### Collection of outside resources

If you want to add a bullet item to an existing subject matter, find the relevant post in `www/_posts` (file titled by its general category) and add to the `.md` file.  Please also update the date in the `.md` file.  For instance, if you want to add another suggestion to text editors, the original file is: `www/_posts/2013-04-19-tools-resources.md`, and once you're done editing, it would be renamed to `www/_post/todays-date-tools-resources.md`.

If there is a collection of resources that do not fit into our loosely-named categories, like "tools" or "tutorials", etc, then start your own in `www/_posts/` and name the Markdown file with today's date, general category, plus the word "resources", like: `2013-04-21-developer-tips-resources.md`.  You will also need to have the following at the top:

```yaml
---
layout: post.html
title: "Your title here"
tags: [list, of relevant, tags]
category: resources
---
```

### Your own resource
If you want to write your own resources, like [Barbara's beginner workshop notes](http://www.pyladies.com/blog/intro-python-april-6-recap/) or [Juliana's Mac setup](http://www.pyladies.com/blog/Get-Your-Mac-Ready-for-Python-Programming/), in addition to [CONTRIBUTING.md](https://github.com/pyladies/pyladies/blob/master/CONTRIBUTING.md), you will need to add more items in the header portion, like so:

```yaml
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

# For Organizers

## Registering your PyLadies Chapter and onbtaining a website

Once you have obtained an official PyLadies Google account you should:

1. Register your [PyLadies Chapter to the Chapter Directory](https://docs.google.com/forms/d/e/1FAIpQLSf43R4FbiIE4z76k5z42UU4HKMKJnTr2ldh4KecE4WRTJZLUw/viewform) as active, we use this to populate the chapter options for [members when registering](https://members.pyladies.com) as well as populate the PyLadies chapter map.
2. Get started on building your PyLadies website, read the directions on the [PyLadies Chapter Website repo](https://github.com/pyladies/chapter-websites#pyladies-chapter-websites).

Questions? *Make sure to join us in Slack at slackin.pyladies.com and ask to join the #organizers channel!*

## LICENSE

[License: MIT License](https://github.com/pyladies/pyladies/blob/master/LICENSE)
