"""ProductHunt scraper — product launches, votes, tagline."""
from scrapling.fetchers import StealthyFetcher

def scrape_producthunt_launches(url: str = "https://www.producthunt.com/") -> list[dict]:
    StealthyFetcher.adaptive = True
    page = StealthyFetcher.fetch(url, headless=True, network_idle=True)
    
    products = []
    for item in page.css('[data-test="post-item"], .home-post'):
        products.append({
            "name": item.css('[data-test="post-name"]::text, h3::text').get(default='').strip(),
            "tagline": item.css('[data-test="post-tagline"]::text, .tagline::text').get(default='').strip(),
            "votes": item.css('[data-test="vote-count"]::text, .voteCount::text').get(default='').strip(),
            "url": item.css('a[href^="/post"]::attr(href)').get(default='').strip(),
        })
    return products
