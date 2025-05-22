import sys
import os
import streamlit as st
import plotly.express as px

# Add current script directory to sys.path so you can import local modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from analyzer.static_analyzer import get_complexity, get_pylint_issues, get_complexity_per_function
from analyzer.ai_analyzer import analyze_code_with_ai, get_readability_score, fix_code_with_ai
from analyzer.suggester import generate_suggestion
from analyzer.ranker import rank_issues

def plot_complexity(complexities, title="Code Complexity per Function"):
    names = [c['name'] for c in complexities]
    values = [c['complexity'] for c in complexities]
    fig = px.bar(
        x=names, y=values,
        labels={'x': 'Function/Block', 'y': 'Cyclomatic Complexity'},
        title=title
    )
    return fig

st.title("🧠 Python Code Quality Analyzer & Auto Fixer")

uploaded_file = st.file_uploader("📎 Upload a Python file", type="py")
if uploaded_file:
    filepath = f"temp_{uploaded_file.name}"
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getvalue())

    code = uploaded_file.getvalue().decode()

    # Static Analysis
    st.subheader("🔍 Static Analysis")
    complexity = get_complexity(filepath)
    lint_issues = get_pylint_issues(filepath)
    st.json({"Complexity Summary": complexity})
    st.text("Pylint Output:")
    st.text("\n".join(lint_issues))

    # Visualize Complexity
    st.subheader("📊 Complexity Visualization")
    complexities_per_func = get_complexity_per_function(filepath)
    fig = plot_complexity(complexities_per_func)
    st.plotly_chart(fig)

    # AI Bug Prediction
    st.subheader("🤖 AI Bug & Issue Prediction")
    ai_predictions = analyze_code_with_ai(code)
    st.markdown(ai_predictions)

    # Readability Score
    st.subheader("📏 Readability & Maintainability Score")
    readability_score = get_readability_score(code)
    st.markdown(readability_score)

    # Suggestions
    st.subheader("💡 Suggestions for Improvement")
    suggestion = generate_suggestion(code[:300], "complex function or style issue")
    st.markdown(suggestion)

    # Issue Ranking — moved up
    st.subheader("📌 Ranked Issues")
    issues = [{"type": "complexity", "desc": str(c)} for c in complexity]
    issues += [{"type": "lint", "desc": l} for l in lint_issues if l]
    issues += [{"type": "bug", "desc": str(ai_predictions)}]
    ranked = rank_issues(issues)
    st.json(ranked)

    # User Request for Fix
    st.subheader("🛠️ Improve Your Code via AI")
    user_request = st.text_input("Describe what you want to improve or fix:")
    if user_request:
        fixed_code = fix_code_with_ai(code, user_request)
        st.subheader("✅ AI-Generated Improved Code")
        st.code(fixed_code, language="python")

    # Clean up
    os.remove(filepath)
