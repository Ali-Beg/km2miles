from km2miles import km_to_miles

def test_km_to_miles():
    assert km_to_miles(1) == 0.621371
    assert km_to_miles(10) == 6.21371
    assert km_to_miles(0) == 0
    assert round(km_to_miles(5), 6) == 3.106855
    assert round(km_to_miles(100), 6) == 62.1371
