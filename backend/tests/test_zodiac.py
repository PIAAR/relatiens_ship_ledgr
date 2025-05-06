# tests/test_zodiac.py

import pytest
from services.zodiac.zodiac import Zodiac
from utils.geocode import get_lat_long


@pytest.fixture(scope="module")
def birth_data():
    lat, lon = get_lat_long("St. Louis, MO")
    return {
        "birth_date": "1977-05-05",
        "birth_time": "05:45",
        "location": "St. Louis, MO",
        "latitude": lat,
        "longitude": lon,
    }

@pytest.fixture(scope="module")
def zodiac_instance(birth_data):
    return Zodiac(
        birth_date=birth_data["birth_date"],
        birth_time=birth_data["birth_time"],
        location=birth_data["location"],
        latitude=birth_data["latitude"],
        longitude=birth_data["longitude"]
    )

def test_zodiac_report_structure(zodiac_instance):
    report = zodiac_instance.get_report()
    expected_keys = {
        "birth_date", "birth_time", "location",
        "core_traits", "zodiac_summary",
        "planetary_positions", "houses", "aspects"
    }
    assert isinstance(report, dict)
    assert expected_keys.issubset(set(report.keys())), "Report missing expected keys"

def test_core_traits_format(zodiac_instance):
    traits_section = zodiac_instance.traits.get("core_traits", {})
    for key in ["sun", "moon", "asc"]:
        assert key in traits_section, f"{key} not found in core_traits"
        assert isinstance(traits_section[key], dict), f"{key} traits should be a dict"
        assert isinstance(traits_section[key].get("traits", []), list), f"{key} traits missing"
        assert all(isinstance(t, str) for t in traits_section[key]["traits"]), f"{key} traits should be strings"

def test_summary_text(zodiac_instance):
    summary = zodiac_instance.summary
    assert isinstance(summary, str)
    assert "Sun in" in summary, "Expected 'Sun in ...' format in summary"
    assert "Moon in" in summary
    assert "Rising in" in summary

def test_planetary_positions_valid(zodiac_instance):
    report = zodiac_instance.get_report()
    planets = report["planetary_positions"]
    assert isinstance(planets, dict)
    for planet, sign in planets.items():
        assert isinstance(planet, str)
        assert isinstance(sign, str)
        assert sign != "Unknown", f"{planet} sign should not be Unknown"

def test_all_trait_objects_present(zodiac_instance):
    object_names = [
        "sun", "moon", "asc", "desc", "mc", "ic",
        "mercury", "venus", "mars", "jupiter", "saturn",
        "uranus", "neptune", "pluto", "chiron",
        "true north node", "true south node",
        "true lilith", "part of fortune", "vertex"
    ]
    
    traits = zodiac_instance.traits.get("core_traits", {})
    
    for name in object_names:
        assert name in traits, f"Missing {name} in core_traits"
        assert "sign" in traits[name], f"{name} missing 'sign'"
        assert isinstance(traits[name]["traits"], list), f"{name} traits should be a list"
        assert all(isinstance(t, str) for t in traits[name]["traits"]), f"{name} traits should be strings"

def test_house_structure_and_content(zodiac_instance):
    report = zodiac_instance.get_report()
    houses = report.get("houses")

    assert isinstance(houses, dict), "Expected 'houses' to be a dict"

    for house_id, obj in houses.items():
        # Make sure we have the correct object type
        assert hasattr(obj, "sign"), f"House {house_id} is missing 'sign' attribute"
        assert hasattr(obj.sign, "name") or hasattr(obj.sign, "abbr"), f"House {house_id} has invalid sign format"

        # Get the sign name or abbreviation
        sign_name = getattr(obj.sign, "name", None) or getattr(obj.sign, "abbr", None)

        assert isinstance(sign_name, str), f"House {house_id} sign is not a string"
        assert sign_name.strip() != "", f"House {house_id} has an empty sign"
        assert sign_name != "Unknown", f"House {house_id} has an Unknown sign"

def test_aspects_structure(zodiac_instance):
    report = zodiac_instance.get_report()
    aspects = report.get("aspects", {})

    assert isinstance(aspects, dict), "Aspects should be a dictionary"

    for source_id, targets in aspects.items():
        assert isinstance(targets, dict), f"Expected nested dict for {source_id}"
        for target_id, aspect in targets.items():
            assert isinstance(aspect, dict), f"Aspect from {source_id} to {target_id} should be a dict"
            for key in ["active", "passive", "aspect", "orb", "distance", "difference", "movement", "condition"]:
                assert key in aspect, f"Missing key '{key}' in aspect from {source_id} to {target_id}"

            # Check expected types for numeric values
            assert isinstance(aspect["aspect"], (int, float)), "'aspect' must be a number"
            assert isinstance(aspect["orb"], (int, float)), "'orb' must be a number"
            assert isinstance(aspect["distance"], (int, float)), "'distance' must be a number"

def test_flat_aspects_summary(zodiac_instance):
    report = zodiac_instance.get_report()
    flat_aspects = report.get("flat_aspects", [])
    assert isinstance(flat_aspects, list)
    for aspect in flat_aspects:
        assert "from" in aspect
        assert "to" in aspect
        assert "type" in aspect
        assert "degree" in aspect or "orb" in aspect

