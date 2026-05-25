"""YouTube video metadata scraper — title, views, likes, description."""
from scrapling.fetchers import Fetcher

def scrape_youtube_video(url: str) -> dict:
    page = Fetcher.fetch(url, headers={"User-Agent": "Mozilla/5.0"})
    return {
        "title": page.css('title::text').get(default='').replace(' - YouTube', '').strip(),
        "views": page.css('meta[itemprop="interactionCount"]::attr(content)').get(default='').strip(),
        "channel": page.css('link[itemprop="name"]::attr(content)').get(default='').strip(),
        "description": page.css('meta[itemprop="description"]::attr(content)').get(default='').strip(),
        "duration": page.css('meta[itemprop="duration"]::attr(content)').get(default='').strip(),
        "upload_date": page.css('meta[itemprop="uploadDate"]::attr(content)').get(default='').strip(),
    }
