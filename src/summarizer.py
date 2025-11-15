from transformers import pipeline
summarizer = pipeline("summarization", model="t5-small")

def generate_summary(text):
    return summarizer(text, max_length=60, min_length=20, do_sample=False)[0]["summary_text"]
