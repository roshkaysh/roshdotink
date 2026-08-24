---
layout: page
title: links
permalink: /links/
nav: true
nav_order: 5
description: things worth sharing
_styles: >
  .links-filters {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem 1rem;
    margin: 1.5rem 0 2rem;
    font-size: 0.875rem;
    color: var(--global-text-color-light);
  }
  .links-filter-btn {
    background: none;
    border: none;
    padding: 0;
    color: var(--global-text-color-light);
    font-size: 0.875rem;
    cursor: pointer;
  }
  .links-filter-btn:hover,
  .links-filter-btn.active {
    color: var(--global-theme-color);
  }
  .links-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .link-entry {
    padding: 0.9rem 0;
    border-bottom: 1px solid var(--global-divider-color);
  }
  .link-entry:first-child { padding-top: 0; }
  .link-title {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    gap: 1rem;
    font-size: 0.95rem;
    font-weight: 600;
    margin: 0 0 0.25rem;
  }
  .link-title a {
    color: var(--global-text-color);
    text-decoration: none;
  }
  .link-title a:hover { color: var(--global-theme-color); }
  .link-date {
    font-size: 0.8rem;
    font-weight: 400;
    color: var(--global-text-color-light);
    white-space: nowrap;
    flex-shrink: 0;
  }
  .link-description {
    font-size: 0.875rem;
    color: var(--global-text-color-light);
    margin: 0 0 0.25rem;
    line-height: 1.5;
  }
  .link-meta {
    color: var(--global-text-color-light);
    font-size: 0.875rem;
    padding-top: 0.25rem;
  }
  .link-meta a {
    color: var(--global-text-color-light);
    text-decoration: none;
  }
  .link-meta a:hover { color: var(--global-theme-color); }
  .link-entry.hidden { display: none; }
---

{% assign all_links = site.data.links | sort: "date" | reverse %}

{% assign all_tags = "" | split: "" %}
{% for link in all_links %}
  {% for tag in link.tags %}
    {% unless all_tags contains tag %}
      {% assign all_tags = all_tags | push: tag %}
    {% endunless %}
  {% endfor %}
{% endfor %}
{% assign all_tags = all_tags | sort %}

<div class="links-filters">
  <button class="links-filter-btn active" data-tag="all">all</button>
  {% for tag in all_tags %}
  <button class="links-filter-btn" data-tag="{{ tag }}"><i class="fa-solid fa-hashtag fa-sm"></i> {{ tag }}</button>
  {% endfor %}
</div>

<ul class="links-list">
{% for link in all_links %}
<li class="link-entry" data-tags="{{ link.tags | join: ' ' }}">
  <div class="link-title">
    <a href="{{ link.url }}" target="_blank" rel="noopener">{{ link.title }}</a>
    <span class="link-date">{{ link.date | date: "%b %-d, %Y" }}</span>
  </div>
  {% if link.description %}<div class="link-description">{{ link.description }}</div>{% endif %}
  <div class="link-meta">
    {% for tag in link.tags %}
      <i class="fa-solid fa-hashtag fa-sm"></i> {{ tag }}{% unless forloop.last %}&nbsp;{% endunless %}
    {% endfor %}
  </div>
</li>
{% endfor %}
</ul>

<script>
(function () {
  var btns = document.querySelectorAll('.links-filter-btn');
  var entries = document.querySelectorAll('.link-entry');
  btns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var tag = this.getAttribute('data-tag');
      btns.forEach(function (b) { b.classList.remove('active'); });
      this.classList.add('active');
      entries.forEach(function (entry) {
        if (tag === 'all' || entry.getAttribute('data-tags').split(' ').indexOf(tag) !== -1) {
          entry.classList.remove('hidden');
        } else {
          entry.classList.add('hidden');
        }
      });
    });
  });
})();
</script>
