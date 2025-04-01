import json
import os
#change 
class CoinMemento:
    """Stores the coin count as a memento."""
    def __init__(self, coin_count):
        self.coin_count = coin_count  # Make sure this is publicly accessible

    def get_coin_count(self):
        """Returns the stored coin count."""
        return self.coin_count

class CoinCaretaker:
    """Manages saving and loading of coin mementos."""
    SAVE_FILE = "entities/data/coin_data.json"  # Path to JSON storage file

    @staticmethod
    def save_memento(memento):
        """Saves the coin count to a JSON file."""
        os.makedirs(os.path.dirname(CoinCaretaker.SAVE_FILE), exist_ok=True)  # Create folder if missing
        with open(CoinCaretaker.SAVE_FILE, "w") as file:
            json.dump({"coin_count": memento.get_coin_count()}, file)

    @staticmethod
    def load_memento():
        """Loads the saved coin count from a JSON file, with error handling."""
        if os.path.exists(CoinCaretaker.SAVE_FILE):
            try:
                with open(CoinCaretaker.SAVE_FILE, "r") as file:
                    data = json.load(file)
                    return CoinMemento(data.get("coin_count", 0))
            except (json.JSONDecodeError, IOError):
                print("⚠️ Error loading coin data. Resetting to 0.")
                return CoinMemento(0)
        return CoinMemento(0)  # Default if file doesn't exist

class GameManager:
    """Manages the coin collection system."""
    def __init__(self):
        self.coin_memento = CoinCaretaker.load_memento()

    def save_coin_count(self, coin_count):
        """Saves the current coin count."""
        self.coin_memento = CoinMemento(coin_count)
        CoinCaretaker.save_memento(self.coin_memento)

    def load_coin_count(self):
        """Loads the saved coin count."""
        self.coin_memento = CoinCaretaker.load_memento()
        return self.coin_memento.coin_count  # Access the correct attribute
