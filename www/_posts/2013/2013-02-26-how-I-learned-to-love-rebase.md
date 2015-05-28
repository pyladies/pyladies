---
layout: post.html
title: "How I Learned to Stop Worrying and Love Rebase"
tags: [rebase, git, version control]
---

Rebase is a downright scary concept. When the best way to explain how it works I've heard starts with thinking that you're time-traveling back to before certain changes were ever introduced to a project, you probably should be afraid. We've all read enough science fiction to know what happens if you go back to the Age of the Dinosaurs and step on an ugly-looking bug.

But while rebase is a responsibility to take seriously - especially if you're working on a team and you could wipe out every commit people have added since last Sunday - perhaps we're in less danger from time travel paradoxes than I previously assumed.

##A Quick Example of Rebase

Just so we all are on the same page, let's go through a quick example of how you might use rebase:

Let's assume that you have a git repository with a file in it and that you've branched that file and made some changes. Meanwhile, someone else has modified that same file on the master branch. In order to get everything put back together again, you may consider using git rebase. To do so, you would need to do the following:

	$ git rebase master

That's it. There might be some conflicts that you'd need to go in and clean up if your co-coder has been up to some serious business since you've last merged in your changes, but the command itself is simple. Now it looks like your changes started from the current master rather than from the original branch point.

If you want to now add your up-to-date changes back into the master, you'll still need to merge it in.

	$ git checkout master
	$ git merge branchname

How is this whole process different from just using git merge in the first place? It's just prettier: someone going through the code's history would see straight forward progress along the master branch.

##A Better Metaphor for Rebase

Rebase is generally considered a slightly-nuclear option. It's possible to be careful about rebasing code, say by duplicating the master branch and rebasing your code on that new version to see if you accidentally destroy the world before trying to rebase within the actual master. Somehow, though, we still see it as something dangerous.

<a href="http://marklodato.github.com/visual-git-guide/index-en.html"><img src="http://marklodato.github.com/visual-git-guide/rebase.svg" align="right" width="400" height="400"/></a>

Perhaps a new metaphor may be more useful here. I'm the type to go out and read a bunch about a particular command before I'll get comfortable with using it. I've gone over [this section from ProGit](http://git-scm.com/book/en/Git-Branching-Rebasing) a couple of times and something finally became clear: when you rebase, you can reorder a whole bunch of different things!

For me, this is like sewing. When I was little, I would help my grandmother with her sewing projects. She grew up in the Great Depression and not one bit of material would ever go to waste in her sewing room. A piece of clothing didn't fit right? She'd tailor it. A seam wound up in the wrong place? She'd rip it out and go again. A project went horribly, horribly wrong? She'd take it apart and put it together again in a different way.

Rebase is a seam ripper and a bowl full of pins, all in one. You've got a bunch of concrete pieces of code that you've committed over time and you can rip them apart with rebase. In the same action, you can pin them back together and run them through the sewing machine again. As a result, you're not just limited to what you might do with the master branch and whatever branch you've been working on seperately. 

Just like in sewing, though, there are some rules that you absolutely need to follow. The "don't accidentally sew your fingers to the garment" rule of rebasing is that **you should never rebase commits that you have pushed to a public repository.** It's not out of the question to fix such a problem (and there's probably less blood than the sewing machine-finger combo), but it requires some serious clean up.

##Measure Twice, Cut Once
In fact, as long as you're taking proper precautions, it's possible to come back from most rebase screw ups (though this opinion is based on my own, admittedly limited, experience). The precautions seems a little tedious, just like measuring fabric twice and double-checking that you know what to do with your pattern can be. But that tedium can help you avoid big screw-ups, even if you never notice the accident you avoided.

The moment that I realized that rebase isn't so much a bomb as a seam ripper, it was a lot less worrying to type in that command and hit 'enter.'

---

Written by our own PDX PyLady, [@thursdayb](https://twitter.com/thursdayb) and regularly writes for her [blog](http://thursdaybram.com).