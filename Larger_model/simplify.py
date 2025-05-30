# Larger_model/simplify.py

import PyPDF2
import re
import subprocess
import tempfile

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_abstract(text):
    match = re.search(r"(?i)abstract\s*(.*?)(?=\n[A-Z][A-Z\s]+\n)", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return text[:1000]

def extract_last_assistant_response(output_text: str) -> str:
    parts = output_text.split("<|assistant|>")
    if len(parts) > 1:
        response = parts[-1]
    else:
        response = output_text
    return response.replace("[end of text]", "").strip()

def simplify_abstract(abstract, model_path):
    prompt = f"""<|system|>
You simplify research abstracts into plain English.
<|user|>
Simplify this abstract:
\"\"\"{abstract.strip()}\"\"\"
<|assistant|>
"""

    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as f:
        f.write(prompt)
        f.flush()

        result = subprocess.run(
            [
                "./llama.cpp/build/bin/llama-cli",
                "-m", model_path,
                "-f", f.name,
                "--n-predict", "512",
                "--temp", "0.7"
            ],
            capture_output=True,
            text=True
        )
        return result.stdout

pdf_path = "Academic_Papers/Attention_is_all_you_need.pdf"
model_path = "models/mistral-7b-instruct-v0.1.Q4_K_M.gguf"

text = extract_text_from_pdf(pdf_path)
abstract = extract_abstract(text)
simplified = simplify_abstract(abstract, model_path)
cleaned_output = extract_last_assistant_response(simplified)

print("📝 Simplified Abstract:\n", cleaned_output)

# Optional: Save output (commented out)
# with open("outputs/simplified_abstract.txt", "w") as f:
#     f.write(cleaned_output)