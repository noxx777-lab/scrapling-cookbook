"""Medium article scraper — title, author, claps, reading time."""
from scrapling.fetchers import Fetcher

def scrape_medium_article(url: str) -> dict:
    page = Fetcher.get(url, headers={"User-Agent": "Mozilla/5.0"})
    return {
        "title": page.css('h1::text').get(default='').strip(),
        "author": page.css('[data-testid="authorName"]::text, a[rel="author"]::text').get(default='').strip(),
        "reading_time": page.css('span.readingTime::text').get(default='').strip(),
        "published_date": page.css('[data-testid="storyPublishDate"]::text, time::text').get(default='').strip(),
        "content_preview": page.css('article p::text').get(default='')[:500].strip(),
    }
