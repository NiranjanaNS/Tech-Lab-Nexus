import spacy
nlp = spacy.load("en_core_web_sm")

def analyze_resume(text):
    doc = nlp(text)
    keywords = ["Python", "cybersecurity", "cloud", "AI", "data science"]
    score = sum(1 for token in doc if token.text in keywords)
    feedback = f"Resume has {score} relevant keywords. Consider adding more if needed."
    word_count = len(doc)
    feedback += "\nYour resume may need more detail." if word_count < 300 else "\nNice word count!"
    return feedback

# Load sample resume text
resume_text = open("sample_resume.txt").read()
print(analyze_resume(resume_text))
