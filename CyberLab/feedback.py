```python
from textblob import TextBlob

def get_feedback(attempt):
    blob = TextBlob(attempt)
    sentiment = blob.sentiment.polarity
    feedback = "Good attempt!" if sentiment > 0 else "Could use improvement."
    print(f"Feedback on your attempt: {feedback}")

attempt = "I tried SQL injection with ' OR '1'='1' --"
get_feedback(attempt)
```
