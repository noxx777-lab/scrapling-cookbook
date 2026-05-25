"""G2 product review scraper — extracts rating, reviews count, pros/cons."""
from scrapling.fetchers import StealthyFetcher

def scrape_g2_reviews(url: str) -> dict:
    StealthyFetcher.adaptive = True
    page = StealthyFetcher.fetch(url, headless=True, network_idle=True)
    return {
        "product_name": page.css('h1::text, [class*="product-name"]::text').get(default='').strip(),
        "rating": page.css('[class*="star-rating"]::attr(aria-label), [class*="rating"]::text').get(default='').strip(),
        "reviews_count": page.css('[class*="reviews-count"]::text').get(default='').strip(),
        "description": page.css('[class*="description"] p::text, [class*="overview"]::text').get(default='').strip(),
        "categories": page.css('[class*="category"] a::text, [class*="breadcrumb"] a::text').getall(),
        "pricing": page.css('[class*="pricing"] ::text').get(default='').strip(),
    }
