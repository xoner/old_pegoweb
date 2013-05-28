---
title: Arxiu Noticies
layout: front_page
---
<div class="span-13 news">
    <ul>
    {% for post in site.posts offset:7 %}
        <li>
            <strong>{{ post.date | date: "%d-%m-%Y" }}</strong>&nbsp;
            <a href="{{ post.url }}">{{ post.title }}</a>
        </li>
    {% endfor %}
    </ul>
</div>