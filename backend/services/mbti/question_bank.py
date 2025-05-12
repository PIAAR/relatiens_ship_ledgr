# services/mbti/question_bank.py

from models.mbti_types import MBTIQuestion

QUESTION_SETS = {
    4: [
        MBTIQuestion(id=1, text="Do you enjoy social gatherings?", dichotomy="E/I", polarity="E"),
        MBTIQuestion(id=2, text="Do you rely on facts over ideas?", dichotomy="S/N", polarity="S"),
        MBTIQuestion(id=3, text="Do you make decisions logically?", dichotomy="T/F", polarity="T"),
        MBTIQuestion(id=4, text="Do you prefer structured planning?", dichotomy="J/P", polarity="J"),
    ],
    8: [
        # Add 2 per dichotomy
    ],
    40: [
        # Populate later with real psychometric set
    ]
}

def get_questions(version: int = 4) -> list[MBTIQuestion]:
    return QUESTION_SETS.get(version, QUESTION_SETS[4])
