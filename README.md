# Scrapling Cookbook — 20+ Ready-to-Use Scraping Recipes

**Stop writing selectors from scratch.** Drop these recipes into your Scrapling project and start extracting data immediately.

## What You Get

20+ pre-built, tested scraping recipes for the most-requested websites. Each recipe is a single Python file — copy, paste, and you're extracting data in 30 seconds.

Every recipe uses Scrapling's adaptive selectors, so they survive website redesigns.

## Sites Covered

| Category | Sites |
|----------|-------|
| E-commerce | Amazon, eBay, Shopify stores, AliExpress |
| Social Media | Reddit, Twitter/X, ProductHunt, Hacker News |
| Business Data | Yelp, Google Maps, Yellow Pages, Trustpilot |
| Jobs | Indeed, LinkedIn (public profiles), Glassdoor |
| Real Estate | Zillow, Realtor.com |
| Developer | GitHub, StackOverflow, npm, PyPI |
| Content | Wikipedia, Medium, news sites, blogs |
| Finance | Yahoo Finance, CoinMarketCap, Crunchbase |

## Example: Amazon Product in 3 Lines

```python
from recipes.amazon_product import scrape_amazon_product
data = scrape_amazon_product("https://amazon.com/dp/B0EXAMPLE")
print(data["title"], data["price"])  # "Widget Pro" "$29.99"
```

## Pricing

**€19 one-time** — lifetime access, all future recipes included.

Pay via:
- **Crypto (ETH/USDC):** `0x` (wallet address)
- **Gumroad:** [link coming soon]

After payment, you get instant access to the full recipe collection + updates.

## Why Pay?

You could write these selectors yourself — but each one takes 30-90 minutes of inspecting DOM, testing, and debugging. 20 recipes × 45 minutes = 15 hours of work. At any reasonable hourly rate, €19 pays for itself in the first recipe you don't have to write.

## Requirements

- Python 3.10+
- Scrapling (`pip install scrapling`)
- Playwright (`pip install playwright && playwright install`)

## Refund Policy

Not satisfied? Email noxx777@proton.me within 7 days for a full refund. No questions asked.

---

**Built by a developer tired of writing the same selectors for the 20th time.**
