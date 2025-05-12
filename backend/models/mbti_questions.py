# question_bank.py

from .models import MBTIQuestion

# Define once, could be moved to JSON later
QUESTION_SETS = {
    4: [MBTIQuestion(id=1, text="...", dichotomy="E/I", polarity="E"), ...],
    8: [...],
    40: [...]
}

def get_questions(version: int = 4) -> list[MBTIQuestion]:
    return QUESTION_SETS.get(version, QUESTION_SETS[4])
