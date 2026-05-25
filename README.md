# 🍳 Scrapling Cookbook — 23 Ready-to-Use Web Scraping Recipes

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Recipes](https://img.shields.io/badge/recipes-23-orange)](recipes/)
[![Built with Scrapling](https://img.shields.io/badge/built%20with-Scrapling-58a6ff)](https://github.com/nousresearch/hermes-agent)

**Stop writing selectors from scratch.** Drop these 23 pre-built, adaptive Scrapling recipes into your project and extract data in 30 seconds.

## ⚡ Quickstart (3 lines)

```python
from recipes.amazon_product import scrape_amazon_product
data = scrape_amazon_product("https://amazon.com/dp/B0EXAMPLE")
print(data["title"], data["price"])  # "Widget Pro" "$29.99"
```

## 📦 Installation

```bash
pip install scrapling playwright
playwright install
git clone https://github.com/noxx777-lab/scrapling-cookbook.git
cd scrapling-cookbook
```

## 🎯 What's Inside

23 single-file recipes covering the sites you actually need. Every recipe uses Scrapling's **adaptive selectors** — they survive website redesigns.

| Category | Sites |
|----------|-------|
| 🛒 E-Commerce | Amazon, eBay, Shopify |
| 📱 Social Media | Reddit, Twitter/X, Instagram, ProductHunt, Hacker News |
| 🏢 Business Data | Yelp, Google Maps, Trustpilot, Glassdoor, G2 |
| 💼 Jobs | LinkedIn, Indeed |
| 🏠 Real Estate | Zillow |
| 💻 Developer | GitHub, Stack Overflow |
| 📄 Content | Wikipedia, Medium, YouTube |
| 💰 Finance | CoinMarketCap, Crunchbase |

See the **[full recipe catalog](https://noxx777-lab.github.io/scrapling-cookbook/#recipes)** for details on every recipe.

## 🔧 Usage

Every recipe follows the same interface: `url` in, structured `dict` out.

```python
# YouTube video details
from recipes.youtube_video import scrape_youtube_video
data = scrape_youtube_video("https://youtube.com/watch?v=dQw4w9WgXcQ")
print(f"{data['title']} — {data['views']} views")

# Reddit posts from any subreddit
from recipes.reddit_posts import scrape_reddit_posts
data = scrape_reddit_posts("https://reddit.com/r/Python/hot")
for post in data["posts"]:
    print(f"{post['score']} ↑ {post['title']}")

# LinkedIn public profile
from recipes.linkedin_profile import scrape_linkedin_profile
data = scrape_linkedin_profile("https://linkedin.com/in/username")
print(data["name"], "-", data["headline"])
```

## 📋 Requirements

- Python 3.10+
- [Scrapling](https://github.com/nousresearch/hermes-agent) (`pip install scrapling`)
- [Playwright](https://playwright.dev) (`playwright install`)

## 💰 Pricing

**€19 one-time** — lifetime access, all 23 recipes + future additions.

[**Buy Now**](https://github.com/noxx777-lab/scrapling-cookbook) — Crypto & Stripe payments coming soon.

## 🌐 Landing Page

See the full marketing site: **[scrapling-cookbook.noxx777.dev](https://noxx777-lab.github.io/scrapling-cookbook/)**

## 📁 Project Structure

```
scrapling-cookbook/
├── recipes/           # 23 single-file scraping recipes
│   ├── amazon_product.py
│   ├── twitter_profile.py
│   └── ...
├── docs/
│   └── index.html     # Marketing landing page
└── README.md
```

## 🤝 Contributing

Found a broken selector? Open an issue or PR. Every recipe is maintained and updated as sites change.

## 📜 License

MIT — use freely in your projects. Attribution appreciated but not required.

---

**Built by a developer tired of writing the same selectors for the 23rd time.**
