"""Wikipedia article scraper — extracts title, summary, sections, infobox, references."""
from scrapling.fetchers import StealthyFetcher

def scrape_wikipedia(url: str) -> dict:
    StealthyFetcher.adaptive = True
    page = StealthyFetcher.fetch(url, headless=True, network_idle=True)
    infobox = {}
    for row in page.css('.infobox tr'):
        key = row.css('th::text').get(default='').strip()
        val = row.css('td::text').get(default='').strip()
        if key and val:
            infobox[key] = val
    return {
        "title": page.css('#firstHeading::text, h1::text').get(default='').strip(),
        "summary": page.css('#mw-content-text .mw-parser-output > p:first-of-type::text').get(default='').strip(),
        "sections": page.css('.mw-headline::text').getall(),
        "infobox": infobox,
        "references": len(page.css('.references li, .reflist li')),
        "categories": page.css('#mw-normal-catlinks li a::text').getall(),
    }
