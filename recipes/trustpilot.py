"""Trustpilot review scraper — company reviews, ratings, reviewer names."""
from scrapling.fetchers import StealthyFetcher

def scrape_trustpilot_reviews(url: str) -> list[dict]:
    StealthyFetcher.adaptive = True
    page = StealthyFetcher.fetch(url, headless=True, network_idle=True)
    
    reviews = []
    for card in page.css('article.review, [data-review-content]'):
        reviews.append({
            "reviewer": card.css('[data-consumer-name-typography]::text, .consumer-information__name::text').get(default='').strip(),
            "rating": card.css('[data-service-review-rating] img::attr(alt), .star-rating img::attr(alt)').get(default='').strip(),
            "title": card.css('[data-service-review-title-typography]::text, .review-content__title::text').get(default='').strip(),
            "text": card.css('[data-service-review-text-typography]::text, .review-content__text::text').get(default='').strip(),
            "date": card.css('[data-service-review-date] time::attr(datetime), .review-content-header__dates time::attr(datetime)').get(default='').strip(),
        })
    return reviews
