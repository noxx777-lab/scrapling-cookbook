"""Shopify store product scraper — all products from a Shopify store."""
from scrapling.fetchers import Fetcher
import json

def scrape_shopify_products(store_url: str) -> list[dict]:
    """Scrape all products from a Shopify store via products.json API."""
    page = Fetcher.get(f"{store_url.rstrip('/')}/products.json")
    data = json.loads(page.css('body::text').get(default='[]'))
    return [{
        "title": p.get("title", ""),
        "price": p.get("variants", [{}])[0].get("price", ""),
        "vendor": p.get("vendor", ""),
        "type": p.get("product_type", ""),
        "tags": p.get("tags", []),
        "available": p.get("variants", [{}])[0].get("available", False),
    } for p in data.get("products", [])]
