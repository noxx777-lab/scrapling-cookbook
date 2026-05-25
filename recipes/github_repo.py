"""GitHub repo scraper — stats, language, topics."""
from scrapling.fetchers import Fetcher

def scrape_github_repo(url: str) -> dict:
    page = Fetcher.get(url)
    
    return {
        "name": page.css('strong[itemprop="name"] a::text').get(default='').strip(),
        "stars": page.css('#repo-stars-counter-star::attr(title)').get(default='').strip(),
        "forks": page.css('#repo-network-counter::attr(title)').get(default='').strip(),
        "language": page.css('[data-ga-click*="language"] span::text').get(default='').strip(),
        "topics": [t.strip() for t in page.css('.topic-tag::text').getall()],
        "description": page.css('p.f4.my-3::text').get(default='').strip(),
    }
