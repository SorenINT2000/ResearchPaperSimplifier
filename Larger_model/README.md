# 🔬 ResearchPaperSimplifier (Larger Model Edition)

This project simplifies complex research paper abstracts into plain English using a **quantized Mistral 7B model** powered by `llama.cpp`. It reads PDF files, extracts the abstract, and passes it through a local LLM using a prompt to generate an easy-to-understand version.

---

## 📁 Project Structure

>**Larger_model**  
>├── **Academic_Papers**  		 <sub># 📚 Input PDFs to be simplified</sub>  
>├── **models**                  <sub># 🧠 Quantized .gguf models (ignored in git)</sub>  
>├── **outputs**                 <sub># 📝 Simplified output files (ignored in git)</sub>  
>├── **llama.cpp**               <sub># 🔧 Local LLM inference backend (submodule or local build)</sub>  
>├── **simplify.py**             <sub># 🎯 Main script: read PDF, extract abstract, simplify</sub>  
>├── **download_model.py**       <sub># 🔽 Script to download GGUF model from Hugging Face</sub>  
>├── **requirements.txt**        <sub># 📦 Python dependencies</sub>  
>├── **README.md**              <sub># 📖 You’re reading it!</sub>  
>└── **.gitignore**              <sub># 🚫 Git ignore rules</sub>  

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ResearchPaperSimplifier.git
cd ResearchPaperSimplifier/Larger_model
```
### Setup Pyhton envt

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Build llama.cpp

```
cd llama.cpp
mkdir build && cd build
cmake ..
make -j
cd ../..
```

### Download the model

```
python download_model.py
```

Or manually download from:

🔗 https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF

Place the .gguf file inside the models/directory.

### Run the simplifier

Add your PDF to Academic_Papers/, then:
```
python simplify.py
```

Output will be printed in the terminal. You can optionally save it to the outputs/ folder by uncommenting the write line at the bottom of simplify.py.

### Prompt Template

```
<|system|>
You simplify research abstracts into plain English.
<|user|>
Simplify this abstract:
"""<ABSTRACT>"""
<|assistant|>
```

### Example Output

📝 Simplified Abstract:
The Transformer is a new model for translating text. It uses attention instead of older methods and is faster and more accurate than previous models...

### 📌 Requirements
	•	Python 3.8+
	•	llama.cpp compiled locally
	•	PyPDF2, huggingface_hub (see requirements.txt)

### 🚫 .gguf Model Disclaimer

Due to file size restrictions, the GGUF model weights are not included in this repository. Please download them from Hugging Face.