from services.summary.blending_service import SummaryBlender

def test_blended_summary_class():
    mbti = {
        "type": "ENTJ",
        "summary": "You are a bold, strategic leader who thrives on challenge and efficiency. You value structure, achievement, and taking initiative."
    }

    zodiac = {
        "sun": "Taurus",
        "summary": "Practical and grounded, yet quietly ambitious and expressive."
    }

    hd = {
        "type": "Manifesting Generator",
        "summary": "You thrive by moving quickly toward aligned opportunities while respecting your emotional clarity."
    }

    blender = SummaryBlender(mbti, zodiac, hd)
    result = blender.blend()

    assert result["mbti_type"] == "ENTJ"
    assert result["zodiac_sun"] == "Taurus"
    assert result["human_design_type"] == "Manifesting Generator"
    assert "MBTI Insight" in result["combined_summary"]
    assert "Zodiac Insight" in result["combined_summary"]
    assert "Human Design Insight" in result["combined_summary"]
