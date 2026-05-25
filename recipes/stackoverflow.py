"""StackOverflow question scraper — extracts title, question body, answers, tags, votes."""
from scrapling.fetchers import StealthyFetcher

def scrape_stackoverflow_question(url: str) -> dict:
    StealthyFetcher.adaptive = True
    page = StealthyFetcher.fetch(url, headless=True, network_idle=True)
    answers = []
    for ans in page.css('.answer'):
        answers.append({
            "body": ans.css('.s-prose, .answercell .js-post-body::text').get(default='').strip()[:500],
            "votes": ans.css('.js-vote-count::text, [class*="vote"] span::text').get(default='').strip(),
            "accepted": bool(ans.css('.accepted-answer')),
        })
    return {
        "title": page.css('h1 a.question-hyperlink::text, h1::text').get(default='').strip(),
        "body": page.css('.question .s-prose::text, .js-post-body::text').get(default='').strip()[:500],
        "tags": page.css('.post-tag::text').getall(),
        "votes": page.css('.js-vote-count::text, [class*="vote-count"]::text').get(default='').strip(),
        "answers_count": len(answers),
        "answers": answers,
        "views": page.css('[class*="views"]::attr(title), [class*="views"] span::text').get(default='').strip(),
    }
