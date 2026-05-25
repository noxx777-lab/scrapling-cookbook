"""Crunchbase company scraper — extracts funding, employees, industry."""
from scrapling.fetchers import StealthyFetcher

def scrape_crunchbase(url: str) -> dict:
    StealthyFetcher.adaptive = True
    page = StealthyFetcher.fetch(url, headless=True, network_idle=True)
    return {
        "name": page.css('h1::text').get(default='').strip(),
        "description": page.css('.description ::text, [class*="description"] ::text').get(default='').strip(),
        "funding": page.css('[class*="funding"] ::text').get(default='').strip(),
        "employees": page.css('[class*="employees"] ::text').get(default='').strip(),
        "industry": page.css('[class*="categories"] ::text, [class*="industry"] a::text').getall(),
        "website": page.css('a[href*="http"]::attr(href)').get(default='').strip(),
    }
