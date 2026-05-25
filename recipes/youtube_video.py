"""YouTube video scraper — extracts title, views, likes, description, channel info."""
from scrapling.fetchers import StealthyFetcher

def scrape_youtube_video(url: str) -> dict:
    StealthyFetcher.adaptive = True
    page = StealthyFetcher.fetch(url, headless=True, network_idle=True)
    return {
        "title": page.css('h1 yt-formatted-string::text, h1::text, #title h1::text').get(default='').strip(),
        "views": page.css('#info span:first-child::text, .view-count::text').get(default='').strip(),
        "likes": page.css('#top-level-buttons-computed > *:first-child ::text').get(default='').strip(),
        "description": page.css('#description-inline-expander ::text, #description ::text').get(default='').strip(),
        "channel": page.css('#channel-name yt-formatted-string a::text, #owner yt-formatted-string a::text').get(default='').strip(),
        "subscribers": page.css('#owner-sub-count::text').get(default='').strip(),
        "published": page.css('#info yt-formatted-string::text, .date::text').get(default='').strip(),
    }
