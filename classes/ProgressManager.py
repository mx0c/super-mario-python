import json
import os

class ProgressManager:
    _instance = None

    def _new_(cls):
        if cls._instance is None:
            cls.instance = super(ProgressManager, cls).new_(cls)
            cls._instance.highest_level = "1-1"
            cls._instance.load_progress()
        return cls._instance

    def load_progress(self):
        if os.path.exists("progress.json"):
            with open("progress.json", "r") as f:
                data = json.load(f)
                self.highest_level = data.get("highest_level", "1-1")

    def save_progress(self, level_name):
        if self.is_higher_level(level_name):
            self.highest_level = level_name
            with open("progress.json", "w") as f:
                json.dump({"highest_level": self.highest_level}, f)

    def is_higher_level(self, new_level):
        levels = [f"1-{i}" for i in range(1,3)]  # Adjust for your level names
        return levels.index(new_level) > levels.index(self.highest_level)