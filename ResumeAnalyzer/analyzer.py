```python
import spacy
nlp = spacy.load("en_core_web_sm")

def analyze_resume(text):
    doc = nlp(text)
    keywords = ["Python", "cybersecurity", "cloud", "AI", "data science"]
    score = sum(1 for token in doc if token.text in keywords)
    feedback = f"Resume has {score} relevant keywords. Consider adding more."
    return feedback

with open("sample_resume.txt") as file:
    resume_text = file.read()
    print(analyze_resume(resume_text))
```
