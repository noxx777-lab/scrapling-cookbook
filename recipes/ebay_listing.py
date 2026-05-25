"""eBay listing scraper — extracts title, price, condition, seller."""
from scrapling.fetchers import StealthyFetcher

def scrape_ebay_listing(url: str) -> dict:
    StealthyFetcher.adaptive = True
    page = StealthyFetcher.fetch(url, headless=True)
    
    return {
        "title": page.css('h1.it-ttl::text, .x-item-title__mainTitle span::text').get(default='').strip(),
        "price": page.css('.x-price-primary span::text, [itemprop="price"]::attr(content)').get(default='').strip(),
        "condition": page.css('.x-item-condition-max-line .ux-textspans::text').get(default='').strip(),
        "seller": page.css('.x-sellercard-atf__info-about span::text').get(default='').strip(),
    }
