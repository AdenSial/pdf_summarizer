from pdf_reader import extract_text_from_pdf
from utils import clean_text
from summarizer import summarize


pdf_path = "sample.pdf"

print("Reading PDF...")

text = extract_text_from_pdf(pdf_path)

print("Cleaning text...")

cleaned_text = clean_text(text)

with open("extracted_text.txt", "w", encoding="utf-8") as file:
    file.write(cleaned_text)

print("Generating summary...")

summary = summarize(cleaned_text)

print("\n========== SUMMARY ==========\n")

print(summary)
