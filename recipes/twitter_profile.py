"""Twitter/X profile scraper — extracts bio, followers, following, join date."""
from scrapling.fetchers import StealthyFetcher

def scrape_twitter_profile(url: str) -> dict:
    StealthyFetcher.adaptive = True
    page = StealthyFetcher.fetch(url, headless=True, network_idle=True)
    return {
        "name": page.css('[data-testid="UserName"] span::text').get(default='').strip(),
        "bio": page.css('[data-testid="UserDescription"]::text').get(default='').strip(),
        "followers": page.css('a[href*="verified_followers"] span::text, a[href*="followers"] span::text').get(default='').strip(),
        "following": page.css('a[href*="following"] span::text').get(default='').strip(),
        "location": page.css('[data-testid="UserLocation"]::text').get(default='').strip(),
        "website": page.css('[data-testid="UserUrl"]::text').get(default='').strip(),
    }
