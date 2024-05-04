import pygame

class Parameters:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 800
        self.fps = 60

        self.icon = pygame.image.load("images/icon/pistol_icon.png")
        self.bullet_image = pygame.image.load("images/in_game_images/player/bullet.png")
        self.button_start = pygame.image.load("images/in_menu_images/start_button.png")
        self.menu_background = pygame.image.load("images/icon/backgrounds/background_in_menu.png")
        self.menu_background = pygame.transform.scale(self.menu_background,
                                                      (self.screen_width, self.screen_height))
        self.menu_title = pygame.image.load("images/icon/backgrounds/title.png")