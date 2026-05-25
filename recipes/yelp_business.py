"""Yelp business scraper — extracts name, rating, reviews, address, phone."""
from scrapling.fetchers import StealthyFetcher

def scrape_yelp_business(url: str) -> dict:
    StealthyFetcher.adaptive = True
    page = StealthyFetcher.fetch(url, headless=True, network_idle=True)
    
    return {
        "name": page.css('h1::text').get(default='').strip(),
        "rating": page.css('[aria-label*="star rating"]::attr(aria-label)').get(default='').strip(),
        "reviews_count": page.css('[aria-label*="reviews"]::text').get(default='').strip(),
        "address": page.css('address ::text').getall(),
        "phone": page.css('[href^="tel:"]::text').get(default='').strip(),
        "website": page.css('[href*="biz_redir"]::attr(href)').get(default='').strip(),
        "categories": page.css('[class*="category"] a::text').getall(),
    }
