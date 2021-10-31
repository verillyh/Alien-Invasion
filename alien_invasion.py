import sys
import pygame

class AlienInvasion:
    """Models the game"""

    def __init__(self):
        """Initializes the game, and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Main loop for the game"""
        while True:
            # Watches keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        
            # Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
