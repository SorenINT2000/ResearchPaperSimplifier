# Research Paper Simplifier

What I did for setup:

1. `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
2. Close + restart IDE
3. `uv init ../ResearchPaperSimplifier`
4. `uv python install 3.11.9`
5. change python versions in `.python-version` & `pyproject.toml` to 3.11.9
6. `uv venv`
7. `uv pip install "transformers[torch]"`
8. `uv pip install "pypdf"`
9. `uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121`
10. `uv pip install datasets`

To run program:
`./.venv\Scripts\activate` to activate environment
`deactivate` to deactivate environment
`uv run main.py` to run program
