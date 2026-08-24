---
layout: page
title: bookshelf
permalink: /bookshelf/
nav: true
nav_order: 4
description: books that have stayed with me
_styles: >
  .book-entry {
    display: flex;
    gap: 1.5rem;
    margin-bottom: 3rem;
    align-items: flex-start;
  }
  .book-cover {
    width: 140px;
    min-width: 140px;
    aspect-ratio: 2/3;
    object-fit: cover;
    border-radius: 3px;
    box-shadow: 2px 4px 12px rgba(0,0,0,0.15);
  }
  .book-cover-placeholder {
    width: 140px;
    min-width: 140px;
    aspect-ratio: 2/3;
    border-radius: 3px;
    background: var(--global-divider-color);
  }
  .book-info h3 {
    margin: 0 0 0.2rem;
    font-size: 1.2rem;
  }
  .book-author {
    color: var(--global-text-color-light);
    margin-bottom: 0.8rem;
    font-size: 0.95rem;
  }
  .book-review {
    font-size: 0.9rem;
    line-height: 1.7;
  }
  hr.book-divider {
    margin: 0 0 3rem;
    border: none;
    border-top: 1px solid var(--global-divider-color);
  }
---

{% assign must_reads = site.data.must_reads %}

{% for book in must_reads %}
<div class="book-entry">
  {% if book.cover %}
    <img class="book-cover" src="{{ book.cover }}" alt="{{ book.title }}">
  {% else %}
    <div class="book-cover-placeholder"></div>
  {% endif %}
  <div class="book-info">
    <h3>{{ book.title }}</h3>
    <div class="book-author">{{ book.author }}</div>
    {% if book.review %}<div class="book-review">{{ book.review }}</div>{% endif %}
  </div>
</div>
{% unless forloop.last %}<hr class="book-divider">{% endunless %}
{% endfor %}
