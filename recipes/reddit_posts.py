"""Reddit post scraper — extracts title, score, comments, author, selftext, flair."""
from scrapling.fetchers import StealthyFetcher

def scrape_reddit_posts(url: str) -> dict:
    StealthyFetcher.adaptive = True
    page = StealthyFetcher.fetch(url, headless=True, network_idle=True)
    posts = []
    for post in page.css('[data-testid="post-container"], article, shreddit-post'):
        posts.append({
            "title": post.css('h1::text, h3::text, [slot="title"]::text').get(default='').strip(),
            "score": post.css('[score]::attr(score), [class*="vote"]::text').get(default='').strip(),
            "comments": post.css('[comment-count]::attr(comment-count), [class*="comment"]::text').get(default='').strip(),
            "author": post.css('a[href*="/user/"]::text').get(default='').strip(),
            "selftext": post.css('[class*="selftext"]::text, [slot="text-body"]::text').get(default='').strip(),
            "flair": post.css('[class*="flair"]::text, [slot="flair"]::text').get(default='').strip(),
        })
    return {"posts": posts, "subreddit": page.css('h1::text, [class*="subreddit"] a::text').get(default='').strip()}
