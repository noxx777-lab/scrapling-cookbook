"""Twitter/X profile scraper — extracts bio, followers, following, location, join date."""
from scrapling.fetchers import StealthyFetcher

def scrape_twitter_profile(url: str) -> dict:
    StealthyFetcher.adaptive = True
    page = StealthyFetcher.fetch(url, headless=True, network_idle=True)
    return {
        "display_name": page.css('[data-testid="UserName"] div::text, h1::text').get(default='').strip(),
        "handle": page.css('[data-testid="UserName"] span::text, [href*="/status/"]::text').get(default='').strip(),
        "bio": page.css('[data-testid="UserDescription"]::text, [class*="bio"]::text').get(default='').strip(),
        "followers": page.css('a[href*="followers"] span::text, a[href*="verified"] + a span::text').get(default='').strip(),
        "following": page.css('a[href*="following"] span::text').get(default='').strip(),
        "location": page.css('[data-testid="UserLocation"]::text').get(default='').strip(),
        "join_date": page.css('[data-testid="UserJoinDate"]::text').get(default='').strip(),
        "website": page.css('[data-testid="UserUrl"]::text, a[rel*="external"]::attr(href)').get(default='').strip(),
    }
