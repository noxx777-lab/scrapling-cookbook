"""Medium article scraper — extracts title, author, claps, reading time, content preview."""
from scrapling.fetchers import StealthyFetcher

def scrape_medium_article(url: str) -> dict:
    StealthyFetcher.adaptive = True
    page = StealthyFetcher.fetch(url, headless=True, network_idle=True)
    return {
        "title": page.css('h1::text, [data-testid="storyTitle"]::text').get(default='').strip(),
        "author": page.css('a[href*="/@"] p::text, [class*="author"] a::text').get(default='').strip(),
        "claps": page.css('[class*="clap"] button::text, [data-testid="clapCount"]::text').get(default='').strip(),
        "reading_time": page.css('[class*="readingTime"]::text, [data-testid="readingTime"]::text').get(default='').strip(),
        "published": page.css('[class*="publish"] span::text, time::text').get(default='').strip(),
        "content_preview": page.css('article p::text, section p::text').get(default='').strip()[:500],
        "tags": page.css('a[href*="/tag/"]::text, [class*="tag"] a::text').getall(),
    }
