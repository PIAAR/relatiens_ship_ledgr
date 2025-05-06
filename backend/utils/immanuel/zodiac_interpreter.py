import json
from pathlib import Path

class ZodiacInterpreter:
    def __init__(self):
        self.project_root = Path(__file__).resolve().parents[2]
        self.traits_path = self.project_root  / "data" / "traits.json"
        self.name_map_path = self.project_root / "utils" / "immanuel" / "object_name_map.json"
        self.traits = self._load_json(self.traits_path)
        self.name_map = self._load_json(self.name_map_path)

    def _load_json(self, path: Path) -> dict:
        with open(path, "r") as f:
            return json.load(f)

    def resolve_object_name(self, obj_id: int) -> str:
        return self.name_map.get("id_to_name_map", {}).get(str(obj_id), f"obj_{obj_id}")

    def get_traits_for(self, object_name: str, sign_abbr: str) -> list[str]:
        key = object_name.lower()
        if key in self.traits and sign_abbr in self.traits[key]:
            return self.traits[key][sign_abbr]
        return []

    def get_positions(self, natal_chart_objects: dict) -> dict:
        positions = {}
        for obj_id, obj in natal_chart_objects.items():
            if hasattr(obj, "sign") and hasattr(obj.sign, "name"):
                name = self.resolve_object_name(obj_id)
                positions[name] = obj.sign.name
        return positions

    def interpret_chart(self, natal_chart_objects: dict) -> dict:
        report = {}
        for obj_id, astro_obj in natal_chart_objects.items():
            name = self.resolve_object_name(obj_id).lower()
            if not hasattr(astro_obj, "sign"):
                continue
            sign = astro_obj.sign.name[:3].upper()
            traits = self.get_traits_for(name, sign)
            report[name] = {
                "sign": sign,
                "traits": traits
            }
        return report

    def list_aspect_attributes(self, aspects: dict) -> dict:
        attributes_found = {}
        for source_id, targets in aspects.items():
            for target_id, aspect in targets.items():
                for attr in dir(aspect):
                    if not attr.startswith("_"):
                        attributes_found[attr] = True
        return dict(sorted(attributes_found.items()))

    def summarize_aspects(self, aspects: dict) -> list[dict]:
        summary = []
        for source_id, targets in aspects.items():
            for target_id, aspect in targets.items():
                item = {
                    "from": self.resolve_object_name(source_id),
                    "to": self.resolve_object_name(target_id),
                    "type": getattr(aspect, "type", "Unknown"),
                    "degree": getattr(aspect, "degree", None),
                    "orb": getattr(aspect, "orb", None),
                }
                summary.append(item)
        return summary

    def convert_aspects_to_dict(self, aspects: dict) -> dict:
        return {
            source_id: {
                target_id: {
                    "aspect": getattr(aspect, "aspect", None),
                    "orb": getattr(aspect, "orb", None),
                    "distance": getattr(aspect, "distance", None),
                    "difference": getattr(aspect, "difference", None),
                    "movement": getattr(aspect, "movement", None),
                    "condition": getattr(aspect, "condition", None),
                }
                for target_id, aspect in targets.items()
            }
            for source_id, targets in aspects.items()
        }

    def unwrap_aspects(self, aspects: dict) -> dict:
        def unwrap(value):
            return value.raw if hasattr(value, "raw") else value

        unwrapped = {}
        for source_id, targets in aspects.items():
            target_unwrapped = {}
            for target_id, aspect in targets.items():
                target_unwrapped[target_id] = {
                    "active": unwrap(getattr(aspect, "active", None)),
                    "passive": unwrap(getattr(aspect, "passive", None)),
                    "aspect": unwrap(getattr(aspect, "aspect", None)),
                    "orb": unwrap(getattr(aspect, "orb", None)),
                    "distance": unwrap(getattr(aspect, "distance", None)),
                    "difference": unwrap(getattr(aspect, "difference", None)),
                    "movement": unwrap(getattr(aspect, "movement", None)),
                    "condition": unwrap(getattr(aspect, "condition", None)),
                }
            unwrapped[source_id] = target_unwrapped
        return unwrapped

