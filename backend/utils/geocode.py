# utils/geocode.py

from geopy.geocoders import Nominatim
from typing import Tuple

def get_lat_long(location: str) -> Tuple[float, float]:
    """Converts city/state/country string into (latitude, longitude) using OpenStreetMap."""
    geolocator = Nominatim(user_agent="relationship-ledger")
    loc = geolocator.geocode(location)
    
    if loc:
        return (loc.latitude, loc.longitude)
    else:
        raise ValueError(f"Could not find coordinates for: {location}")
