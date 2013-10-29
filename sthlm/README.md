PyLadies Sthlm
==========
# Overview

This is the source code for the future http://sthlm.pyladies.com/ website. It uses:

* [mynt](http://mynt.mirroredwhite.com/) - a static site generator
* [Grunt](http://gruntjs.com) - task runner (for development)
* [Bower](http://bower.io/) - package manager  (for development)
* [Sass](http://sass-lang.com) with [Compass](http://compass-style.org/) - CSS pre-processor and authoring framework  (for development)
* [Bootstrap](http://getbootstrap.com/) - Front-end web development framework
* Cute [icon fonts](http://zocial.smcllns.com/), kindly provided by [Fontello](http://fontello.com/)

## Directory Layout

This is a general overview of the top-level directory structure:


```
.
├── test           # Mocha test files
└── src            # mynt directory
    ├── _assets        # CSS, JavaScript, images and fonts.
    ├── _templates     # Layouts and includes.
    ├── about
    └── events
```

**Note**: mynt also handles blog posts, and RSS feeds and archives which this site does not currently use.


## To run locally
Depending on if you want to work on the layout/code or add content, there are
two divering paths

### Both paths
1. Clone to your machine
2. Open a terminal and go to the project directory (sthlm)
3. Create (`mkvirtualenv PyLadies`) or use (`workon PyLadies`) PyLadies virtual environment
4. `pip install -r requirements.txt`

### Adding content
1. `mynt gen -f src _site && mynt serve _site --port=9000`
2. Open [http://localhost:9000/](http://localhost:9000/) in your browser to view the site
3. Once done, copy the built site (`_site`) to the site repository, commit changes and push


### Working on site
`npm install && bower install && bundle install && pip install -r requirements.txt` to draw in all dependencies

#### Basic commands
* `grunt server` to run a local development server, opens [http://localhost:9000](http://localhost:9000) and reloads at changes
* `grunt deploy` pushes the changes in the site to the live site repository, with a commit message stating its' auto-generated

## To do:

* Add content
* Create Sponsors page
* Meetup and Twitter integration (widgets)
* Contact form
* Resources (links to projects and such)
* Turn navtabs into other kind of menu at a smaller size
