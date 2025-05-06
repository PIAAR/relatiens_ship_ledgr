# backend/scripts/generate_object_name_map.py

import json
from datetime import datetime
from immanuel import charts

# Example birth data (use any real data)
birth_data = {
    "date": "1977-05-05",
    "time": "05:45",
    "latitude": 38.6280278,
    "longitude": -90.1910154,
}

def build_object_name_map(birth_data: dict, output_path: str = "./immanuel/object_name_map.json"):
    """Generate a mapping of chart object IDs to human-readable names."""
    subject = charts.Subject(
        date_time=datetime.strptime(f"{birth_data['date']} {birth_data['time']}", "%Y-%m-%d %H:%M"),
        latitude=birth_data["latitude"],
        longitude=birth_data["longitude"]
    )

    natal_chart = charts.Natal(subject)

    name_map = {
        str(key): obj.name.strip().lower()
        for key, obj in natal_chart.objects.items()
    }

    readable_names = sorted(
        {obj.name.strip().lower() for obj in natal_chart.objects.values()}
    )

    output = {
        "id_to_name_map": name_map,
        "available_names": readable_names
    }

    with open(output_path, "w") as f:
        json.dump(output, f, indent=4)

    print(f"[✅] Object name map written to {output_path}")

if __name__ == "__main__":
    build_object_name_map(birth_data)
