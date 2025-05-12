from services.zodiac.immanuel_engine import ImmanuelEngine

def test_immanuel_engine_skyfield_output():
    engine = ImmanuelEngine(
        birth_date="1977-05-05",
        birth_time="05:45",
        latitude=38.623,    # Cahokia, IL
        longitude=-90.15
    )

    objects = engine.get_chart_objects()
    
    assert isinstance(objects, dict), "Planetary object result should be a dict"
    assert "Sun" in objects, "Sun data missing"
    assert "RA" in objects["Sun"], "Sun RA missing"
    assert isinstance(objects["Sun"]["RA"], float), "RA should be float"
    assert objects["Sun"]["RA"] > 0, "RA should be positive"

    print("✅ Skyfield-based chart data test passed.")
