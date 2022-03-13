import sys
import pygame
class Config:
    def __init__(self):
        self.fps = 60
        self.width = 300
        self.height = 200
        self.resolution = (self.width, self.height)
        self.bg_color = pygame.Color(100, 100, 100)
        self.name = "Minesweeper"

