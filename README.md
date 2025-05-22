
# 🧠 Python Code Quality Analyzer & Auto Fixer

This is a Streamlit web application that performs comprehensive static and AI-powered analysis of Python code. It detects complexity, pylint issues, readability, bug predictions, and even suggests or applies AI-based improvements.

## 🚀 Features

- 📎 Upload any `.py` file for analysis
- 🔍 Static Analysis (Cyclomatic Complexity + Pylint issues)
- 📊 Visual complexity plot per function
- 🤖 AI-powered bug prediction
- 📏 Readability & maintainability scoring
- 💡 Suggestions for improving bad code patterns
- 📌 Ranking of issues by impact
- 🛠️ One-click AI fix suggestions and code generation

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – for web app
- [Plotly](https://plotly.com/python/) – for data visualization
- `pylint`, `radon` – for static analysis
- OpenAI or HuggingFace – for AI-powered analysis (via custom modules)
- Python 3.8+

## 📂 Project Structure

```
.
├── app.py
├── analyzer/
│   ├── ai_analyzer.py
│   ├── static_analyzer.py
│   ├── suggester.py
│   └── ranker.py
└── README.md
```

## 🔧 Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/python-code-analyzer.git
   cd python-code-analyzer
   ```

2. **(Optional) Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**:
   ```bash
   streamlit run app.py
   ```

## 📦 `requirements.txt`

```
streamlit
plotly
pylint
radon
openai  # or huggingface_hub, depending on your AI module
```

> 🔐 **Note**: Make sure to set up your OpenAI or HuggingFace API keys as environment variables if your `ai_analyzer.py` uses external APIs.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Made with ❤️ using Streamlit and Python.
