# services/zodiac.py

from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib import const

from typing import Dict, Any
import json

# Example trait dictionary (to be expanded into a traits DB)
TRAIT_KEYWORDS = {
    'Sun': {
        'TAU': ['Stable', 'Grounded', 'Pleasure-seeking'],
        'ARI': ['Assertive', 'Bold', 'Impulsive']
    },
    'Moon': {
        'TAU': ['Emotionally steady', 'Comfort-seeking'],
        'ARI': ['Quick-reacting', 'Passionate']
    },
    'Asc': {
        'TAU': ['Approachable', 'Patient'],
        'ARI': ['Energetic', 'Direct']
    },
    # Add Venus, Mars, etc.
}


def load_natal_chart(birth_date: str, birth_time: str, location: str, latitude: float, longitude: float) -> Chart:
    """Load a natal chart using flatlib."""
    dt = Datetime(birth_date, birth_time, '+00:00')  # Adjust timezone handling later
    pos = GeoPos(latitude, longitude)
    chart = Chart(dt, pos)
    return chart


def extract_traits(chart: Chart) -> Dict[str, Any]:
    """Extract traits from key planetary positions."""
    core_traits = []
    planetary_positions = {}

    for key in [const.SUN, const.MOON, const.ASC, const.VENUS, const.MARS]:
        obj = chart.get(key)
        sign = obj.sign
        planetary_positions[key] = sign

        keywords = TRAIT_KEYWORDS.get(key, {}).get(sign, [])
        core_traits.extend(keywords)

    return {
        "core_traits": list(set(core_traits)),
        "planetary_positions": planetary_positions
    }


def generate_summary(traits: Dict[str, Any]) -> str:
    """Create an NLP-style summary from traits."""
    summary = (
        f"Your chart reveals you're driven by qualities like {', '.join(traits['core_traits'][:3])}... "
        "These reflect how you show up in relationships and respond emotionally. "
        "Your core planetary alignments suggest a relational style that's both unique and potent."
    )
    return summary


def get_zodiac_report(birth_date: str, birth_time: str, location: str, latitude: float, longitude: float) -> Dict[str, Any]:
    """Full report generation pipeline."""
    chart = load_natal_chart(birth_date, birth_time, location, latitude, longitude)
    traits = extract_traits(chart)
    summary = generate_summary(traits)

    # Optional: calculate element distribution, 7th house analysis here

    return {
        "core_traits": traits["core_traits"],
        "zodiac_summary": summary,
        "planetary_positions": traits["planetary_positions"],
        "location": location,
        "birth_date": birth_date,
        "birth_time": birth_time
    }
