"""Amazon product scraper — extracts title, price, rating, reviews count."""
from scrapling.fetchers import StealthyFetcher

def scrape_amazon_product(url: str) -> dict:
    """Extract product details from an Amazon product page."""
    StealthyFetcher.adaptive = True
    page = StealthyFetcher.fetch(url, headless=True, network_idle=True)
    
    return {
        "title": page.css('#productTitle::text').get(default='').strip(),
        "price": page.css('.a-price .a-offscreen::text').get(default='').strip(),
        "rating": page.css('[data-hook="rating-out-of-text"]::text').get(default='').strip(),
        "reviews_count": page.css('#acrCustomerReviewText::text').get(default='').strip(),
        "availability": page.css('#availability span::text').get(default='').strip(),
        "brand": page.css('#bylineInfo::text').get(default='').strip(),
    }
