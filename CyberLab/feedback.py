from transformers import pipeline

# Load a sentiment-analysis model for feedback on user attempts
feedback_model = pipeline("sentiment-analysis")

def get_feedback(attempt):
    result = feedback_model(attempt)[0]
    feedback = "Positive feedback!" if result["label"] == "POSITIVE" else "Needs improvement."
    print(f"Feedback on your attempt: {feedback}")

# Example attempt for testing feedback
attempt = "I tried using SQL injection with ' OR '1'='1' --"
get_feedback(attempt)
