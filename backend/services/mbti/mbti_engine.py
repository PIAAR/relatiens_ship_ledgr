# services/mbti/mbti_engine.py

from mbti import MBTI

def score_mbti_quiz(answers: dict) -> str:
    """ Map answers to E/I, S/N, T/F, J/P counts and return MBTI type """
    return answers["E/I"] + answers["S/N"] + answers["T/F"] + answers["J/P"]

def analyze_mbti_type(mbti_type: str) -> dict:
    mbti_obj = MBTI(mbti_type)
    return {
        "type": mbti_type,
        "cognitive_functions": mbti_obj.functions,
        "trait_tags": list(mbti_obj.dichotomies.values()),
        "summary": f"{mbti_obj} is known for {mbti_obj.short_description}."
    }
