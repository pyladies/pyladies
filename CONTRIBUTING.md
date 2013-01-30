{% extends "site.html" %}
{% block title %}Guest Post{% endblock %}
{% block content %}
    <section id="archive">
        <h1>Guest Post Guidelines</h1>
        <article>
            <aside>
                <p>We accept guest posts for the Pyladies blog. Here is a guest post that you should read as samples of what we're looking for:</p>

                <ul><li><a href="http://www.pyladies.com/blog/get-the-most-out-of-your-conference-going-experience/">Get the Most Out of Your Conference-Going Experience</a></li></ul>

                <h2>Topics</h2>

                <p>We're looking for posts about Python and the ladies doing cool things with it. Our audience includes both experts and newer programmers. If you're writing a more expert level post, consider pointing newer programmers to resources to get started with.</p>

                <h2>Length</h2>

                <p>Posts should be 500 words in length. If your post is much longer (thousands of words), consider whether it could be broken into two connected posts.</p>

                <h2>Images</h2>

                <p>If you wish to include images, they must be 500 pixels wide or less. You should own the images you're submitting or they should be available under a Creative Commons license.</p>

                <h2>Formatting</h2>

                <p>Write your guest post in Markdown (Suggestion: Mou.app for mac is created for Markdown - gives you a preview while you write) (Suggestion #2: http://dillinger.io/ is a web app that provides a live preview when you're writing in Markdown).</p>

                <p>A cheatsheet for Markdown commands is at <a href="http://daringfireball.net/projects/markdown/syntax">http://daringfireball.net/projects/markdown/syntax</a>.</p>

                <p>The very top of the blog post needs the following (including the three dashes before and after the layout/title/tags):</p>

                <blockquote>---
                layout: post.html
                title: "Your title here"
                tags: [list, of relevant, tags]
                ---</blockquote>

                <h2>Submission Method</h2>

                <p>To submit your post:</p>

                <p>Save in _posts</p>

                <p>(PyLadies) $ mynt _gen -f _site && mynt serve _site</p>

                <p>When you submit a pull request, everyone with commit access for Pyladies will see it.</p>

            </aside>

        </article>
    </section>
{% endblock %}