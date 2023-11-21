import pygame
from pygame.sprite import Sprite


class Gun(Sprite):
    def __init__(self, screen):
        """Инициализация пушки"""
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("image/gun2.0.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False
        self.mtop = False
        self.mbottom = False

    def output(self):
        """Отображение пушки"""
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """Обновление позиции пушки"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.2
        if self.mleft and self.rect.left > self.screen_rect.left:
            self.center -= 1.2
        if self.mtop and self.rect.top > self.screen_rect.top:
            self.center_y -= 1.2
        if self.mbottom and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += 1.2
        self.rect.centerx = self.center
        self.rect.centery = self.center_y

    def create_gun(self):
        """Размецает пушку"""
        self.center = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center_y = self.rect.centery


