---
layout: post.html
title: "How to hook people on CS through Magic"
tags: [computer science, magic, outreach]
---

Computer Science Outreach Magic
===============================

*Thanks to Katie Cunningham of Tucson for letting us copy this post from [her blog](http://katieirenec.blogspot.com/2013/03/computer-science-outreach-magic.html)!*

For several months, I always carried a deck of cards in my backpack. I like playing gin rummy as much as anyone, but that's not the reason why. I carried them because I had discovered ***Computer Science Outreach Magic***.

I learned a Computer Science magic trick from [cs4fn.org/magic](http://cs4fn.org/magic), and I've been hooked ever since. I've performed this trick to much success when manning booths at outreach events and teacher visiting days. It lets you engage people while illustrating a bit of computer science. At the PyLadies' lunch at [PyCon '13](https://us.pycon.org/2013/), Esther Nam convinced me to write a blog post about this card trick I was so excited about. "Lots of people want to know how to demonstrate computer science without a computer!" she said.


![Teaching the card trick to Computer Science student volunteers at the Tucson Festival of Books.](http://4.bp.blogspot.com/-QWERYs18cuw/UUWEUHD2leI/AAAAAAAAAEI/DNVDS_mvWNo/s400/cards1.jpg)

![Performing the big reveal at a University of Arizona College of Science ceremony.](http://2.bp.blogspot.com/-7zkM7b9NU3c/UVeDQxvHd5I/AAAAAAAAALM/6nes0mg8Vxg/s400/cards2_light.jpg)

 That's exactly why I love this trick. It's portable, it's easy, and it doesn't use a computer. It allows people to see an easily digestible example of the logic, discrete math, and information that is at the core of Computer Science. For people who aren't impressed by physical computers or cryptic terminal windows, this can really be a draw.


> "[Computer science] is not really about computers -- and it's not about computers in the same sense that physics is not really about particle accelerators, and biology is not about microscopes and Petri dishes.... Now the reason that we think computer science is about computers is pretty much the same reason that the Egyptians thought geometry was about surveying instruments: when some field is just getting started and you don't really understand it very well, it's very easy to confuse the essence of what you're doing with the tools that you use." - Hal Abelson (1986)

Here's how I do it:
-------------------
+ You need **three people**: The magician, the assistant, and the learner.

+ The magician closes her eyes and **keeps them closed until the end of the trick**.

+ The learner is given the deck and told to **make a four by four matrix of cards with some face up and some face down, randomly distributed**.

![](http://2.bp.blogspot.com/-PaDicUidMdc/UVlR53gTf7I/AAAAAAAAAM4/6151cf6yKZE/s200/2013-03-31+13.36.14.jpg)

+ The assistant takes the deck back and whispers to the learner: **"I'm going to make it harder for her and add another row and column".** The magician might groan at this point and say "Nooo it's so hard already!!!" The new row and column are added.

![](http://4.bp.blogspot.com/-SjXhvfiM7ks/UVlR5KOW9oI/AAAAAAAAAM0/YnuzY62o7g4/s200/2013-03-31+13.37.51.jpg)

+ The assistant tells the learner to flip one card, and that the magician will tell him which card he flipped. **The learner flips one card.**

![](http://1.bp.blogspot.com/-rd8vxAd32pU/UVlR2EGsu5I/AAAAAAAAAMs/Ie0E7w2SL0k/s200/2013-03-31+13.39.49.jpg)

+ The magician opens her eyes, hovers her hands over the cards, and **identifies the flipped card!**

+ The learner is very impressed. While the amazement hasn't worn off, the magician and assistant tell the learner that **this method is used to identify errors in computer data.** Face up and face down cards are just like the way a computer stores information in 1s and 0s. Perhaps the information is being sent from one computer to another and one of the bits -- one of the 1s or 0s -- gets changed to the other (flipped!). Computer Scientists invented this technique so computers could discover where the error took place. If the learner is still interested, explain how the trick worked.


How does the trick work??!!??
-----------------------------

When the assistant adds the extra row and column, he is actually adding **parity bits**. For non-CS people, that means that the assistant adds another card to each row and column so **the sum of face up cards in that row or column is now even**. If there are an even number of face up cards in the row or column, the assistant adds a face down. If there are an odd number of face down cards in the row or column, he adds a face up.

The cards need to be put down seemingly without thought, like the assistant is just adding the extra row and column randomly. Here's a walkthrough:

Add a parity bit to the end of each of the columns

![](http://4.bp.blogspot.com/-43G67TR9qx0/UVnMUg5xkeI/AAAAAAAAANM/wQSrpONYsrU/s320/paritied_with_row_merged.png)


Add a parity bit to all of the rows, including the row you just added. (Notice that the column you are adding has parity automatically.)

![](http://2.bp.blogspot.com/-f-glidmmt-k/UVnMYM6168I/AAAAAAAAANU/KLLIjMNfJis/s320/paritied_with_col_merged.png)

Now when the learner flips a card, the row and column of the card that was flipped have an odd number of face up cards! You can quickly find the flipped card, even though you've never seen the grid before.

![](http://3.bp.blogspot.com/-0PjjohEdhy0/UVnQyXP4lDI/AAAAAAAAANk/bXKXQWyY14U/s320/found_it.png)

It works just as well when the flipped card is in the parity row or column.

![](http://4.bp.blogspot.com/--5Vj10M2eoQ/UVnQz1T9AOI/AAAAAAAAANs/GY4dr0GOClI/s320/found_it_side.png)

The kids at the CSUnplugged show figured it out on their own, I was very impressed. The presenters used this trick as their opening act, and then explained it at the very end, so the kids had some time to think about it. If you want to see their explanation, check out [this video](http://www.youtube.com/watch?feature=player_embedded&v=gBPZOpT4DPU)


Optional Follow-up
------------------

Make sure the learner really understands by **putting the cards back into their parity'd state and asking him to close his eyes and guess which card his friend flipped**. This is demoed in the video above. If you have more time for more than a quick wow moment, you can ask the learner:

* Does it matter if the error is in the parity bits?
* Is it possible to detect two errors, and if so, can they be corrected?
* How about three errors?


Practice!
---------

I'm sure you are excited now to show this trick to all your friends. With this trick in your pocket, every person becomes someone you can impress with computer science! You'll live for the stunned look on people's faces when you pick the right card!

But to make it go smoothly, you'll need to **practice practice practice practice**! The trick might sound simple enough, but every time I or someone else has attempted the trick without recent practice, it has been a major fail.

![Practice with your cat! And people.](http://2.bp.blogspot.com/-dASy6SDRpKk/UVkf-MZPdTI/AAAAAAAAALk/pjaO4G3DPso/s200/2013-03-30+13.36.13.jpg)


Practice with your cat! And people.


Alternate versions
------------------

I like doing this trick with cards because cards are easy to get my hands on when I'm inspired to perform. Usually I have limited table space, so it's hard to squeeze in more cards than I have described. In the CSUnplugged version, they start with a larger grid and black and white squares. (Note that it doesn't matter how big your grid is -- the trick works the same.) They also had the nifty idea to make them magnetic so the trick can be performed on a whiteboard.

![](http://1.bp.blogspot.com/-CfcakI791kE/UU3hycAFaQI/AAAAAAAAAHQ/C8VUDQ5swZU/s640/parity_trick.jpg)

CSUnplugged has the magician add the extra row, eliminating the assistant. I like having the assistant better, because the magician's reveal is more impressive, since clearly no memorization is done -- the magician hasn't seen the cards at all! Also, when a little kid is the learner, the assistant is necessary to make sure he or she puts down the cards correctly and flips only one card. But for a demonstration in front of a classroom or when you're alone, it's worth thinking about.

Find the original cs4fn version of the trick on page 25 here: <http://www.cs4fn.org/magic/downloads/cs4fnmagicbook1.pdf>. They add the extra row based on face down cards instead of face up cards. It doesn't matter really of course -- do what's easier to see quickly. Or if you change the size of the grid to have an even number of rows and columns at the end of the trick, it doesn't matter! Face up and face down will both have to be even or odd.

P.s. Now that you are using this trick, you have to watch out for Magnita Makov, world's greatest magician.



**Good luck! Go forth and impress all your friends!!!**

A big thanks to [Daniel Harms](https://twitter.com/danielharms) for helping me improve this trick :)
