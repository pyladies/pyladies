# Overview

This is the source code for the future http://sthlm.pyladies.com/ website. It uses:

* [mynt](http://mynt.mirroredwhite.com/) - a static site generator
* [Bootstrap](http://getbootstrap.com/) - Front-end web development framework
* Cute [icon fonts](http://zocial.smcllns.com/), kindly provided by [Fontello](http://fontello.com/)

## Directory Layout

This is a general overview of the top-level directory structure:


```
.
├── _assets        # CSS, JavaScript, images and fonts.
├── _templates     # Layouts and includes.
├── about
└── events
```

**Note**: mynt also handles blog posts, and RSS feeds and archives which this site does not currently use.


## To run locally

1. Clone to your machine
2. Open a terminal and go to the project directory
3. `pip install -r requirements.txt`
4. `mynt gen -f _site && mynt serve _site`
5. Open [http://localhost:8080/](http://localhost:8080/) in your browser to view the site


## To do:

* Add content
* Create Sponsors page
* Meetup and Twitter integration
* Contact form
