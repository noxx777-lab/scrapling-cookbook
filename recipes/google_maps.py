"""Google Maps business scraper — extracts name, rating, reviews, address, phone."""
from scrapling.fetchers import StealthyFetcher

def scrape_google_maps_business(url: str) -> dict:
    StealthyFetcher.adaptive = True
    page = StealthyFetcher.fetch(url, headless=True, network_idle=True)
    return {
        "name": page.css('h1::text').get(default='').strip(),
        "rating": page.css('[aria-label*="stars"]::text, .fontBodyMedium > span::text').get(default='').strip(),
        "reviews_count": page.css('button[aria-label*="reviews"]::text').get(default='').strip(),
        "address": page.css('[data-item-id="address"]::text, button[data-tooltip*="address"]::text').get(default='').strip(),
        "phone": page.css('[data-item-id*="phone"]::text, button[data-tooltip*="Phone"]::text').get(default='').strip(),
        "hours": page.css('[data-item-id="oh"] ::text').get(default='').strip(),
        "website": page.css('a[data-item-id="authority"]::attr(href), a[aria-label*="Website"]::attr(href)').get(default='').strip(),
    }
