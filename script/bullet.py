import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """Создаем пулю в позиции пушки"""

        super(Bullet, self).__init__()
        self.screen = screen
        self.width = 3
        self.rect = pygame.Rect(0, 0, self.width, 12)
        self.color = 252, 248, 0
        self.speed = 3
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """Перемещение пули вверх"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Отображение пули на экране"""

        pygame.draw.rect(self.screen, self.color, self.rect)