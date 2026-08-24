---
layout: page
title: cinema
permalink: /cinema/
nav: true
nav_order: 3
description: films i've watched and want to watch
_styles: >
  .post-header { display: none; }
  .film-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
    gap: 1.2rem;
    margin: 1.5rem 0 2.5rem;
  }
  .film-card {
    display: flex;
    flex-direction: column;
    gap: 0.4rem;
  }
  .film-card a {
    text-decoration: none;
    color: inherit;
  }
  .film-poster {
    width: 100%;
    aspect-ratio: 2/3;
    object-fit: cover;
    border-radius: 4px;
    display: block;
    background: var(--global-divider-color);
  }
  .film-poster-placeholder {
    width: 100%;
    aspect-ratio: 2/3;
    border-radius: 4px;
    background: var(--global-divider-color);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.65rem;
    color: var(--global-text-color-light);
    text-align: center;
    padding: 0.5rem;
    line-height: 1.3;
  }
  .film-meta {
    font-size: 0.75rem;
    line-height: 1.3;
  }
  .film-title { font-weight: 600; }
  .film-year { color: var(--global-text-color-light); }
  .cinema-section-header {
    display: flex;
    align-items: baseline;
    gap: 1rem;
    margin-bottom: 0;
  }
  .cinema-section-header h2 { margin: 0; }
  .cinema-section-link { font-size: 0.85rem; }
  .rec-entry {
    display: flex;
    gap: 1.5rem;
    margin-bottom: 3rem;
    align-items: flex-start;
  }
  .rec-poster {
    width: 140px;
    min-width: 140px;
    aspect-ratio: 2/3;
    object-fit: cover;
    border-radius: 4px;
    box-shadow: 2px 4px 12px rgba(0,0,0,0.15);
  }
  .rec-poster-placeholder {
    width: 140px;
    min-width: 140px;
    aspect-ratio: 2/3;
    border-radius: 4px;
    background: var(--global-divider-color);
  }
  .rec-info h3 { margin: 0 0 0.2rem; font-size: 1.2rem; }
  .rec-meta { color: var(--global-text-color-light); font-size: 0.9rem; margin-bottom: 0.8rem; }
  .rec-note { font-size: 0.9rem; line-height: 1.7; }
  hr.rec-divider {
    margin: 0 0 3rem;
    border: none;
    border-top: 1px solid var(--global-divider-color);
  }
---

{% assign must_watch = site.data.must_watch %}
{% assign watchlist = site.data.letterboxd_watchlist %}

## must watch

things i'd genuinely recommend — films and shows that have stuck with me.

{% for item in must_watch %}
<div class="rec-entry">
  {% if item.poster %}
    <img class="rec-poster" src="{{ item.poster }}" alt="{{ item.title }}">
  {% else %}
    <div class="rec-poster-placeholder"></div>
  {% endif %}
  <div class="rec-info">
    <h3>{% if item.url %}<a href="{{ item.url }}" target="_blank">{{ item.title }}</a>{% else %}{{ item.title }}{% endif %}</h3>
    <div class="rec-meta">{{ item.type }} · {{ item.year }}</div>
    {% if item.note %}<div class="rec-note">{{ item.note }}</div>{% endif %}
  </div>
</div>
{% unless forloop.last %}<hr class="rec-divider">{% endunless %}
{% endfor %}

<div class="cinema-section-header"><h2>watchlist</h2>{% if watchlist.size > 0 %}<a class="cinema-section-link" href="https://letterboxd.com/roshkaysh/watchlist/" target="_blank">full watchlist →</a>{% endif %}</div>

{% if watchlist.size > 0 %}
<div class="film-grid">
{% for film in watchlist limit: 24 %}
<div class="film-card">
  <a href="{{ film.url }}" target="_blank">
    {% if film.poster %}
      <img class="film-poster" src="{{ film.poster }}" alt="{{ film.title }}" loading="lazy">
    {% else %}
      <div class="film-poster-placeholder">{{ film.title }}</div>
    {% endif %}
  </a>
  <div class="film-meta">
    <div class="film-title"><a href="{{ film.url }}" target="_blank">{{ film.title }}</a></div>
    <div class="film-year">{{ film.year }}</div>
  </div>
</div>
{% endfor %}
</div>
{% else %}
<p>watchlist is private — <a href="https://letterboxd.com/roshkaysh/watchlist/" target="_blank">view it here</a> instead.</p>
{% endif %}
