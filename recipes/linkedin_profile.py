"""LinkedIn public profile scraper — extracts name, title, company, location."""
from scrapling.fetchers import StealthyFetcher

def scrape_linkedin_profile(url: str) -> dict:
    StealthyFetcher.adaptive = True
    page = StealthyFetcher.fetch(url, headless=True, network_idle=True)
    return {
        "name": page.css('h1::text').get(default='').strip(),
        "headline": page.css('.text-body-medium::text').get(default='').strip(),
        "current_company": page.css('.pv-text-details__right-panel ~ div span::text').get(default='').strip(),
        "location": page.css('.text-body-small.inline.t-black--light::text').get(default='').strip(),
        "about": page.css('#about ~ div span::text, .pv-shared-text-with-see-more span::text').get(default='').strip(),
    }
