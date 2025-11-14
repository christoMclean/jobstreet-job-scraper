thonpython
import json
import logging
from pathlib import Path
from extractors.jobstreet_parser import JobStreetParser
from outputs.exporters import JsonExporter

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

def load_input(input_path: str):
    with open(input_path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    input_path = "data/input.example.json"
    output_path = "data/sample_output.json"

    logging.info(f"Loading input configuration: {input_path}")
    config = load_input(input_path)

    parser = JobStreetParser(
        max_items=config.get("maxItems", 20),
        include_description_html=config.get("includeDescriptionHtml", False)
    )

    results = []
    for url in config.get("searchUrls", []):
        logging.info(f"Processing URL: {url}")
        results.extend(parser.scrape(url))

    logging.info(f"Collected {len(results)} results")
    JsonExporter.export_json(results, output_path)
    logging.info(f"Saved output to {output_path}")

if __name__ == "__main__":
    main()