# services/mbti/analyzer.py

def cognitive_stack(mbti_type: str) -> list[str]:
    stacks = {
        "ENTJ": ["Te", "Ni", "Se", "Fi"],
        "INTP": ["Ti", "Ne", "Si", "Fe"],
        "INFJ": ["Ni", "Fe", "Ti", "Se"],
        "ISFP": ["Fi", "Se", "Ni", "Te"],
        # Add more types as needed
    }
    return stacks.get(mbti_type, [])

def get_summary(mbti_type: str) -> str:
    summaries = {
        "ENTJ": "Commanding and strategic leaders who love efficiency.",
        "INFJ": "Insightful, reserved idealists focused on harmony and vision.",
        "ISFP": "Gentle artists who lead with empathy and grounded presence.",
        # Add more types as needed
    }
    return summaries.get(mbti_type, "No summary available.")
