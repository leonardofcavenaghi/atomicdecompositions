"""Index scientific catalogue keywords without displaying metadata paragraphs."""
import json
from pathlib import Path
from mkdocs.plugins import event_priority


@event_priority(-100)
def on_post_build(config):
    path = Path(config.site_dir) / "search/search_index.json"
    index = json.loads(path.read_text())
    records = json.loads((Path(config.docs_dir) / "data/catalog-records.json").read_text())["records"]
    by_location = {doc["location"]: doc for doc in index["docs"]}
    for record in records:
        if not record["link"].startswith("records/"):
            continue
        location = "catalog/" + record["link"].replace(".md", "/")
        doc = by_location[location]
        keywords = " · ".join(record["keywords"])
        doc["text"] += " " + keywords
    path.write_text(json.dumps(index, ensure_ascii=False, separators=(",", ":")))
