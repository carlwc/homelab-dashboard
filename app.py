import json
import os
import feedparser
from flask import Flask, render_template

app = Flask(__name__)

CONFIG_FILE = "feeds.json"


def load_feed_config():
    """Loads the feed configurations from the local JSON file."""
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


def fetch_headlines(feed_url, limit=4):
    """Fetches and parses headlines from an RSS feed source."""
    try:
        feed = feedparser.parse(feed_url)
        parsed_entries = []
        for entry in feed.entries[:limit]:
            parsed_entries.append(
                {
                    "title": entry.get("title", "No Title Available"),
                    "link": entry.get("link", "#"),
                    "published": entry.get("published", "Recently"),
                }
            )
        return parsed_entries
    except Exception as e:
        print(f"Error parsing feed {feed_url}: {e}")
        return [
            {
                "title": "Failed to load live headlines.",
                "link": "#",
                "published": "Error",
            }
        ]


@app.route("/")
def index():
    feed_config = load_feed_config()
    active_feeds = []

    # Loop through the JSON config and parse feeds that are marked 'enabled'
    for feed_key, config in feed_config.items():
        if config.get("enabled", False):
            headlines = fetch_headlines(config["url"])
            active_feeds.append(
                {
                    "title": config["title"],
                    "icon": config["icon"],
                    "headlines": headlines,
                }
            )

    return render_template("index.html", active_feeds=active_feeds)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)