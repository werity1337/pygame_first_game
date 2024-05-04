import pygame
from parameters import Parameters
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.parameters = Parameters()
        self.screen = pygame.display.set_mode((self.parameters.screen_width, self.parameters.screen_height))
        pygame.display.set_caption("Zombie Shooter")
        pygame.display.set_icon(self.parameters.icon)
        self.game_start = False
        self.in_menu = True
        self.in_menu_options = False
        self.game_over = False

    def run_game(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(self.parameters.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()
        pygame.quit()

    def _check_game_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()

    def _check_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    def update_menu_screen(self):
        self.screen.blit(self.parameters.menu_background, (0, 0))
        pygame.display.update()



if __name__ == '__main__':
    ai = Game()
    ai.run_game()