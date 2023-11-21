import pygame


class GameOver():
    def __init__(self, screen):
        """Инициализация"""
        self.screen = screen
        self.image = pygame.image.load("My_space_game/image/gameover.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def draw_im(self):
        """Вывод картинки окончация игры"""
        self.screen.blit(self.image, self.rect)