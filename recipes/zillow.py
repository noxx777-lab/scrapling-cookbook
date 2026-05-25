"""Zillow property scraper — extracts price, beds, baths, sqft, address."""
from scrapling.fetchers import StealthyFetcher

def scrape_zillow(url: str) -> dict:
    StealthyFetcher.adaptive = True
    page = StealthyFetcher.fetch(url, headless=True, network_idle=True)
    return {
        "price": page.css('[data-testid="price"]::text, .ds-price::text').get(default='').strip(),
        "address": page.css('[data-testid="home-details-chip"]::text, h1::text').get(default='').strip(),
        "beds": page.css('[data-testid="bed-bath-beyond"] span::text').getall(),
        "sqft": page.css('.ds-summary-row span::text').get(default='').strip(),
        "description": page.css('[data-testid="description"] ::text, .ds-home-description ::text').get(default='').strip(),
    }
