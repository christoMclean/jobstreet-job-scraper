thonpython
import logging
from datetime import datetime
from typing import List, Dict
from .utils_normalization import normalize_text

class JobStreetParser:
    def __init__(self, max_items: int = 20, include_description_html: bool = False):
        self.max_items = max_items
        self.include_description_html = include_description_html

    def scrape(self, url: str) -> List[Dict]:
        # This is a simulated scraper (no live requests).
        results = []
        for i in range(self.max_items):
            job = {
                "jobSearchUrl": url,
                "jobId": f"FAKE-{i}",
                "title": f"Sample Job {i}",
                "company": {
                    "name": "Sample Corp",
                    "id": f"CMP-{i}",
                    "description": "A sample company",
                    "logo": None
                },
                "salary": "",
                "location": "Sample City",
                "country": url.split("//")[1].split(".")[0].upper(),
                "workTypes": ["Full time"],
                "workArrangement": "Hybrid",
                "description": f"Description for job {i}",
                "bulletPoints": ["Requirement 1", "Requirement 2"],
                "classifications": [
                    {"main": "Engineering", "sub": "Software Development"}
                ],
                "postDate": datetime.utcnow().isoformat() + "Z",
                "postDateDisplay": "Just now",
                "sourceUrl": url,
                "scrapedAt": datetime.utcnow().isoformat() + "Z",
                "jobDescriptionHtml": "<div>Example description</div>" if self.include_description_html else None
            }
            # Normalize text fields
            job["title"] = normalize_text(job["title"])
            results.append(job)

        return results