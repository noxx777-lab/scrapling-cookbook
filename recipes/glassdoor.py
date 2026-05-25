"""Glassdoor company scraper — extracts rating, reviews, salary, CEO approval."""
from scrapling.fetchers import StealthyFetcher

def scrape_glassdoor_company(url: str) -> dict:
    StealthyFetcher.adaptive = True
    page = StealthyFetcher.fetch(url, headless=True, network_idle=True)
    return {
        "name": page.css('[data-test="company-name"]::text, h1::text').get(default='').strip(),
        "rating": page.css('[data-test="rating"]::text, .ratingNum::text').get(default='').strip(),
        "reviews_count": page.css('[data-test="reviews-count"]::text, .reviewCount::text').get(default='').strip(),
        "salaries_count": page.css('[data-test="salaries-count"]::text').get(default='').strip(),
        "ceo_approval": page.css('[data-test="ceo-approval"]::text, .ceoApproval::text').get(default='').strip(),
        "recommend_to_friend": page.css('[data-test="recommend-rating"]::text').get(default='').strip(),
        "industry": page.css('[data-test="industry"]::text').get(default='').strip(),
        "headquarters": page.css('[data-test="headquarters"]::text').get(default='').strip(),
    }
