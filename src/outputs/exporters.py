thonpython
import json
from pathlib import Path

class JsonExporter:
    @staticmethod
    def export_json(data, path: str):
        output_path = Path(path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)