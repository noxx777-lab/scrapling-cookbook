"""Hacker News scraper — front page posts, scores, authors."""
from scrapling.fetchers import Fetcher

def scrape_hackernews(url: str = "https://news.ycombinator.com") -> list[dict]:
    page = Fetcher.get(url)
    posts = []
    
    # Get all titles and URLs
    titles = page.css('.titleline a::text').getall()
    urls = page.css('.titleline a::attr(href)').getall()
    scores = page.css('.score::text').getall()
    authors = page.css('.hnuser::text').getall()
    
    for i, title in enumerate(titles):
        posts.append({
            "title": title.strip(),
            "url": urls[i] if i < len(urls) else "",
            "score": scores[i].strip() if i < len(scores) else "0",
            "author": authors[i].strip() if i < len(authors) else "",
        })
    return posts
