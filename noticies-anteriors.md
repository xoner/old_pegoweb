---
title: Arxiu de Notícies
layout: page_layout
section: blog
author: Ajuntament de Pego
date: "now"
description: Històric de les notícies publicades a la plana web de l'Ajuntament de Pego.
---
<div class="row">
    <div class="col-md-12">
        <ul>
        {% assign curr_year = 0 %}
        {% for post in site.posts offset:10 %}
            {% assign post_year = post.date | date: "%Y" %}
            {% if curr_year != post_year %}
                {% assign curr_year = post_year %}
                </ul>
                <h3>{{ curr_year }}</h3>
                <ul>
            {% endif %}
            <li>
                <strong>{{ post.date | date: "%d-%m-%Y" }}</strong>&nbsp;
                <a href="{{ post.url }}">{{ post.title }}</a>
            </li>
        {% endfor %}
        </ul>
    </div>
</div>