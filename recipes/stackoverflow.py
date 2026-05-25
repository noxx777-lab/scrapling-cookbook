"""StackOverflow question scraper — title, votes, answers, tags."""
from scrapling.fetchers import Fetcher

def scrape_stackoverflow_question(url: str) -> dict:
    page = Fetcher.get(url, headers={"User-Agent": "Mozilla/5.0"})
    return {
        "title": page.css('h1 a::text').get(default='').strip(),
        "votes": page.css('.js-vote-count::attr(data-value)').get(default='0').strip(),
        "question": page.css('.question .js-post-body, #question .s-prose').get(default='').strip()[:300],
        "answers_count": page.css('[itemprop="answerCount"]::text, #answers-header h2::attr(data-answercount)').get(default='0').strip(),
        "tags": page.css('.post-tag::text').getall(),
        "views": page.css('[title*="views"]::text').get(default='').strip(),
    }
