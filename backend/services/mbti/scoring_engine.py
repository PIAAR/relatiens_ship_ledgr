# services/mbti/scoring_engine.py

from collections import defaultdict
from models.mbti_types import MBTIQuestion

def score_mbti(questions: list[MBTIQuestion], answers: list[bool]) -> str:
    tally = defaultdict(float)

    for q, answer in zip(questions, answers):
        if answer:
            tally[q.polarity] += q.weight
        else:
            opposite = get_opposite_polarity(q.polarity)
            tally[opposite] += q.weight

    return "".join([
        "E" if tally["E"] >= tally["I"] else "I",
        "S" if tally["S"] >= tally["N"] else "N",
        "T" if tally["T"] >= tally["F"] else "F",
        "J" if tally["J"] >= tally["P"] else "P",
    ])

def get_opposite_polarity(p: str) -> str:
    opposites = {"E": "I", "I": "E", "S": "N", "N": "S", "T": "F", "F": "T", "J": "P", "P": "J"}
    return opposites[p]
