# Larger_model/download_model.py

from huggingface_hub import hf_hub_download

path = hf_hub_download(
    repo_id="TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
    filename="mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    local_dir="models",
    resume_download=True,
)
print(f"✅ Model downloaded to: {path}")