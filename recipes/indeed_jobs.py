"""Indeed job listing scraper — extracts title, company, location, salary."""
from scrapling.fetchers import StealthyFetcher

def scrape_indeed_jobs(search_url: str) -> list[dict]:
    """Scrape job listings from an Indeed search results page."""
    StealthyFetcher.adaptive = True
    page = StealthyFetcher.fetch(search_url, headless=True, network_idle=True)
    
    jobs = []
    for card in page.css('.job_seen_beacon, .resultContent, [data-testid="job-card"]'):
        jobs.append({
            "title": card.css('h2 a span::text, [data-testid="jobTitle"]::text').get(default='').strip(),
            "company": card.css('[data-testid="company-name"]::text, .companyName::text').get(default='').strip(),
            "location": card.css('[data-testid="text-location"]::text, .companyLocation::text').get(default='').strip(),
            "salary": card.css('[class*="salary"] ::text').get(default='').strip(),
        })
    return jobs
