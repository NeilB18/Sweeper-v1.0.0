class Restart:

    def __init__(self):
        self.game_over = False
    
    def update(self):
        self.game_over = True
    
    def reset_game(self):
        self.update()

        