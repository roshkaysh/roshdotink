# Site Guide

A quick reference for managing and updating this Jekyll blog.

---

## Writing a Blog Post

All posts go in the `_posts/` folder. The filename **must** follow this format:

```
_posts/YYYY-MM-DD-title-with-dashes.md
```

Every post needs a front matter block at the top:

```markdown
---
layout: post
title: My Post Title
date: 2026-03-14
description: A short summary shown in the blog listing.
tags: [writing, personal]        # optional
categories: [essays]             # optional
---

Your post content goes here.
```

The post will be live at `/blog/YYYY/title-with-dashes/`.

### Optional front matter fields

| Field | What it does |
|---|---|
| `tags` | Adds hashtag links on the listing page |
| `categories` | Adds category links on the listing page |
| `featured: true` | Pins the post as a featured card at the top of the blog |
| `thumbnail` | Path to an image shown as a thumbnail in the listing (e.g. `/assets/img/thumb.jpg`) |
| `toc: {beginning: true}` | Adds a table of contents at the top of the post |
| `giscus_comments: true` | Enables comments on this post (requires Giscus to be configured in `_config.yml`) |
| `redirect` | Redirect to an external URL instead of showing post content |

### Draft posts

Don't want a post to go live yet? Either:
- Keep the file outside `_posts/` (e.g. in a `_drafts/` folder)
- Use a future date — Jekyll won't publish it until that date passes

---

## Adding a New Page

Pages go in `_pages/`. Create a new `.md` file:

```markdown
---
layout: page
title: my page
permalink: /my-page/
nav: true          # set to true to show in the navbar
nav_order: 5       # controls the order in the navbar
description: Optional subtitle shown below the title.
---

Page content here.
```

Current pages and their nav order:
- `blog.md` → nav_order: 1
- `cinema.md` → nav_order: 3
- `about.md` → homepage (`permalink: /`)

---

## Updating the About Page

Edit `_pages/about.md`. The content below the front matter is the body of the page.

To change the profile image, replace `assets/img/rosh_ink.jpg` with your image (keep the same filename, or update the `image:` field in the front matter).

---

## Updating Your Socials

Edit `_data/socials.yml`. The icons shown on the about page are controlled here.

Common fields:

```yaml
email: you@example.com
github_username: yourhandle
twitter_username: yourhandle
linkedin_username: yourhandle
rss_icon: true   # comment out to hide RSS
```

Remove or comment out any social you don't want shown.

---

## Site-wide Settings (`_config.yml`)

Key settings to know:

| Setting | What to change |
|---|---|
| `title` | Your name shown in the browser tab |
| `description` | Site tagline |
| `url` | Your GitHub Pages URL (e.g. `https://yourusername.github.io`) |
| `blog_name` | Heading shown at the top of the blog listing |
| `blog_description` | Subheading on the blog listing |
| `display_tags` | List of tags to show as filter links on the blog page |
| `display_categories` | List of categories to show as filter links |
| `search_enabled` | Toggle the search bar |
| `navbar_fixed` | Sticky navbar |
| `footer_fixed` | Sticky footer |

After editing `_config.yml`, you need to restart Jekyll locally for changes to take effect.

---

## Adding Images to Posts

Put images in `assets/img/`. Reference them in posts like:

```markdown
![alt text](/assets/img/my-image.jpg)
```

Or with a caption using the `figure.liquid` include:

```liquid
{% include figure.liquid path="assets/img/my-image.jpg" caption="My caption here" %}
```

---

## Letterboxd / Cinema Page

The cinema page (`_pages/cinema.md`) is auto-populated from your Letterboxd account.

- **Diary data** is fetched from your public Letterboxd RSS feed and saved to `_data/letterboxd_diary.json`
- The GitHub Action at `.github/workflows/letterboxd.yml` runs this fetch daily at 4 AM UTC
- To trigger a manual update: go to **Actions → Fetch Letterboxd Data → Run workflow** on GitHub
- The fetch script is at `_scripts/fetch_letterboxd.py`

---

## Deploying

The site is deployed to GitHub Pages automatically via `.github/workflows/deploy.yml` whenever you push to `main`.

To preview locally (requires Ruby and Bundler):

```bash
bundle exec jekyll serve
```

Then open `http://localhost:4000`.
