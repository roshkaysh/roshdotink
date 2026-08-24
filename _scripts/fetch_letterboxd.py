import json
import re
import urllib.request
import xml.etree.ElementTree as ET

USERNAME = "roshkaysh"
LB_NS = "https://letterboxd.com"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "jekyll-letterboxd/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def extract_poster(html):
    m = re.search(r'<img src="([^"]+)"', html or "")
    return m.group(1) if m else None


def extract_review(html):
    if not html:
        return ""
    html = re.sub(r"<p>\s*<img[^>]+>\s*</p>", "", html)
    html = re.sub(r"<p>Watched on.*?</p>", "", html, flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", "", html).strip()
    return text


# --- Diary (recent films watched) ---
diary = []
try:
    xml = fetch(f"https://letterboxd.com/{USERNAME}/rss/")
    root = ET.fromstring(xml)
    for item in root.findall(".//item"):
        film_title = item.findtext(f"{{{LB_NS}}}filmTitle")
        if not film_title:
            continue  # skip list updates and non-film entries
        description = item.findtext("description") or ""
        rating_str = item.findtext(f"{{{LB_NS}}}memberRating")
        entry = {
            "title": film_title,
            "year": item.findtext(f"{{{LB_NS}}}filmYear") or "",
            "rating": float(rating_str) if rating_str else None,
            "watched_date": item.findtext(f"{{{LB_NS}}}watchedDate") or "",
            "url": item.findtext("link") or "",
            "poster": extract_poster(description),
            "review": extract_review(description),
        }
        diary.append(entry)
    print(f"Fetched {len(diary)} diary entries")
except Exception as e:
    print(f"Error fetching diary: {e}")

with open("_data/letterboxd_diary.json", "w", encoding="utf-8") as f:
    json.dump(diary, f, indent=2, ensure_ascii=False)

# --- Watchlist ---
watchlist = []
try:
    xml = fetch(f"https://letterboxd.com/{USERNAME}/watchlist/rss/")
    root = ET.fromstring(xml)
    for item in root.findall(".//item"):
        description = item.findtext("description") or ""
        film_title = item.findtext(f"{{{LB_NS}}}filmTitle") or ""
        film_year = item.findtext(f"{{{LB_NS}}}filmYear") or ""
        if not film_title:
            raw = item.findtext("title") or ""
            m = re.match(r"^(.+?)\s*\((\d{4})\)$", raw)
            film_title, film_year = (m.group(1), m.group(2)) if m else (raw, "")
        watchlist.append(
            {
                "title": film_title,
                "year": film_year,
                "url": item.findtext("link") or "",
                "poster": extract_poster(description),
            }
        )
    print(f"Fetched {len(watchlist)} watchlist items")
except Exception as e:
    print(f"Error fetching watchlist: {e}")

with open("_data/letterboxd_watchlist.json", "w", encoding="utf-8") as f:
    json.dump(watchlist, f, indent=2, ensure_ascii=False)
