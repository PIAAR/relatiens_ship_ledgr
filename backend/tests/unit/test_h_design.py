# tests/unit/test_h_design.py

import pytest
from services.human_design import h_design

class MockEngine:
    def get_chart_data(self):
        return {
            "type": "Generator",
            "authority": "Emotional",
            "profile": "4/6",
            "defined_centers": ["Sacral", "Root"],
            "open_centers": ["Heart", "Head"],
            "gates": [2, 3, 4],
            "channels": ["2-14", "3-60"],
            "summary": "You are a Generator with Emotional authority and a 4/6 profile. Your defined centers are Sacral, Root. Key gates include 2, 3, 4."
        }

@pytest.fixture
def human_design_instance(monkeypatch):
    # Patch the engine with mock
    monkeypatch.setattr(h_design.HumanDesignEngine, "get_chart_data", lambda self: MockEngine().get_chart_data())

    return h_design.HumanDesign(
        birth_date="1990-01-01",
        birth_time="12:00:00",
        location="New York, USA"
    )

def test_human_design_initialization(human_design_instance):
    assert human_design_instance.birth_date == "1990-01-01"
    assert human_design_instance.birth_time == "12:00:00"
    assert human_design_instance.location == "New York, USA"
    assert hasattr(human_design_instance, '_chart_data')
    assert hasattr(human_design_instance, '_type')

def test_human_design_summary(human_design_instance):
    summary = human_design_instance.summary
    assert isinstance(summary, str)
    assert human_design_instance._type in summary
    assert human_design_instance._profile in summary

def test_human_design_report_structure(human_design_instance):
    report = human_design_instance.get_report()
    required_keys = [
        "birth_date", "birth_time", "location",
        "type", "authority", "profile",
        "centers", "gates", "summary"
    ]
    for key in required_keys:
        assert key in report

def test_human_design_centers_and_gates(human_design_instance):
    report = human_design_instance.get_report()
    assert isinstance(report["centers"], list)
    assert isinstance(report["gates"], list)
    assert all(isinstance(center, str) for center in report["centers"])
    assert all(isinstance(gate, int) for gate in report["gates"])  # changed to int to match mock

def test_human_design_lat_long_resolution(monkeypatch):
    monkeypatch.setattr(h_design.HumanDesignEngine, "get_chart_data", lambda self: MockEngine().get_chart_data())

    hd = h_design.HumanDesign(
        birth_date="1990-01-01",
        birth_time="12:00:00",
        location="Los Angeles, USA"
    )
    assert hd.latitude is not None
    assert hd.longitude is not None
