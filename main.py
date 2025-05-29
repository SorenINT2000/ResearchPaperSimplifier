from pypdf import PdfReader
reader = PdfReader("input/test.pdf")

# printing number of pages in pdf file
print(len(reader.pages))

# getting a specific page from the pdf file
page_texts = [page.extract_text() for page in reader.pages[1:]]

# extracting text from page
text = "\n".join(page_texts)
print(text)

# With pipeline, just specify the task and the model id from the Hub.
from transformers import pipeline
pipe = pipeline("summarization", model="facebook/bart-large-cnn")

# Prompt the model and print the response
response = pipe(text)  # Generate one response
print(response)