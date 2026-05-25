"""LinkedIn public profile scraper — extracts name, headline, location, about."""
from scrapling.fetchers import StealthyFetcher

def scrape_linkedin_profile(url: str) -> dict:
    StealthyFetcher.adaptive = True
    page = StealthyFetcher.fetch(url, headless=True, network_idle=True)
    return {
        "name": page.css('h1::text, .top-card-layout__title::text').get(default='').strip(),
        "headline": page.css('.top-card-layout__headline::text, h2::text').get(default='').strip(),
        "location": page.css('.top-card__subline-item::text').get(default='').strip(),
        "about": page.css('.summary::text, #about ~ p::text').get(default='').strip(),
        "current_company": page.css('.experience-group-header__company::text, .experience-item__subtitle::text').get(default='').strip(),
        "followers": page.css('[class*="follower"]::text').get(default='').strip(),
    }
