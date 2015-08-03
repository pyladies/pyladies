PyLadies Remote
==========

From within remote/

$ `pip install -r requirements.txt`

From within remote/www

$ `mynt gen -f _site && mynt serve _site`


Deploy
------

To deploy (you will need SSH access, so either @econchick or @estherbester for now), from within `remote/www` run `./_deploy.sh`.  It will first generate the HTML files into `remote/www/_site` then `rsync` the files to our server into the `remote` directory.
