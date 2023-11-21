import pygame
import time


class Ino(pygame.sprite.Sprite):
    """Класс пришельца"""

    def __init__(self, screen, speed=0):
        """Инициализируем начальную позицию на эркане"""
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("image/ino.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.new_speed = speed
        self.right = 0
        self.left = 0

    def draw(self):
        """Вывод пришельца на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self, right):
        self.y += 0.015 + self.new_speed
        self.rect.y = self.y
        if right:
            self.x += 0.022
        else:
            self.x -= 0.022
        self.rect.x = self.x



