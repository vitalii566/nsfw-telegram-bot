import json
import os
import filetype

def find_best_match(query):
    with open("scene_db.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        if query.lower() in item["description"].lower():
            image_path = item["image_path"]
            if os.path.exists(image_path) and filetype.is_image(image_path):
                return image_path
    return None
