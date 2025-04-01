class Command:
    def execute(self):
        pass

class ContinueCommand(Command):
    def _init_(self, game_main):
        self.game_main = game_main
        
    def execute(self):
        self.game_main.load_next_level()

class CancelCommand(Command):
    def _init_(self, game_main):
        self.game_main = game_main
        
    def execute(self):
        self.game_main.return_to_menu()