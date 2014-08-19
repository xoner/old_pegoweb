---
title: Arxiu de Noticies
layout: content_layout
section: blog
author: Ajuntament de Pego
date: "now"
description: Històric de les noticies publicades a la plana web de l'Ajuntament de Pego.
---
<div class="row">
    <div class="col-md-12">
        <ul>
        {% for post in site.posts offset:10 %}
            <li>
                <strong>{{ post.date | date: "%d-%m-%Y" }}</strong>&nbsp;
                <a href="{{ post.url }}">{{ post.title }}</a>
            </li>
        {% endfor %}
        </ul>
    </div>
</div>