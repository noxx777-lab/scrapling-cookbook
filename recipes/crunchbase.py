"""Crunchbase company scraper — extracts funding, employees, industry, description."""
from scrapling.fetchers import StealthyFetcher

def scrape_crunchbase_company(url: str) -> dict:
    StealthyFetcher.adaptive = True
    page = StealthyFetcher.fetch(url, headless=True, network_idle=True)
    return {
        "name": page.css('h1::text, .profile-name::text').get(default='').strip(),
        "description": page.css('.description::text, [class*="description"] p::text').get(default='').strip(),
        "industry": page.css('[class*="categories"] a::text, [class*="category"] a::text').getall(),
        "headquarters": page.css('[class*="headquarters"]::text, [class*="location"] ::text').get(default='').strip(),
        "founded": page.css('[class*="founded"]::text').get(default='').strip(),
        "funding_total": page.css('[class*="funding"] ::text, [class*="total-funding"]::text').get(default='').strip(),
        "employees": page.css('[class*="employees"]::text, [class*="size"] ::text').get(default='').strip(),
        "website": page.css('a[rel="nofollow noopener"]::attr(href), [class*="website"] a::attr(href)').get(default='').strip(),
    }
