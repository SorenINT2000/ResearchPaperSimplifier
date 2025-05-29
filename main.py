from pypdf import PdfReader
from transformers import pipeline, AutoTokenizer
import re
from datasets import Dataset
import torch

def chunk_text(text, tokenizer, max_length=1024):
    # Split text into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    current_chunk = []
    current_length = 0
    
    for sentence in sentences:
        # Get actual token count for the sentence
        sentence_tokens = len(tokenizer.encode(sentence))
        
        if current_length + sentence_tokens > max_length:
            if current_chunk:  # Only add if we have content
                chunks.append(' '.join(current_chunk))
            current_chunk = [sentence]
            current_length = sentence_tokens
        else:
            current_chunk.append(sentence)
            current_length += sentence_tokens
    
    if current_chunk:  # Add the last chunk if it exists
        chunks.append(' '.join(current_chunk))
    
    return chunks

# Read PDF
reader = PdfReader("input/test.pdf")
print(f"Number of pages: {len(reader.pages)}")

# Extract text from all pages
page_texts = [page.extract_text() for page in reader.pages[1:]]
text = "\n".join(page_texts)

# Initialize the model and tokenizer
model_name = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(model_name)
summarizer = pipeline("summarization", model=model_name, device='cuda')

# Split text into manageable chunks
chunks = chunk_text(text, tokenizer)
print(f"Split text into {len(chunks)} chunks")

# Filter chunks that are too short
valid_chunks = [chunk for chunk in chunks if len(chunk.split()) > 30]
print(f"Found {len(valid_chunks)} valid chunks to process")

# Create a dataset for efficient processing
dataset = Dataset.from_dict({"text": valid_chunks})

# Process chunks in batches
summaries = []
batch_size = 4  # Adjust based on your GPU memory

for i in range(0, len(valid_chunks), batch_size):
    batch = valid_chunks[i:i + batch_size]
    print(f"Processing batch {i//batch_size + 1}/{(len(valid_chunks) + batch_size - 1)//batch_size}")
    
    try:
        # Process the batch
        results = summarizer(batch, 
                           max_length=130,
                           min_length=30,
                           do_sample=False,
                           truncation=True)
        
        # Extract summaries from results
        batch_summaries = [result['summary_text'] for result in results]
        summaries.extend(batch_summaries)
        
    except Exception as e:
        print(f"Error processing batch {i//batch_size + 1}: {str(e)}")
        continue

# Combine summaries
final_summary = " ".join(summaries)
print("\nFinal Summary:")
print(final_summary)