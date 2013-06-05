---
title: Arxiu de Noticies
layout: post
author: Ajuntament de Pego
date: "now"
---
<div class="span-13 news">
    <ul>
    {% for post in site.posts offset:10 %}
        <li>
            <strong>{{ post.date | date: "%d-%m-%Y" }}</strong>&nbsp;
            <a href="{{ post.url }}">{{ post.title }}</a>
        </li>
    {% endfor %}
    </ul>
</div>