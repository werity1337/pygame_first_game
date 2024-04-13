import pygame

class Player:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.parameters = game.parameters
        self.screen_rect = game.screen.get_rect()
        