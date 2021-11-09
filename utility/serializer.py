import json
from typing import Dict


def serialize_json_to_dict(json_data: str) -> Dict:
    return json.loads(json_data)
