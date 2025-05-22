import os
import openai

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_code_with_ai(code: str) -> str:
    """
    Uses AI to analyze the code for bugs, maintainability issues, and general suggestions.
    """
    prompt = (
        "Analyze the following Python code. Identify any bugs, code smells, "
        "poor practices, and maintainability concerns. Suggest ways to improve:\n\n"
        + code
    )
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
        max_tokens=500,
    )
    return response.choices[0].message.content.strip()

def fix_code_with_ai(code: str, user_request: str) -> str:
    """
    Applies AI-powered improvements to code based on a specific user request.
    Returns only the improved code without explanation.
    """
    prompt = (
        "Here is some Python code:\n\n"
        + code
        + "\n\nPlease improve or fix the code based on the following instruction:\n"
        + user_request
        + "\n\nReturn only the improved code without any explanation or formatting."
    )
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
        max_tokens=1000,
    )
    return response.choices[0].message.content.strip()

def get_readability_score(code: str) -> str:
    """
    Gets a readability and maintainability score (1-10) with explanation.
    """
    prompt = (
        "Rate the following Python code from 1 to 10 in terms of readability and maintainability, "
        "where 1 is poor and 10 is excellent. Then briefly explain your reasoning:\n\n" + code
    )
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
        max_tokens=150,
    )
    return response.choices[0].message.content.strip()
