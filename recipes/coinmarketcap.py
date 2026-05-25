"""CoinMarketCap crypto scraper — price, market cap, volume, supply."""
from scrapling.fetchers import StealthyFetcher

def scrape_coinmarketcap(url: str) -> dict:
    StealthyFetcher.adaptive = True  
    page = StealthyFetcher.fetch(url, headless=True, network_idle=True)
    return {
        "name": page.css('[data-role="header"] span::text, .sc-65e7f566-0::text').get(default='').strip(),
        "price": page.css('.priceValue span::text, [class*="priceValue"]::text').get(default='').strip(),
        "market_cap": page.css('[data-metric="market-cap"] dd::text, .statsValue::text').get(default='').strip(),
        "volume_24h": page.css('[data-metric="volume"] dd::text').get(default='').strip(),
        "circulating_supply": page.css('[data-metric="circulating-supply"] dd::text').get(default='').strip(),
        "rank": page.css('.namePill::text, .sc-16891c57-0::text').get(default='').strip(),
    }
