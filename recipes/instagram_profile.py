"""Instagram profile scraper — extracts bio, followers, following, post count."""
from scrapling.fetchers import StealthyFetcher

def scrape_instagram_profile(url: str) -> dict:
    StealthyFetcher.adaptive = True
    page = StealthyFetcher.fetch(url, headless=True, network_idle=True)
    return {
        "username": page.css('h2::text, header h1::text').get(default='').strip(),
        "bio": page.css('header section span::text, [class*="biography"]::text').get(default='').strip(),
        "followers": page.css('header ul li:nth-child(2) span::text, li a[href*="followers"] span::text').get(default='').strip(),
        "following": page.css('header ul li:nth-child(3) span::text, li a[href*="following"] span::text').get(default='').strip(),
        "posts_count": page.css('header ul li:nth-child(1) span::text, li > span > span::text').get(default='').strip(),
        "website": page.css('header a[href*="http"]::attr(href), a[rel*="external"]::attr(href)').get(default='').strip(),
    }
