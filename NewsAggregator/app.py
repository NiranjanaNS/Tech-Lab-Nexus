```python
from flask import Flask, render_template
import feedparser

app = Flask(__name__)
feeds = {
    "AI": "https://example.com/ai-news-rss",
    "Cybersecurity": "https://example.com/cybersecurity-news-rss"
}

def fetch_news(category):
    feed = feedparser.parse(feeds.get(category, ""))
    return feed['entries'][:5] if 'entries' in feed else []

@app.route('/news/<category>')
def news(category):
    articles = fetch_news(category)
    return render_template('news.html', category=category, articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
```
