"""Wikipedia article scraper — extracts title, summary, sections, links."""
from scrapling.fetchers import Fetcher

def scrape_wikipedia(url: str) -> dict:
    page = Fetcher.fetch(url)
    
    return {
        "title": page.css('#firstHeading::text').get(default='').strip(),
        "summary": ' '.join(p.strip() for p in page.css('.mw-parser-output > p::text').getall()[:3]),
        "sections": [h.strip() for h in page.css('.mw-headline::text').getall()],
        "infobox": {
            row.css('th::text').get(default='').strip(): row.css('td::text').get(default='').strip()
            for row in page.css('.infobox tr')
        },
        "external_links": page.css('.mw-parser-output a.external::attr(href)').getall()[:20],
    }
