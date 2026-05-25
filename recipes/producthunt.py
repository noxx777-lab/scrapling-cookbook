"""ProductHunt product scraper — extracts tagline, upvotes, makers, topics, description."""
from scrapling.fetchers import StealthyFetcher

def scrape_producthunt_product(url: str) -> dict:
    StealthyFetcher.adaptive = True
    page = StealthyFetcher.fetch(url, headless=True, network_idle=True)
    return {
        "name": page.css('h1::text, [class*="name"] h1::text').get(default='').strip(),
        "tagline": page.css('[class*="tagline"]::text, [class*="tagline"] p::text').get(default='').strip(),
        "upvotes": page.css('[class*="vote"] button::text, [data-test="vote-count"]::text').get(default='').strip(),
        "description": page.css('[class*="description"] ::text, [class*="body"] p::text').get(default='').strip()[:500],
        "makers": page.css('[class*="maker"] a::text, [class*="user"] [class*="name"]::text').getall(),
        "topics": page.css('[class*="topic"] a::text, [class*="tag"] ::text').getall(),
        "website": page.css('a[class*="website"]::attr(href), a[data-test="product-url"]::attr(href)').get(default='').strip(),
        "launched": page.css('[class*="launched"]::text, time::text').get(default='').strip(),
    }
