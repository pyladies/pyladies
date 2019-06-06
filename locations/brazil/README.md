Overview
--------

This is the source code for the http://brasil.pyladies.com/. It uses [jekyll][j], a simple, blog-aware, static site generator.

[j]: http://jekyllrb.com/

## Directory Layout

This is a general overview of the top-level directory structure. The
things that aren't labeled contain content for the website.


```
.
├── _includes
├── _layouts       # these are the base templates that other things use.
├── _posts         # these are the blog posts written in markdown
├── css            # these are the css files
├── site           # these are the static files
├── .gitignore
├── Gemfile
├── Gemfile.lock
├── README.md
|── _config.yml
├── about.md
├── feed.xml
├── index.html
└── leve_nos.md
```

## To run locally

1. $ gem install jekyll 
2. Clone http://github.com/pyladies/pyladies to your machine. 
3. Change into the directory brazil (cd brazil)
4. $ jekyll serve
# => Now browse to http://localhost:4000

You can use tinypress.co to edit and to create posts.
