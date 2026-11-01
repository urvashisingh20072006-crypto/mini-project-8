import json
from pathlib import Path


class Storage:

    def __init__(self, filename="data.json"):
        self.filename = Path(__file__).parent / filename

    def save_data(self, data):

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

        print("Data saved successfully!")

    def load_data(self):

        if not self.filename.exists():
            return {
                "items": [],
                "members": [],
                "loans": []
            }

        with open(self.filename, "r") as file:
            return json.load(file)