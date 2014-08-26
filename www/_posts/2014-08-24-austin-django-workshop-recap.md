---
layout: post.html
title: "PyLadiesATX event: What's a Web Framework? Python, Django, and more"
tags: [events, django, austin]
author: Sara Safavi
author_link: mailto:sara@sarasafavi.com
---

From August 9-11, I led a 2-part, all-women workshop series on web frameworks & learning Django for PyLadiesATX. 

For this class, I decided to teach Django 1.7, and, after verifying my demo project on 2.7 & 3.3, let the students use any Python version they preferred. This ended up working really well: teaching migrations without bothering with South is great, and dealing with 18 very different laptop platforms is a tiny bit easier when pre-existing Python versions aren't a problem!

![Photo](/assets/images/blog/austin_django_2014.jpeg)

The first class in the series was a two-hour session, which began by covering the basics of how the web works (we started with the question, "what happens when you hit 'enter' after typing a URL into the browser?") and where a framework like Django fit into the big picture. We then spent the second half of that first session working to get everyone's development environments set up, and Django 1.7 installed in a virtualenv. This turned out to be a huge improvement over single-day workshops, as it meant everyone was able to show up to the 2nd class ready to start working immediately. After seeing this work so well for us, I strongly recommend anyone planning a similar workshop consider splitting a setup session out from the main class time.

For the second class, we met in a classroom at a local library and spent all day learning to build a Django application: our simple CRUD app let users submit & view recipes to a "Recipe Minder" site. I tried something new for this class, experimenting with a code-by-diff sort of process: after discussing each new topic and giving the student's a new assignment to work on, I put short URLs on the slides they could type easily, which pointed to relevant commits on GitHub. I used this more heavily as we progressed - at first the students had to type a complete code update before I gave them a short URL to check against, but as the project got more detailed they would see the URL to the next commit at the same time they were working. Of course, after linking to the first GitHub commit, some students were able to "skip ahead" and work on their own - but for the most part the group kept pace together and ended up completing their projects right around the same time. You can find the code for the [finished demo on GitHub](https://github.com/sarasafavi/introdjango), and the slides for both classes here: [Part 1](http://links.sarasafavi.com/predjango), [Part 2] (http://links.sarasafavi.com/introdjango).

All in all, we had 18 ladies come together to attend both classes. An "Intro to Django" class has been top of PyLadiesATX's "most requested" list for a while, so I was really glad to finally get this off the ground. Based on the feedback received, I'm already pretty sure I'll be doing this again next quarter. Meanwhile, if you are interested in running this class for your own local PyLadies chapter, feel free to use the code & slides linked above (all are released under an MIT license, if you're interested in that sort of thing). Also if you have any questions or comments, please do get in touch! I'd love to hear your thoughts on improving future instances of the class.

_Sara is an organizer for PyLadies Austin. Contact her at sara@sarasafavi.com_
