"""Hacker News scraper — front page posts, scores, comment counts."""
from scrapling.fetchers import Fetcher

def scrape_hackernews(url: str = "https://news.ycombinator.com") -> list[dict]:
    page = Fetcher.fetch(url)
    posts = []
    for row in page.css('.athing'):
        posts.append({
            "title": row.css('.titleline a::text').get(default='').strip(),
            "url": row.css('.titleline a::attr(href)').get(default='').strip(),
            "score": row.css('+ tr .score::text').get(default='0').strip(),
            "author": row.css('+ tr .hnuser::text').get(default='').strip(),
            "comments": row.css('+ tr a[href*="item"]::text').getall(),
        })
    return posts
