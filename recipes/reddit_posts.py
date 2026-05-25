"""Reddit post scraper — extracts title, score, comments, author."""
from scrapling.fetchers import Fetcher

def scrape_reddit_posts(subreddit_url: str) -> list[dict]:
    page = Fetcher.get(subreddit_url, headers={"User-Agent": "Mozilla/5.0"})
    
    posts = []
    for post in page.css('article, .thing, shreddit-post'):
        posts.append({
            "title": post.css('[slot="title"]::text, h3::text, .title::text').get(default='').strip(),
            "score": post.css('[score]::attr(score), .score::text').get(default='').strip(),
            "author": post.css('[author]::attr(author), .author::text').get(default='').strip(),
            "comments": post.css('[comment-count]::attr(comment-count), .comments::text').get(default='').strip(),
            "url": post.css('[permalink]::attr(permalink), a[data-click-id="body"]::attr(href)').get(default='').strip(),
        })
    return posts
